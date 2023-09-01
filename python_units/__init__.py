import math
from python_units.constants import UNITS, SPECIAL_UNITS, PREFIXES

## Relevant constants ##
pi = math.pi

## Relevant functions ##
def sqrt(value, n=1): pass
def nsqrt(value, n): pass
def round(value): pass

## Value Class ##
class v():
    def __init__(self, value):
        self._get_value(value)
        self.value *= self.unit.get_prefix()

    def __str__(self): return str(self.value) + " " + self.unit.get()
    def __eq__(self, other): return str(self) == other
    def __add__(self, other): return v(str(self.value + other.value) + " " + self.unit.get_add(other))
    def __sub__(self, other): return v(str(self.value - other.value) + " " + self.unit.get_sub(other))
    def __rtruediv__(self, other): return self.__truediv__(other)
    def __rmul__(self, other): return self.__mul__(other)
    def __pow__(self, other): return v(str(self.value ** other) + " " + self.unit.get_pow(other))

    def __truediv__(self, other): 
        if isinstance(other, (int, float)): return v(str(self.value / other) + " " + self.unit.get())
        value = self.value / other.value
        unit = self.unit.get_div(other)
        return v(str(value) + " " + unit)

    def __mul__(self, other): 
        if isinstance(other, (int, float)): return v(str(self.value * other) + " " + self.unit.get())
        value = self.value * other.value
        unit = self.unit.get_mul(other)
        return v(str(value) + " " + unit)

    def _get_value(self, value): 
        split = value.split()
        if len(split) != 2: raise Exception(f"The input should be 1 number and 1 unit: '5 m', '18.23 m/s', etc.\n{value}")
        self.value, self.unit = float(split[0]), Unit(split[1])

## Unit Class ##
class Unit():
    def __init__(self, unit) -> None:
        self.unit = unit
        self.set_power()

    def check_compatibility(self, other): 
        if self.unit != other.unit.get(): raise Exception(f"Units are not compatible: {self.unit} : {other.unit.get()}")

    def add_power(self, power=None): 
        if not power: power = self.power
        if power == 0: return ""
        return self.unit + "**" + str(power) if power != 1 else self.unit

    def get(self): return self.add_power()
    def get_add(self, other): self.check_compatibility(other); return self.add_power()
    def get_sub(self, other): self.check_compatibility(other); return self.add_power()
    def get_pow(self, other): power = other if self.power == 1 else self.power ** other; return self.add_power(power)

    def get_mul(self, other):
        if self.unit == other.unit.unit: 
            power = self.power + other.unit.power
            return self.unit + "**" + str(power)
        return self.add_power() + "*" + other.unit.add_power()

    def get_div(self, other):
        if self.unit == other.unit.unit: 
            power = self.power - other.unit.power
            return self.unit + "**" + str(power)
        return self.add_power() + "/" + other.unit.add_power()

    def set_power(self):
        self.unit = self.unit.replace("**", "^")
        if "^" in self.unit: self.unit, self.power = self.unit.split("^")
        else: self.power = 1
        self.power = int(self.power)

    def get_prefix(self):
        if self.unit[1:] in UNITS: self.prefix = PREFIXES[self.unit[0]]; self.unit = self.unit[1:]
        elif self.unit in SPECIAL_UNITS: self.prefix, self.unit = SPECIAL_UNITS
        else: self.prefix = 1
        return self.prefix