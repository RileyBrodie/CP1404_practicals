class ProgrammingLanguage:

    def __init__(self, name, typing, reflecting, year):
        self.name = name
        self.typing = typing
        self.reflecting = reflecting
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}" \
            .format(self.name, self.typing, self.reflecting, self.year)

    def is_dynamic(self):
        if "Dynamic" in self.typing:
            return True
        else:
            return False
