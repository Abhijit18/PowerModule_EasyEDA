import unittest, json, csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class DesignContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract=json.loads((ROOT/'hardware/rev-c/design-contract.json').read_text())
    def test_battery_18650_single_protected_cell(self):
        c=self.contract
        self.assertEqual(c['battery']['cells_series'],1)
        self.assertEqual(c['battery']['protection'],'REQUIRED')
        self.assertIn('18650',c['battery']['chemistry'])
    def test_relay_pin_and_io_unchanged(self):
        c=self.contract
        self.assertEqual(c['controller']['relay_command_board_pin'],'D1')
        self.assertEqual(c['controller']['relay_command_soc_gpio'],3)
        self.assertEqual(c['interfaces']['breakouts'],[f'D{i}' for i in range(2,11)])
    def test_no_unverified_5v_backup(self):
        self.assertFalse(self.contract['controller']['battery_5V_boosted_output_present'])
        self.assertFalse(self.contract['fabrication_approved'])
    def test_hardware_tests_are_not_preapproved(self):
        with (ROOT/'docs/test-matrix.csv').open(newline='') as f:
            rows=list(csv.DictReader(f))
        self.assertTrue(len(rows)>=10)
        self.assertTrue(all(r['Status'] in ('NOT_RUN','PASS','FAIL') for r in rows))
        self.assertTrue(all(r['Status']=='NOT_RUN' or bool(r['Evidence'].strip()) for r in rows))
    def test_all_power_modes_unverified(self):
        self.assertTrue(all((not m['verified']) or bool(self.contract['power_mode_evidence'].get(m['name'])) for m in self.contract['power_modes']))
if __name__=='__main__':unittest.main()
