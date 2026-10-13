"""Run with: python3 -m unittest discover -s tools -p 'test_court.py'."""
import argparse
import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import court


DOCKET = '92-7302, 93-7918; 67 F.3d 359 (2d Cir. 1994).'
PANEL = ('James L. Oakes (Senior Circuit Judge); Thomas J. Meskill (Senior Circuit Judge); '
         'Frank X. Altimari (Active Circuit Judge). Source: historical header.')


def packet(docket=DOCKET, panel=PANEL):
    return f'**Docket or citation:** {docket}\n\n**Historical panel:** {panel}\n\n**Replacement exclusions:** None.\n'


def complete_packet():
    text = packet()
    draw = court.packet_draw(text)
    return text + '\n'.join(f'**{label}:** {value}' for label, value in court.assignment_fields('example-case', draw).items()) + '\n'


class PanelDrawTests(unittest.TestCase):
    def test_typography_roles_source_notes_and_order_do_not_change_draw(self):
        expected = court.panel_draw(DOCKET, PANEL)
        changed = court.panel_draw(
            'Dockets 93 – 07918 ; 92 - 7302, 92-7302; 67 F.3d 359, 361-62 (1994)',
            '**HON. FRANK X ALTIMARI** (Circuit Judge); '
            '[James L Oakes](https://example.test/judge) (Senior); '
            ' Thomas   J.Meskill (Judge). Source: a different source; ignored name.')
        self.assertEqual(expected['docket'], changed['docket'])
        self.assertEqual([court.judge_key(x) for x in expected['order']],
                         [court.judge_key(x) for x in changed['order']])
        self.assertEqual(court.judge_key(changed['selected']), 'frankxaltimari')

    def test_accents_punctuation_and_honorifics_normalize(self):
        self.assertEqual(court.judge_key('Hon. José A. Cabranes (Active Circuit Judge)'),
                         court.judge_key('  JOSE A CABRANES '))
        self.assertEqual(court.judge_key('Ralph K. Winter, Jr. (Judge)'),
                         court.judge_key('Ralph K Winter Jr'))
        self.assertNotEqual(court.judge_key('John M. Walker'), court.judge_key('John Walker'))

    def test_calabresi_always_takes_priority(self):
        panel = 'James L. Oakes; GUIDO CALABRESI (Active Circuit Judge); Frank X. Altimari'
        result = court.panel_draw('94-1234', panel)
        self.assertTrue(result['calabresi'])
        self.assertEqual(court.judge_key(result['selected']), 'guidocalabresi')
        with self.assertRaisesRegex(ValueError, 'cannot remain'):
            court.panel_draw('94-1234', panel, 'Guido Calabresi = legal obstacle in supplied order')

    def test_exclusion_advances_only_in_the_same_order(self):
        first = court.panel_draw(DOCKET, PANEL)
        reason = court.judge_name(first['order'][0]) + ' = legal ineligibility established by the supplied order'
        second = court.panel_draw(DOCKET, PANEL, reason)
        self.assertEqual(first['order'], second['order'])
        self.assertEqual(second['selected'], first['order'][1])
        all_excluded = '; '.join(court.judge_name(x) + ' = supplied legal order' for x in first['panel'])
        with self.assertRaisesRegex(ValueError, 'no historical seat'):
            court.panel_draw(DOCKET, PANEL, all_excluded)

    def test_invalid_inputs_fail_instead_of_guessing(self):
        for docket, panel, excluded in [
            ('67 F.3d 359 (1994)', PANEL, 'None'),
            (DOCKET, 'James Oakes; Thomas Meskill', 'None'),
            (DOCKET, 'José A. Cabranes; JOSE A CABRANES; James Oakes', 'None'),
            (DOCKET, PANEL, 'Frank X. Altimari = '),
            (DOCKET, PANEL, 'Unknown Judge = supplied legal order'),
        ]:
            with self.subTest(docket=docket, panel=panel, excluded=excluded), self.assertRaises(ValueError):
                court.panel_draw(docket, panel, excluded)

    def test_packet_lookup_is_exact_and_read_only(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            location = root / 'years/1994/cases/example-case/neutral.md'
            location.parent.mkdir(parents=True)
            original = complete_packet()
            location.write_text(original)
            args = argparse.Namespace(case='example-case', docket=None, panel=None)
            with patch.object(court, 'ROOT', root), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(court.cmd_draw(args), 0)
            self.assertIn('**Member Stone replaces:** Frank X. Altimari', output.getvalue())
            self.assertEqual(location.read_text(), original)
            with patch.object(court, 'ROOT', root):
                for slug in ['../example-case', 'missing-case']:
                    with self.assertRaises(ValueError):
                        court.case_packet(slug)
                second = root / 'years/1995/cases/example-case/neutral.md'
                second.parent.mkdir(parents=True)
                second.write_text(original)
                with self.assertRaisesRegex(ValueError, 'exactly one'):
                    court.case_packet('example-case')

    def test_case_mode_rejects_manual_overrides(self):
        args = argparse.Namespace(case='example-case', docket='99-9999', panel=PANEL)
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(court.cmd_draw(args), 1)

    def test_stored_panel_and_basis_must_match(self):
        text = complete_packet()
        self.assertEqual(court.assignment_errors(text, 'example-case'), [])
        wrong = text.replace('**Member Stone replaces:** Frank X. Altimari',
                             '**Member Stone replaces:** James L. Oakes')
        self.assertTrue(any('replaced judge' in x for x in court.assignment_errors(wrong, 'example-case')))
        wrong = text.replace('Judge Stone (Circuit Judge)', 'Frank X. Altimari (Circuit Judge)')
        self.assertTrue(any('resulting panel' in x for x in court.assignment_errors(wrong, 'example-case')))
        wrong = text.replace('Exactly one seat changes', 'Two seats change')
        self.assertTrue(any('basis' in x for x in court.assignment_errors(wrong, 'example-case')))

    def test_staging_refuses_a_stale_assignment(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / 'example-case'
            folder.mkdir()
            (folder / 'neutral.md').write_text(complete_packet().replace(
                '**Member Stone replaces:** Frank X. Altimari', '**Member Stone replaces:** James L. Oakes'))
            case = argparse.Namespace(slug='example-case', folder=folder)
            args = argparse.Namespace(slug='example-case', stage='neutral')
            with patch.object(court, 'load_cases', return_value=([case], [])):
                with self.assertRaisesRegex(SystemExit, 'assignment must be fixed'):
                    court.cmd_stage(args)


if __name__ == '__main__':
    unittest.main()
