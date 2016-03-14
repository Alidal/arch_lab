import json
from datetime import datetime, timedelta
import dateutil.parser


class PressureStatistic(object):
    """
    Class, that provides basic CRUD functionality for arterial pressure info.
    """
    def __init__(self, *args, **kwargs):
        self.table = json.load(open("db.json", "r"))

    def __del__(self):
        json.dump(self.table, open("db.json", "w"))

    def _show_for_time(self, time):
        last_week = datetime.now() - time
        for date, pressure in self.table.items():
            if dateutil.parser.parse(date) > last_week:
                print("{} - {}".format(date, pressure))

    def add(self, pressure_list):
        now = datetime.now()
        if now.isoformat().split("T")[0] not in self.table:
            self.table[now.isoformat().split("T")[0]] = pressure_list
        else:
            raise Exception("You've already added value today.")

    def update(self, date, pressure_list):
        self.table[date.isoformat().split("T")[0]] = pressure_list

    def delete(self, date):
        try:
            del self.table[date.isoformat().split("T")[0]]
        except:
            raise Exception("Wrong date.")

    def show_for_week(self):
        print("Pressure statistic for last week:")
        self._show_for_time(timedelta(weeks=1))

    def show_for_month(self):
        print("Pressure statistic for last month:")
        self._show_for_time(timedelta(days=30))
