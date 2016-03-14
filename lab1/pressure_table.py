import json
import dateutil.parser

from datetime import datetime, timedelta


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

    def _show_for_time(self, time):
        last_week = datetime.now() - time
        for date, pressure in self.table.items():
            if dateutil.parser.parse(date) > last_week:
                print("{} - {}, {}".format(date, pressure[0], pressure[1]))

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

    def show_for_week(self):
        """
        Show records only for last week. Older records wont be showned.

        >>> ps = PressureStatistic()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(datetime(2016, 3, 11, 0, 0), ['120', '80'])
        >>> ps.update(datetime(2016, 2, 11, 0, 0), ['120', '80'])
        >>> ps.show_for_week()
        Pressure statistic for last week:
        2016-03-11 - 120, 80
        >>> ps.table = tmp
        """
        print("Pressure statistic for last week:")
        self._show_for_time(timedelta(weeks=1))

    def show_for_month(self):
        """
        Show records only for last week. Older records wont be showned.

        >>> ps = PressureStatistic()
        >>> tmp = ps.table
        >>> ps.table = {}
        >>> ps.update(datetime(2016, 3, 11, 0, 0), ['120', '80'])
        >>> ps.update(datetime(2016, 3, 1, 0, 0), ['120', '80'])
        >>> ps.update(datetime(2016, 2, 1, 0, 0), ['120', '80'])
        >>> ps.show_for_month()
        Pressure statistic for last month:
        2016-03-11 - 120, 80
        2016-03-01 - 120, 80
        >>> ps.table = tmp
        """
        print("Pressure statistic for last month:")
        self._show_for_time(timedelta(days=30))
