import io
import pickle
from unittest import TestCase
from unittest import mock
from backends import get_pickle


@mock.patch('backends.get_pickle.get')
@mock.patch('backends.get_pickle.set')
class TestPickleBackend(TestCase):
    fbk = get_pickle.PickleFileBackend
    testval = [123, 123]

    def setUp(self):
        self.fakefil = io.BytesIO()

    def test_save(self, mopen):
        mopen().__enter__.return_value = self.fakefil
        self.fbk.save("/tmp/blah", self.testval)

        self.fakefil.seek(0)
        self.assertEqual(self.testval, pickle.load(self.fakefil))

    def test_read_correct(self, mopen):
        mopen().__enter__.return_value = self.fakefil
        pickle.dump(self.testval, self.fakefil)

        self.fakefil.seek(0)
        self.assertEqual(self.testval, self.fbk.load(self.fakefil))
