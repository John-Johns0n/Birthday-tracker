import datetime as d


class Person:
    """
    The basic person object.
    This is mostly here to make my job easier.
    """

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        self.age = self.get_age()
        self.next_bday = self.get_next_birthday()
        self.days_until_next_bday = self.get_days_until_next_birthday()

    def get_age(self):
        """Returns the person's age."""
        today = d.date.today()
        return today.year - self.birthdate.year - (
                    (today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    def get_next_birthday(self):
        """Returns the date for the person's next birthday."""
        today = d.date.today()
        bday_this_year = d.date(year=today.year, month=self.birthdate.month, day=self.birthdate.day)
        bday_next_year = d.date(year=today.year + 1, month=self.birthdate.month, day=self.birthdate.day)

        if bday_this_year >= today:
            return bday_this_year
        elif bday_next_year >= today:
            return bday_next_year

    def get_days_until_next_birthday(self):
        """Returns the number of days until the person's next birthday. If it is their birthday, return 0."""
        today = d.date.today()
        return (self.next_bday - today).days

    def __gt__(self, other):
        # Create new dates with bogus year to use for comparisons, so dates can be compared independently of the year
        self_date = d.date(1000, self.birthdate.month, self.birthdate.day)
        other_date = d.date(1000, other.birthdate.month, other.birthdate.day)

        return self_date > other_date

    def __lt__(self, other):
        # Create new dates with bogus year to use for comparisons, so dates can be compared independently of the year
        self_date = d.date(1000, self.birthdate.month, self.birthdate.day)
        other_date = d.date(1000, other.birthdate.month, other.birthdate.day)

        return self_date < other_date
