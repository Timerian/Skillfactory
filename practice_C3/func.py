pi = 3.1415


class Figure:
    def __init__(self, par=1):
        self._par = par

    @property
    def par(self):
        return self._par

    @par.setter
    def par(self, value):
        self._par = value

    @property
    def sq_area(self):
        return self._par ** 2

    @property
    def cir_area(self):
        return pi * self._par ** 2



