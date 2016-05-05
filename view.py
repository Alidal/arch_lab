"""
View module, that contains all functions that interacts with command line.
"""

import argparse
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

    def get_main_menu_choice_cli(self):
        """
        Get main menu input from console. (by command options)
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("-a", "--addtoday", action="store_true")
        parser.add_argument("-u", "--update", action="store_true")
        parser.add_argument("-d", "--delete", action="store_true")
        parser.add_argument("-pw", "--printweek", action="store_true")
        parser.add_argument("-pm", "--printmonth", action="store_true")
        parser.add_argument("-p", "--printall", action="store_true")

        arguments = parser.parse_args()
        if arguments.addtoday:
            return 1
        elif arguments.update:
            return 2
        elif arguments.delete:
            return 3
        elif arguments.printweek:
            return 4
        elif arguments.printmonth:
            return 5
        elif arguments.printall:
            return 6
        else:
            raise Exception("Choose option")

    def get_main_menu_choice_simple(self):
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
        for record_date, pressure in self.model.table.items():
            if dateutil.parser.parse(record_date).date() > lower_border:
                print("{} - {}, {}".format(record_date, pressure[0], pressure[1]))
                written = True
        if not written:
            self.print_exception(self.responses['empty_table'])

    def print_for_week(self):
        """
        Show records only for last week. Older records wont be showned.

        >>> ps = PressureStatistics()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(date(2016, 3, 25), ['120', '80'])
        >>> ps.update(date(2016, 2, 11), ['120', '80'])
        >>> show_for_week(ps)
        Pressure statistic for last week:
        2016-03-25 - 120, 80
        >>> ps.table = tmp
        """
        print(self.responses['ps_for_week'])
        self.print_for_time(timedelta(weeks=1))

    def print_for_month(self):
        """
        Show records only for last week. Older records wont be showned.

        >>> ps = PressureStatistics()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(date(2016, 3, 11), ['120', '80'])
        >>> ps.update(date(2016, 3, 1), ['120', '80'])
        >>> ps.update(date(2016, 2, 1), ['120', '80'])
        >>> show_for_month(ps)
        Pressure statistic for last month:
        2016-03-11 - 120, 80
        2016-03-01 - 120, 80
        >>> ps.table = tmp
        """
        print(self.responses['ps_for_month'])
        self.print_for_time(timedelta(days=30))

    def print_all(self):
        """
        Show all records.

        >>> ps = PressureStatistics()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(date(2016, 3, 11), ['120', '80'])
        >>> ps.update(date(2016, 3, 1), ['120', '80'])
        >>> ps.update(date(2016, 2, 1), ['120', '80'])
        >>> print_all(ps)
        Pressure statistic for all time:
        2016-03-11 - 120, 80
        2016-03-01 - 120, 80
        2016-02-01 - 120, 80
        >>> ps.table = tmp
        """
        print(self.responses['ps_all'])
        print(self.model)

    def print_exception(self, text):
        """Highlight exceptions."""
        print("\033[91m{}\033[0m".format(text))
