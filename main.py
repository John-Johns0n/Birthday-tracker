import initPeople
import datetime as d


def main():
    # Get people data sorted by birth date (within the year, starting from current date)
    people = initPeople.sort_birthdays_with_current_date(initPeople.sort_birthdays(initPeople.get_people_data()))

    # Get today's date to make comparisons
    today = d.date.today()
    # This can be set to anything you like, it doesn't have to be three weeks. Used to display upcoming birthdays
    today_plus_3weeks = today + d.timedelta(days=21)

    birthdays_today = []
    upcoming_birthdays = []

    # Take people who were born today and put them in a separate list
    while people[0].birthdate.month == today.month and people[0].birthdate.day == today.day:
        birthdays_today.append(people.pop(0))

    # Take people who were born on dates between tomorrow and x later (default 3 weeks) and put them in a separate list
    while initPeople.is_first_date_later(today_plus_3weeks, people[0].birthdate):
        upcoming_birthdays.append(people.pop(0))

    # Print today's date
    print(f"\nToday is {today.strftime('%B %d, %Y')}")

    # Print names and age of people born today
    if len(birthdays_today) > 0:
        print("\nBirthdays today:")
        for person in birthdays_today:
            print(f"{person.name}, turning {person.age}")
    else:
        print("No birthdays today.")

    # Print names and age of people born in dates between tomorrow and x later (default 3 weeks)
    if len(upcoming_birthdays) > 0:
        print("\nBirthdays coming up soon:")
        for person in upcoming_birthdays:
            print(f"{person.name}, turning {person.age + 1} on {person.birthdate.strftime('%B %d')}")
    else:
        print("No soon upcoming birthdays.")


main()
