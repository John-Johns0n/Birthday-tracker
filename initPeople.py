from person import Person
import datetime as d
import csv


def get_people_data():
    """Get people data from csv"""

    people = []
    csv_path = "people.csv"

    with open(csv_path, newline='', encoding="UTF-8") as people_csv:
        reader = csv.DictReader(people_csv, delimiter=',', quotechar='"')
        for row in reader:
            people.append(
                Person(
                    name=row['name'],
                    birthdate=d.date(
                        int(row['b_year']),
                        int(row['b_month']),
                        int(row['b_day'])
                    )
                )
            )

    return people


def is_first_date_later(date1, date2):
    """Returns True if the first date is later in the year than the second, False if not"""
    return date1.month > date2.month or (date1.month == date2.month and date1.day > date2.day)


def sort_birthdays(people):
    """Sort people by birthdate within the year"""

    people.sort()
    return people


def sort_birthdays_with_current_date(people):
    """
    Go through the (now sorted by birthdate) list of people, iterate through them,
    and if their birthdate is earlier in the year than the current date,
    put them at the end of the list
    """
    today = d.date.today()

    # If the latest birthday in the list is earlier in the year than today's date, the while loop can go on forever.
    # Thus, we have to check for it first.
    if is_first_date_later(people[-1].birthdate, today):
        while is_first_date_later(today, people[0].birthdate):
            people.append(people.pop(0))

    return people


def get_people_data_sorted():
    """Returns sorted people data for usage in main."""
    return sort_birthdays_with_current_date(sort_birthdays(get_people_data()))
