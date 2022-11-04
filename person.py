import datetime as d


class Person:
    """
    The basic person object.
    This is mostly here to make my job easier.
    """

    def __init__(self, name, birthdate):
        today = d.date.today()

        self.name = name
        self.birthdate = birthdate
        self.age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
