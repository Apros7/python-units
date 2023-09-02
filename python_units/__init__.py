import math
import builtins
from python_units.functions import fraction_decoder

from python_units.constants import UNITS, SPECIAL_UNITS, PREFIXES

## Relevant constants ##
pi = math.pi

## Relevant functions ##
def sqrt(value, n=1): copy = value.copy(); copy.sqrt(n); return copy
def nsqrt(value, n): copy = value.copy(); copy.sqrt(n); return copy
def round(value, digits): copy = value.copy(); copy.round(digits); return copy

## Value Class ##
class v():
    def __init__(self, value):
        self.nominators, self.denominators = fraction_decoder(value)
        self._get_value(value)

    def copy(self): return v(self.__str__())
    def round(self, digits): self.value = builtins.round(self.value, digits)
    def sqrt(self, n=1): return self.__pow__(1/n)
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
        if len(self.nominators) and not self.denominators: self._get_single_value(value)
        else: self._get_value_fraction(value)
    
    def _get_value_fraction(self, value):
        self.value = 1
        nom_unit = Unit("")
        for nominator in self.nominators:
            if len(nominator.split()) == 1: 
                nom_unit = self.handle_len_1_value(nominator, "mul", unit_obj = nom_unit)
            else: 
                value_obj = v(nominator)
                self.value *= value_obj.value
                nom_unit *= value_obj.unit

        denom_unit = Unit("")
        if self.denominators:
            for denominator in self.denominators:
                if len(denominator.split()) == 1: 
                    denom_unit = self.handle_len_1_value(denominator, "div", unit_obj = denom_unit)
                else: 
                    value_obj = v(denominator)
                    self.value /= value_obj.value
                    denom_unit *= value_obj.unit
        self.unit = nom_unit / denom_unit

    def handle_len_1_value(self, value, method, unit_obj):
        if self.is_hidden_float(value): 
            if method == "mul": self.value *= value
            else: self.value /= value
        else: 
            if value not in UNITS:
                value_obj = v(f"1 {value}")
                unit_obj *= value_obj.unit
                if method == "mul": self.value *= value_obj.value
                else: self.value /= value_obj.value
            else:
                unit_obj *= Unit(value)
        return unit_obj

    def is_hidden_float(self, value):
        try: float(value); return True
        except: return False

    def _get_single_value(self, value):
        split = value.split()
        if len(split) != 2: raise Exception(f"The input should be 1 number and 1 unit: '5 m', '18.23 m/s', etc.\nYou gave this input: {value}")
        self.value, self.unit = float(split[0]), Unit(split[1])
        self.value *= self.unit.get_prefix()

    def to(self, desired_unit):
        desired_unit_obj = v(f"1 {desired_unit}")
        if self.unit.get() != desired_unit_obj.unit.get(): raise Exception(f"{self.unit.get()} does not match with desired unit: {desired_unit} with the SI-unit: {desired_unit_obj.unit.get()}")
        return f"{(self.value / desired_unit_obj.value)} {desired_unit}"

## Unit Class ##
class Unit():
    def __init__(self, unit) -> None:
        self.unit = unit
        self.set_power() ## does not work properly

    def _check_compatibility(self, other): 
        if self.unit != other.unit.get(): raise Exception(f"Units are not compatible: {self.unit} : {other.unit.get()}")

    def add_power(self, power=None): 
        if not power: power = self.power
        if power == 0: return ""
        return self.unit + "**" + str(power) if power != 1 else self.unit

    def __mul__(self, other): 
        if not isinstance(other, Unit): raise Exception(f"Other must be Unit: is {type(other)}")
        if self.unit == other.unit: 
            power = self.power + other.power
            return Unit(self.unit + "**" + str(power))
        elif len(self.unit) == 0: return Unit(other.add_power())
        return Unit(self.add_power() + "*" + other.add_power())

    def __truediv__(self, other): 
        if not isinstance(other, Unit): raise Exception(f"Other must be Unit: is {type(other)}")
        if self.unit == other.unit: 
            power = self.power - other.power
            return Unit(self.unit + "**" + str(power))
        elif len(self.unit) == 0: return other
        return Unit(self.add_power() + "/" + other.add_power())

    def get(self): return self.add_power()
    def get_add(self, other): self._check_compatibility(other); return self.add_power()
    def get_sub(self, other): self._check_compatibility(other); return self.add_power()
    def get_pow(self, other): power = other if self.power == 1 else self.power * other; return self.add_power(power)

    def get_mul(self, other):
        if self.unit == other.unit.unit: 
            power = self.power + other.unit.power
            return self.unit + "**" + str(power)
        elif len(self.unit) == 0: return other.unit.get()
        return self.add_power() + "*" + other.unit.add_power()

    def get_div(self, other):
        if self.unit == other.unit.unit: 
            power = self.power - other.unit.power
            return self.unit + "**" + str(power)
        elif len(self.unit) == 0: return other.unit.get()
        return self.add_power() + "/" + other.unit.add_power()

    def set_power(self):
        self.unit = self.unit.replace("**", "^")
        if "^" in self.unit: self.unit, self.power = self.unit.split("^")
        else: self.power = 1
        self.power = float(self.power)

    def get_prefix(self):
        if self.unit[1:] in UNITS: self.prefix = PREFIXES[self.unit[0]]; self.unit = self.unit[1:]
        elif self.unit in SPECIAL_UNITS: self.prefix, self.unit = SPECIAL_UNITS[self.unit]
        else: self.prefix = 1
        return self.prefix