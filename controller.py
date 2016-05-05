"""
Controller module. Contains all function, that provides interface functionality.
"""
import dateutil.parser
import configparser
from datetime import date

from model import PressureStatistics
from view import View


class Controller:

    def __init__(self, view=None, model=None):
        """
        Initial function. If parameters don't passed
        creates view and model instances for controller
        :params:
            view: View instance
            model: Model instance
        """
        if not model:
            model = PressureStatistics()
        if not view:
            view = View(model)
        self.model = model
        self.view = view

    def run(self):
        """
        Main interface function. Provides menu functionality.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        interface_type = config['interface']['type']
        stop_execution = False
        while True:
            try:
                if interface_type == "cli":
                    choice = int(self.view.get_main_menu_choice_cli())
                    stop_execution = True
                else:
                    choice = int(self.view.get_main_menu_choice_simple())
                assert(0 < choice < 8)

                if choice == 1:
                    self.model.add(self.input_pressure())
                elif choice == 2:
                    self.model.update(self.input_date(), self.input_pressure())
                elif choice == 3:
                    self.model.delete(self.input_date())
                elif choice == 4:
                    self.view.print_for_week()
                elif choice == 5:
                    self.view.print_for_month()
                elif choice == 6:
                    self.view.print_all()
                elif choice == 7:
                    return

                if stop_execution:
                    return
            except ValueError:
                self.view.print_exception("Wrong value! Enter number.")
            except AssertionError:
                self.view.print_exception("Enter value between 1 and 7.")
            except Exception as e:
                self.view.print_exception(e.args[0])
                return

    def input_pressure(self):
        """
        Input logic for blood pressure. Validates entered data.
        """
        while True:
            pressure = self.view.get_pressure_choice()
            pressure = pressure.replace(" ", "").split(',')
            if len(pressure) == 2 and\
                    0 < int(pressure[0]) < 250 and 0 < int(pressure[1]) < 250:
                return pressure

            self.view.print_exception("You've entered wrong value. Try again")

    def input_date(self):
        """
        Input logic for date. Validates entered data.
        """
        while True:
            date_input = self.view.get_date_choice()
            try:
                date_input = dateutil.parser.parse(date_input).date()
                assert(date_input < date.today())
                return date_input
            except ValueError:
                self.view.print_exception("You've entered wrong value. Try again")
