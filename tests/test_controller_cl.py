from datetime import date
from unittest import TestCase
from unittest.mock import patch
from controller_cl import ControllerCL


class ControllerCLTestCase(TestCase):

    @patch('backends.get_pickle.PickleSerializer.read', return_value={})
    def setUp(self, get_mock):
        self.controller = ControllerCL()

    @patch('backends.get_pickle.PickleSerializer.read', return_value={})
    def test__init__(self, get_mock):
        controller = ControllerCL()
        self.assertTrue(controller.view is not None)
        self.assertTrue(controller.model is not None)

        controller = ControllerCL(view='view', model='model')
        self.assertEqual(controller.view, 'view')
        self.assertEqual(controller.model, 'model')

    @patch('controller_cl.ControllerCL.input_pressure')
    @patch('controller_cl.ControllerCL.input_date')
    def test_run(self, *mocks):
        with patch('sys.argv', ['main.py', '-a']):
            with patch('model.PressureStatistics.add', side_effect=Exception()) as add_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(add_mock.called)
        with patch('sys.argv', ['main.py', '-u']):
            with patch('model.PressureStatistics.update', side_effect=Exception()) as update_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(update_mock.called)
        with patch('sys.argv', ['main.py', '-d']):
            with patch('model.PressureStatistics.delete', side_effect=Exception()) as delete_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(delete_mock.called)
        with patch('sys.argv', ['main.py', '-pw']):
            with patch('view.View.print_for_week', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)
        with patch('sys.argv', ['main.py', '-pm']):
            with patch('view.View.print_for_month', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)
        with patch('sys.argv', ['main.py', '-p']):
            with patch('view.View.print_all', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)

        with patch('sys.argv', ['main.py']):
            with patch('view.View.print_exception', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                print_mock.assert_called_once_with(self.controller.view.responses['choose_valid_option'])

    def test_input_pressure(self):
        with patch('view.View.get_pressure_choice') as input_mock:
            input_mock.return_value = "120, 80"
            result = self.controller.input_pressure()
            self.assertEqual(result, ["120", "80"])

            with patch('view.View.print_exception', side_effect=Exception("Test")) as print_mock:
                input_mock.return_value = "120, 80, 60"
                try:
                    self.controller.input_pressure()
                except:
                    pass
                print_mock.assert_called_once_with("You've entered wrong value. Try again")
                print_mock.reset_mock()

                input_mock.return_value = "120, 800"
                try:
                    self.controller.input_pressure()
                except:
                    pass
                print_mock.assert_called_once_with("You've entered wrong value. Try again")
                print_mock.reset_mock()

                input_mock.return_value = "120, -80"
                try:
                    self.controller.input_pressure()
                except:
                    pass
                print_mock.assert_called_once_with("You've entered wrong value. Try again")
                print_mock.reset_mock()

    def test_input_date(self):
        with patch('view.View.get_date_choice') as input_mock:
            input_mock.return_value = "2016-2-1"
            result = self.controller.input_date()
            self.assertEqual(result, date(2016, 2, 1))

            with patch('view.View.print_exception', side_effect=Exception("Test")) as print_mock:
                input_mock.return_value = "sdfgsdfg"
                try:
                    self.controller.input_date()
                except:
                    pass
                print_mock.assert_called_once_with("You've entered wrong value. Try again")
                print_mock.reset_mock()
