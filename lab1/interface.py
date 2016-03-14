from pressure_table import PressureStatistic
import dateutil.parser


def main_interface():
    while True:
        choice = input(
            "Choose one of menu items:\n" +
            "1. Add today value.\n" +
            "2. Update existing record.\n" +
            "3. Delete record.\n" +
            "4. Show statistic for last week.\n" +
            "5. Show statistic for last month.\n" +
            "6. Exit.\n\n" +
            "Enter value: "
        )
        try:
            choice = int(choice)
            assert(0 < choice < 7)
            break
        except ValueError:
            print("Wrong value! Enter number.")
        except AssertionError:
            print("Enter value between 1 and 6.")

    pressure_stat = PressureStatistic()
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


def input_pressure():
    while True:
        pressure = input(
            """
            Enter values in format: systolic pressure, diastolic pressure 
            (remember about comma):
            """
        )
        pressure = pressure.split(',')
        if len(pressure) == 2 and\
                0 < int(pressure[0]) < 250 and 0 < int(pressure[1]) < 250:
            return pressure

        print("You've entered wrong value. Try again")


def input_date():
    while True:
        date = input(
            """
            Enter date in format: 01.11.2016 (remember about comma):
            """
        )
        try:
            return dateutil.parser.parse(date)
        except ValueError:
            print("You've entered wrong value. Try again")
