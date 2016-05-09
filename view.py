"""
View class, that contains all functions that interacts with command line.
"""
import configparser
import dateutil.parser
from datetime import date, timedelta

from lang import lang


class View:

    def __init__(self, model=None):
        self.model = model

        config = configparser.ConfigParser()
        config.read('config.ini')
        self.responses = lang[config['language']['type']]

    def get_main_menu_choice(self):
        """
        Get main menu input from console. (interactive mode)
        """
        return input(self.responses['main_menu_cli_choice'])

    def get_pressure_choice(self):
        """
        Get pressure from console.
        """
        return input(self.responses['pressure_choice'])

    def get_date_choice(self):
        """
        Get date from console.
        """
        return input(self.responses['date_choice'])

    def print_for_time(self, time):
        """
        Print records that have date more than passed `time` parameter.
        """
        lower_border = date.today() - time
        written = False
        for record_date, pressure in sorted(self.model.table.items()):
            if dateutil.parser.parse(record_date).date() > lower_border:
                print("{} - {}, {}".format(record_date, pressure[0], pressure[1]))
                written = True
        if not written:
            self.print_exception(self.responses['empty_table'])

    def print_for_week(self):
        """
        Show records only for last week. Older records wont be showned.
        """
        print(self.responses['ps_for_week'])
        self.print_for_time(timedelta(weeks=1))

    def print_for_month(self):
        """
        Show records only for last week. Older records wont be showned.
        """
        print(self.responses['ps_for_month'])
        self.print_for_time(timedelta(days=30))

    def print_all(self):
        """
        Show all records.
        """
        print(self.responses['ps_all'])
        print(self.model)

    def print_exception(self, text):
        """Highlight exceptions."""
        print("\033[91m{}\033[0m".format(text))
