class Unit(object):
    def __init__(self):
        self.value = None
        self.suffix = None

    def __str__(self):
        return "{0}{1}".format(self.value, self.suffix)


class Temperature(Unit):
    def to_kelvin(self):
        pass

    def to_celcius(self):
        return self.to_kelvin().to_celcius()


class Kelvin(Temperature):
    def __init__(self, value):
        self.suffix = "K"
        self.value = value

    def to_celcius(self):
        return Celcius(self.value - 273.15)

    def to_kelvin(self):
        return self


class Celcius(Temperature):
    def __init__(self, value):
        self.suffix = "C"
        self.value = value

    def to_kelvin(self):
        return Kelvin(self.value + 273.15)

