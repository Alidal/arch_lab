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
6. Exit.\n
Enter value:""")

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
