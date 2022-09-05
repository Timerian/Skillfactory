class Square:
    _a = None

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value

    @property
    def area(self):
        return self.a**2


sq = Square
sq.a = 10
print(sq.area)
