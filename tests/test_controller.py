from datetime import date
from unittest import TestCase
from unittest.mock import patch
from controller import Controller


class ControllerTestCase(TestCase):

    @patch('backends.get_pickle.PickleSerializer.read', return_value={})
    def setUp(self, get_mock):
        self.controller = Controller()

    @patch('backends.get_pickle.PickleSerializer.read', return_value={})
    def test__init__(self, get_mock):
        controller = Controller()
        self.assertTrue(controller.view is not None)
        self.assertTrue(controller.model is not None)

        controller = Controller(view='view', model='model')
        self.assertEqual(controller.view, 'view')
        self.assertEqual(controller.model, 'model')

    @patch('controller.Controller.input_pressure')
    @patch('controller.Controller.input_date')
    def test_run(self, *mocks):
        with patch('view.View.get_main_menu_choice', return_value=1):
            with patch('model.PressureStatistics.add', side_effect=Exception()) as add_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(add_mock.called)
        with patch('view.View.get_main_menu_choice', return_value=2):
            with patch('model.PressureStatistics.update', side_effect=Exception()) as update_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(update_mock.called)
        with patch('view.View.get_main_menu_choice', return_value=3):
            with patch('model.PressureStatistics.delete', side_effect=Exception()) as delete_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(delete_mock.called)
        with patch('view.View.get_main_menu_choice', return_value=4):
            with patch('view.View.print_for_week', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)
        with patch('view.View.get_main_menu_choice', return_value=5):
            with patch('view.View.print_for_month', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)
        with patch('view.View.get_main_menu_choice', return_value=6):
            with patch('view.View.print_all', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertTrue(print_mock.called)

        with patch('view.View.get_main_menu_choice', return_value=56):
            with patch('view.View.print_exception', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                print_mock.assert_called_once_with("Enter value between 1 and 7.")
        with patch('view.View.get_main_menu_choice', return_value="abcs"):
            with patch('view.View.print_exception', side_effect=Exception()) as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                print_mock.assert_called_once_with("Wrong value! Enter number.")

        with patch('view.View.get_main_menu_choice', side_effect=Exception("Test")):
            with patch('view.View.print_exception') as print_mock:
                try:
                    self.controller.run()
                except:
                    pass
                self.assertEqual(print_mock.call_count, 1)

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
