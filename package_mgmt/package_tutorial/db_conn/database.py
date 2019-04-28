class Database:

    def __init__(self, name, load):
        self.name = name
        self.load = load

    def __str__(self):
        return 'It is it'


class Test:
    def __repr__(self):
        return "Test()"

    def __str__(self):
        return "member of Test"


