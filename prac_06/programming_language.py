class ProgrammingLanguage:

    def __init__(self, typing, reflecting, year):
        self.typing = typing
        self.reflecting = reflecting
        self.year = year

    def is_dynamic(self):
        if "Dynamic" in self:
            return True
        else:
            return False
