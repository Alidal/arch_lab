import json
from datetime import datetime


class PressureStatistic(object):
    """
    Class, that provides basic CRUD functionality for arterial pressure info.
    """

    def __init__(self, *args, **kwargs):
        """
        Initial method, that loads saved pressure statistic from json file.
        """
        self.table = json.load(open("db.json", "r"))

    def __del__(self):
        """
        Save pressure statistics to json file on object deletion.
        """
        json.dump(self.table, open("db.json", "w"))

    def add(self, pressure_list):
        """
        Add pressure value for today.

        Raises exception, if we already added todays values.

        >>> ps = PressureStatistic()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.add(['120', '80'])
        >>> len(ps.table) == 1
        True
        >>> ps.add(['120', '80'])
        Traceback (most recent call last):
        ...
        Exception: You've already added value today.
        >>> ps.table = tmp
        """
        now = datetime.now()
        if now.isoformat().split("T")[0] not in self.table:
            self.table[now.isoformat().split("T")[0]] = pressure_list
        else:
            raise Exception("You've already added value today.")

    def update(self, date, pressure_list):
        """
        Update or create new record in table.
        Args:
            date - datetime object. Points, what day we need to update.
            pressure_list - list object (size=2).

        >>> ps = PressureStatistic()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(datetime(2016, 3, 11, 0, 0), ['120', '80'])
        >>> ps.table['2016-03-11'] == ['120', '80']
        True
        >>> ps.table = tmp
        """
        self.table[date.isoformat().split("T")[0]] = pressure_list

    def delete(self, date):
        """
        Drops record by key.
        Args:
            date - datetime object. Points, what day we need to update.

        >>> ps = PressureStatistic()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(datetime(2016, 3, 11, 0, 0), ['120', '80'])
        >>> len(ps.table) == 1
        True
        >>> ps.delete(datetime(2016, 3, 11, 0, 0))
        >>> ps.table
        {}
        >>> ps.table = tmp
        """
        try:
            del self.table[date.isoformat().split("T")[0]]
        except:
            raise Exception("Wrong date.")
