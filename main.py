import initPeople
import datetime as d


if __name__ == "__main__":
    # Get people data sorted by birth date (within the year, starting from current date)
    people = initPeople.get_people_data_sorted()

    # This can be set to anything you like, it doesn't have to be three weeks. Used to display upcoming birthdays
    days_to_check = 21

    birthdays_today = []
    upcoming_birthdays = []

    # Take people who were born today and put them in a separate list
    while people[0].days_until_next_bday == 0:
        birthdays_today.append(people.pop(0))

    # Take people born on dates between tomorrow and n days later (default 3 weeks) and put them in a separate list
    try:
        while people[0].days_until_next_bday <= days_to_check:
            upcoming_birthdays.append(people.pop(0))
    except IndexError:  # If all birthdays left in the list are upcoming in n <= [days_to_check] days
        pass

    # Print today's date
    print(f"\nToday is {d.date.today().strftime('%B %d, %Y')}")

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
