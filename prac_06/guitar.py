class Guitar:

    def __init__(self, name, year, cost):
        self.name = ""
        self.year = 0
        self.cost = 0

    def __str__(self):
        return "{} {} : {}".format(self.name, self.year, self.cost)

    def get_age(self, current_year,):
        age = current_year - self.year
        return age

    def is_vintage(self):
        if age >= 50:
            return True
        else:
            return False

