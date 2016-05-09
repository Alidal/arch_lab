import pickle

from unittest import TestCase
from unittest.mock import patch, mock_open
from backends import get_pickle, get_json, get_yaml


class TestPickleBackend(TestCase):

    def setUp(self):
        self.backend = get_pickle.PickleSerializer()
        self.testval = {"2016-05-04": ["120", "80"]}

    def test_read(self):
        with patch("pickle.load", return_value=self.testval):
            with patch.object(get_pickle, 'open', mock_open(), create=True) as m:
                result = self.backend.read()

        m.assert_called_once_with('backends/db.pkl', 'rb')
        self.assertEqual(result, self.testval)

    def test_write(self):
        m = mock_open()
        with patch.object(get_pickle, 'open', m, create=True):
            self.backend.write(self.testval)
        m.assert_called_once_with('backends/db.pkl', 'wb')
        handle = m()
        handle.write.assert_called_once_with(pickle.dumps(self.testval))


class TestJsonBackend(TestCase):
    
    def setUp(self):
        self.backend = get_json.JsonSerializer()
        self.testval = {"2016-05-04": ["120", "80"]}

    def test_read(self):
        with patch("json.load", return_value=self.testval):
            with patch.object(get_json, 'open', mock_open(), create=True) as m:
                result = self.backend.read()

        m.assert_called_with('backends/db.json', 'r')
        self.assertEqual(result, self.testval)

    def test_write(self):
        with patch("json.dump") as json_mock:
            m = mock_open()
            with patch.object(get_json, 'open', m, create=True):
                self.backend.write(self.testval)
            m.assert_called_with('backends/db.json', 'w')
            self.assertEqual(len(json_mock.mock_calls), 1)


class TestYamlBackend(TestCase):
    def setUp(self):
        self.backend = get_yaml.YamlSerializer()
        self.testval = {"2016-05-04": ["120", "80"]}

    def test_read(self):
        with patch("yaml.load", return_value=self.testval):
            with patch.object(get_yaml, 'open', mock_open(), create=True) as m:
                result = self.backend.read()

        m.assert_called_with('backends/db.yaml', 'r')
        self.assertEqual(result, self.testval)

    def test_write(self):
        with patch("yaml.dump") as yaml_mock:
            m = mock_open()
            with patch.object(get_yaml, 'open', m, create=True):
                self.backend.write(self.testval)
            m.assert_called_with('backends/db.yaml', 'w')
            self.assertEqual(len(yaml_mock.mock_calls), 1)
