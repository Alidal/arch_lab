import dateutil.parser
from datetime import datetime, timedelta


def get_main_menu_choice():
    """
    Get main menu input from console.
    """
    return input("""
Choose one of menu items:
1. Add today value.
2. Update existing record.
3. Delete record.
4. Show statistic for last week.
5. Show statistic for last month.
6. Show all records in table.
7. Exit.\n
Enter value: """)


def get_pressure_choice():
    """
    Get pressure from console.
    """
    return input("""
Enter values in format: systolic pressure, diastolic pressure
(remember about comma):""")


def get_date_choice():
    """
    Get date from console.
    """
    return input("Enter date in format: 01.11.2016:")


def print_for_time(pressure_stat, time):
    """
    Print records that have date more than passed `time` parameter.
    """
    lower_border = datetime.now() - time
    for date, pressure in pressure_stat.table.items():
        if dateutil.parser.parse(date) > lower_border:
            print("{} - {}, {}".format(date, pressure[0], pressure[1]))


def print_for_week(pressure_stat):
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
    print_for_time(pressure_stat, timedelta(weeks=1))


def print_for_month(pressure_stat):
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
    print_for_time(pressure_stat, timedelta(days=30))


def print_all(pressure_stat):
    """
    Show all records.

    >>> ps = PressureStatistic()
    >>> tmp = ps.table
    >>> ps.table = {}
    >>> ps.update(datetime(2016, 3, 11, 0, 0), ['120', '80'])
    >>> ps.update(datetime(2016, 3, 1, 0, 0), ['120', '80'])
    >>> ps.update(datetime(2016, 2, 1, 0, 0), ['120', '80'])
    >>> ps.show_for_month()
    Pressure statistic for all time:
    2016-03-11 - 120, 80
    2016-03-01 - 120, 80
    2016-02-01 - 120, 80
    >>> ps.table = tmp
    """
    print("Pressure statistic for all time:")
    print_for_time(pressure_stat, timedelta(weeks=10000))


def print_exception(text):
    """Function that highlights exceptions."""
    print("\033[91m{}\033[0m".format(text))
