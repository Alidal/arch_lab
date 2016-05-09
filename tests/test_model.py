from datetime import date
from unittest import TestCase
from unittest.mock import patch
from model import PressureStatistics


class ModelTestCase(TestCase):

    @patch('backends.get_pickle.PickleSerializer.read', return_value={})
    def setUp(self, get_mock):
        self.model = PressureStatistics()

    def test__init__(self):
        with patch('backends.get_pickle.PickleSerializer.read') as get_mock:
            PressureStatistics()
            get_mock.assert_called_once_with()

    def test_add(self):
        self.assertFalse(self.model.table)
        self.model.add(["120", "80"])

        self.assertEqual(len(self.model.table), 1)
        self.assertEqual(self.model.table[date.today().isoformat()], ["120", "80"])

    def test_update(self):
        self.model.table = {"2016-01-01": ["120", "90"]}
        self.assertEqual(len(self.model.table), 1)
        self.model.update(date(2016, 1, 1), ["130", "80"])
        self.assertEqual(len(self.model.table), 1)
        self.assertEqual(self.model.table["2016-01-01"], ["130", "80"])

    def test_delete(self):
        self.model.table = {"2016-01-01": ["120", "90"]}
        self.assertEqual(len(self.model.table), 1)
        self.model.delete(date(2016, 1, 1))
        self.assertEqual(len(self.model.table), 0)

        # Check wrong date handling
        with self.assertRaises(Exception):
            self.model.delete(date(2016, 1, 1))

    def test_save(self):
        with patch('backends.get_pickle.PickleSerializer.write') as set_mock:
            self.model.table = {"2016-01-01": ["120", "90"]}
            self.model.save()
            set_mock.assert_called_once_with({"2016-01-01": ["120", "90"]})

    def test__str__(self):
        # Check empty table
        self.assertEqual(str(self.model), "Table is empty.")

        # Check format
        self.model.table = {"2016-01-01": ["120", "90"],
                            "2016-02-02": ["130", "70"]}
        result = str(self.model)
        expected_result = "2016-01-01 - 120, 90\n2016-02-02 - 130, 70\n"
        self.assertEqual(result, expected_result)
