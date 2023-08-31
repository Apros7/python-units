import math
from python_units.constants import UNITS, SPECIAL_UNITS, PREFIXES

## Relevant constants ##
pi = math.pi

## Relevant functions ##
def sqrt(value): pass
def nsqrt(value): pass

## Value Class ##
class v():
    def __init__(self, value):
        self._get_value(value)
        self.value *= self.unit.get_prefix()


    def __str__(self): return str(self.value) + " " + self.unit.get()
    def __eq__(self, other): return str(self) == other
    def __add__(self, other): return v(str(self.value + other.value) + " " + self.unit.get_add(other))
    def __sub__(self, other): return v(str(self.value - other.value) + " " + self.unit.get_sub(other))
    # def __mul__(self, other): 

    def _get_value(self, value): 
        split = value.split()
        if len(split) != 2: raise Exception("The input should be 1 number and 1 unit: '5 m', 18.23 m/s, etc.")
        self.value, self.unit = float(split[0]), Unit(split[1])

## Unit Class ##
class Unit():
    def __init__(self, unit) -> None:
        self.unit = unit

    def check_compatibility(self, other): 
        if self.unit != other.unit.get(): raise Exception(f"Units are not compatible: {self.unit} : {other.unit.get()}")

    def get(self): return self.unit
    def get_add(self, other): self.check_compatibility(other); return self.unit
    def get_sub(self, other): self.check_compatibility(other); return self.unit

    def get_prefix(self):
        if self.unit[1:] in UNITS: self.prefix = PREFIXES[self.unit[0]]; self.unit = self.unit[1:]
        elif self.unit in SPECIAL_UNITS: self.prefix, self.unit = SPECIAL_UNITS
        else: self.prefix = 1
        return self.prefix