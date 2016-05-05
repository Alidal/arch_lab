from unittest import TestCase
from unittest import mock
from .model import PressureStatistics


@mock.patch('pickle_backend.open')
class ModelTestCase(TestCase):
    def setUp(self):
        self.model = PressureStatistics()
