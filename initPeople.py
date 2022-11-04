from person import Person
import datetime as d
import csv


def init():
    """Get people data from csv"""

    people = []

    with open('people.csv', newline='') as people_csv:
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


def quick_sort_birthdays(people):
    """Sort people by birth date within the year"""
    # This should really be an insertion sort.
    # If you're bored and want to change the implementation yourself, go ahead!

    length = len(people)
    if length <= 1:
        return people
    else:
        pivot = people.pop()

    items_greater = []
    items_lower = []

    for person in people:
        if is_first_date_later(person.birthdate, pivot.birthdate):
            items_greater.append(person)
        else:
            items_lower.append(person)

    return quick_sort_birthdays(items_lower) + [pivot] + quick_sort_birthdays(items_greater)


def sort_birthdays_with_current_date(people):
    """
    Go through the (now sorted by birth date) list of people, iterate through them,
    and if their birth date is earlier in the year than the current date,
    put them at the end of the list
    """
    today = d.date.today()

    while is_first_date_later(today, people[0].birthdate):
        people.append(people.pop(0))

    return people
