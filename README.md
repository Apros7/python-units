# UnitsPythonPackage
### Python package built with focus on simplicity, ease of use & readability.
Check out SPECIAL_UNITS in python_units/constants.py if you are missing some constants.

If your unit is missing, open a PR with your constant, the appropriate prefix and SI-unit added.
## Installation
Install with: 
```
pip install python_units
```
If you have already installed this package, but want the latest version use:
```
pip install python_units --upgrade
```
## How to use:

In this example, we have a physics problem to solve. 

We will solve it using units-python to keep track of our units:

### **Physics Example 1**:
How many soccer balls (diameter of 22 cm) can fit inside a 5 x 5 x 2.7 meter room?
[See the example code here](https://github.com/Apros7/python-units/blob/main/Examples/physics_example1.py)

### **Physics Example 2**:
A runner has been running 96 km in 8 hours. 
1) What are their average page?
2) If the runner continues at this pace, how far will they go in 46.2 minutes?
[See the example code here](https://github.com/Apros7/python-units/blob/main/Examples/physics_example2.py)

## Relevant methods:
- .copy(): returns copy of value
```
my_value = v("9 m**2")
my_copied_value = my_value.copy()
print(my_copied_value) # outputs "9 m**2"
```
- .round(digits): round value to number of digits (returns nothing)
```
my_value = v("3.1415926535 m")
my_value.round(4)
print(my_value) # outputs "3.1416 m"
```
- .sqrt(n=1): takes n-squareroot of value (returns changed value)
```
my_value = v("9 m**2")
my_value_sqrt = my_value.sqrt(2)
print(my_value_sqrt) # outputs "3 m"
```
- .value: returns the value of the object (float)
- .unit.get(): returns the unit (string)
- .to(str): input string with desired unit: "km/h", "tons", "hours". Returns string with value and unit

## Custom functions:
We supply certain relevant functions:
- sqrt(value, n=1): take n-squareroot of value
```
import python_units as pu
from python_units import v

my_value = v("9 m^2")
my_value_sqrt = pu.sqrt(my_value)
print(my_value_sqrt) # outputs "3 m"
```
- nsqrt(value, n): take n-squareroot of value
```
other_value = v("21 m^3")
my_value_3sqrt = pu.nsqrt(my_value, 3)
print(my_value_sqrt) # outputs "3 m"
```
- round(value, digits): round value number
```
third_value = v("3.1415926535 m")
third_value_rounded = pu.round(third_value, 4)
print(third_value_rounded) # outputs "3.1416 m"
```
## What units can I use?
You can find all avaliable units in **python_units.constant.UNITS** & **python_units.constant.SPECIAL_UNITS**.

You can find all avaliable prefixes in **python_units.constant.PREFIXES**.

You can combine prefixes and units in whatever way you like. You can also combine multiple units: 'ton/liter', 'kg*liter/hour' etc.

## What you, at this time, cannot do:
- exp
- value ** value (value ** constant works!)
