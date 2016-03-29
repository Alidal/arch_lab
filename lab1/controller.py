"""
Interface module. Contains all function, that provides interface functionality.
"""
import dateutil.parser
from datetime import datetime

from model import PressureStatistic
from view import get_main_menu_choice, get_date_choice, print_exception,\
    get_pressure_choice, print_for_week, print_for_month, print_all


def main():
    """
    Main interface function. Provides menu functionality.
    """
    pressure_stat = PressureStatistic()
    while True:
        try:
            choice = int(get_main_menu_choice())
            assert(0 < choice < 8)

            if choice == 1:
                pressure_stat.add(input_pressure())
            elif choice == 2:
                pressure_stat.update(input_date(), input_pressure())
            elif choice == 3:
                pressure_stat.delete(input_date())
            elif choice == 4:
                print_for_week(pressure_stat)
            elif choice == 5:
                print_for_month(pressure_stat)
            elif choice == 6:
                print_all(pressure_stat)
            elif choice == 7:
                return

        except ValueError:
            print_exception("Wrong value! Enter number.")
        except AssertionError:
            print_exception("Enter value between 1 and 7.")
        except Exception as e:
            print_exception(e.args[0])
            return


def input_pressure():
    """
    Input logic for blood pressure. Validates entered data.
    """
    while True:
        pressure = get_pressure_choice()
        pressure = pressure.replace(" ", "").split(',')
        if len(pressure) == 2 and\
                0 < int(pressure[0]) < 250 and 0 < int(pressure[1]) < 250:
            return pressure

        print_exception("You've entered wrong value. Try again")


def input_date():
    """
    Input logic for date. Validates entered data.
    """
    while True:
        date = get_date_choice()
        try:
            date = dateutil.parser.parse(date)
            assert(date < datetime.now)
            return date
        except ValueError:
            print_exception("You've entered wrong value. Try again")

if __name__ == "__main__":
    main()
