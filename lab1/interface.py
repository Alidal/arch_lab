"""
Interface module. Contains all function, that provides interface functionality.
"""
import dateutil.parser
from pressure_table import PressureStatistic
from console_input import get_main_menu_choice, get_date_choice, get_pressure_choice


def main_interface():
    """
    Main interface function. Provides menu functionality.
    """
    pressure_stat = PressureStatistic()
    while True:
        try:
            choice = int(get_main_menu_choice())
            assert(0 < choice < 7)

            if choice == 1:
                pressure_stat.add(input_pressure())
            elif choice == 2:
                pressure_stat.update(input_date(), input_pressure())
            elif choice == 3:
                pressure_stat.delete(input_date())
            elif choice == 4:
                pressure_stat.show_for_week()
            elif choice == 5:
                pressure_stat.show_for_month()
            elif choice == 6:
                return
        except ValueError:
                print("Wrong value! Enter number.")
        except AssertionError:
            print("Enter value between 1 and 6.")
        except Exception as e:
            print(e.args[0])


def input_pressure():
    """
    Input logic for blood pressure. Validates entered data.
    """
    while True:
        pressure = get_pressure_choice()
        pressure = pressure.split(',')
        if len(pressure) == 2 and\
                0 < int(pressure[0]) < 250 and 0 < int(pressure[1]) < 250:
            return pressure

        print("You've entered wrong value. Try again")


def input_date():
    """
    Input logic for date. Validates entered data.
    """
    while True:
        date = get_date_choice()
        try:
            return dateutil.parser.parse(date)
        except ValueError:
            print("You've entered wrong value. Try again")
