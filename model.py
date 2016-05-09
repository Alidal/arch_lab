"""
Model module, that contains all functions, that we need to manipulate data.
"""
import configparser
from pydoc import locate
from datetime import date

config = configparser.ConfigParser()
config.read('config.ini')
backend = locate('backends.get_%s.%sSerializer' %\
    (config['backend']['type'], config['backend']['type'].capitalize()))


class PressureStatistics:
    """
    Class, that provides basic CRUD functionality for arterial pressure info.
    """

    def __init__(self, *args, **kwargs):
        """
        Initial method, that loads saved pressure statistic from file.
        """
        self.backend = backend()
        self.table = self.backend.read() or {}

    def save(self):
        """
        Sericalize and save pressure statistics to file on object deletion.
        """
        self.backend.write(self.table)

    def add(self, pressure_list):
        """
        Add pressure value for today.
        Raises exception, if we already added todays values.
        """
        today = date.today().isoformat()
        if today not in self.table:
            self.table[today] = pressure_list
        else:
            raise Exception("You've already added value today.")

    def update(self, date, pressure_list):
        """
        Update or create new record in table.
        Args:
            date - date object. Points, what day we need to update.
            pressure_list - list object (size=2).
        """
        self.table[date.isoformat()] = pressure_list

    def delete(self, date):
        """
        Drops record by key.
        Args:
            date - date object. Points, what day we need to update.
        """
        try:
            del self.table[date.isoformat().split("T")[0]]
        except:
            raise Exception("Wrong date.")

    def __str__(self):
        """
        String representation for class instance.
        Returns table if table exists. Otherway returns message,
        that table is empty.
        """
        string = ""
        for date_, pressure in sorted(self.table.items()):
            string += "{} - {}, {}\n".format(date_, pressure[0], pressure[1])
        if not self.table:
            string = "Table is empty."
        return string
