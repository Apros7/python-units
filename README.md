# UnitsPythonPackage
### Python package built with focus on simplicity, ease of use & readability.
Check out SPECIAL_UNITS in python_units/constants.py if you are missing some constants.

If your unit is missing, open a PR with your constant, the appropriate prefix and SI-unit added.
## Installation
Install with: 
```
pip install units_python
```
If you have already installed this package, but want the latest version use:
```
pip install units_python --upgrade
```
## How to use:

In these examples, we have a physics problem to solve. 

We will solve it using python_units to keep track of our units:

### **Physics Example 1**:
How many soccer balls (diameter of 22 cm) can fit inside a 5 x 5 x 2.7 meter room?


[See the example code here](https://github.com/Apros7/python-units/blob/main/Examples/physics_example1.py)

### **Physics Example 2**:
A runner has been running 96 km in 8 hours. 
1) What are their average page?
2) If the runner continues at this pace, how far will they go in 46.2 minutes?


[See the example code here](https://github.com/Apros7/python-units/blob/main/Examples/physics_example2.py)

## Value Object parameters:
The v object parameters are:
- value: string of value and desired unit split by a space
- ten_exponent (optional): float of the ten_exponent i.e: 1.8 * 10 ** 8 m would be v("1.8 m", 8). 

## Relevant methods:
- .copy() -> Value Object: returns copy of value
- .round(digits) -> None: round value to number of digits (returns nothing)
- .sqrt(n=1) -> Value Object: takes n-squareroot of value (returns changed value)
- .raw_value() -> Float: returns the value of the object
- .unit.get() -> String: returns the unit
- .to(str) -> String: input string with desired unit: "km/h", "tons", "hours". Returns string with value and unit
- .change_unit(str) -> None: change unit of value to str e.g. if it was not done corectly
- .raw() -> Value Object: the string representation has ten exponents. This gives the value without any ten exponents.
- .abs() -> Value Object: returns new value object with the objects value being the absolute value


[See this for an example of how to use some of the functions]

## Custom functions:
We supply certain relevant functions:
- sqrt(value, n=1): take n-squareroot of value
```
import units_python as up
from units_python import v

my_value = v("9 m^2")
my_value_sqrt = up.sqrt(my_value)
print(my_value_sqrt) # outputs "3 m"
```
- nsqrt(value, n): take n-squareroot of value
```
other_value = v("21 m^3")
my_value_3sqrt = up.nsqrt(my_value, 3)
print(my_value_sqrt) # outputs "3 m"
```
- round(value, digits): round value number
```
third_value = v("3.1415926535 m")
third_value_rounded = up.round(third_value, 4)
print(third_value_rounded) # outputs "3.1416 m"
```
## What units can I use?
You can find all avaliable units in **python_units.constant.UNITS** & **python_units.constant.SPECIAL_UNITS**.

You can find all avaliable prefixes in **python_units.constant.PREFIXES**.

You can combine prefixes and units in whatever way you like. You can also combine multiple units: 'ton/liter', 'kg*liter/hour' etc.

## What you, at this time, cannot do:
- exp
- value ** value (value ** constant works!)
