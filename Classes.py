class Aircraft:
        def __init__(self,registration):
            self._registration = registration
        def registration(self):
            return self._registration
        def num_seats(self):
            rows,row_seats = self.seating_plan()
            return len(rows) * len(row_seats)

class AirbusA319(Aircraft):

    def model(self):
        return "AirbusA319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"

class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1,56),"XYZPQR"


dubai =Boeing777('12')
print(dubai)
print(dubai.model())
print(dubai.seating_plan())
print(dubai.num_seats())

delhi = Aircraft('10')
print(delhi)
print(delhi.num_seats())
