"""
Controller module. Contains all function, that provides interface functionality.
"""
import dateutil.parser
import argparse
from datetime import date

from model import PressureStatistics
from view import View


class ControllerCL:

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
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--addtoday", action="store_true")
        parser.add_argument("-u", "--update", action="store_true")
        parser.add_argument("-d", "--delete", action="store_true")
        parser.add_argument("-pw", "--printweek", action="store_true")
        parser.add_argument("-pm", "--printmonth", action="store_true")
        parser.add_argument("-p", "--printall", action="store_true")
        while True:
            try:
                arguments = parser.parse_args()
                if arguments.addtoday:
                    self.model.add(self.input_pressure())
                elif arguments.update:
                    self.model.update(self.input_date(), self.input_pressure())
                elif arguments.delete:
                    self.model.delete(self.input_date())
                elif arguments.printweek:
                    self.view.print_for_week()
                elif arguments.printmonth:
                    self.view.print_for_month()
                elif arguments.printall:
                    self.view.print_all()
                else:
                    raise Exception(self.view.responses['choose_valid_option'])
                return
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
