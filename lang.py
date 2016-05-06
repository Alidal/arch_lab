"""
Module that provides multilanguage support.
Contains dictionary with languages as keys, and dictionary
with all responses, written in this language.
You can change language in config.ini.
"""

lang = {
    "eng": {
        "main_menu_cli_choice": """
Choose one of menu items:
1. Add today value.
2. Update existing record.
3. Delete record.
4. Show statistic for last week.
5. Show statistic for last month.
6. Show all records in table.
7. Exit.\n
Enter value: """,

        "pressure_choice": """
Enter values in format: systolic pressure, diastolic pressure
(remember about comma): """,

        "date_choice": "Enter date in format: 01.11.2016:",
        "empty_table": "Table is empty",
        "ps_for_week": "\nPressure statistic for last week:",
        "ps_for_month": "\nPressure statistic for last month:",
        "ps_all": "\nPressure statistic for all time:",
        "choose_valid_option": "Choose valid option",
    }
}
