# UnitsPythonPackage
## Installation
Install with: 
```
pip install units-python
```

## How to use:

In this example, we have a physics problem to solve. 

We will solve it using units-python to keep track of our units:

**Physics Example 1**:
How many soccer balls (diameter of 22 cm) can fit inside a 5 x 5 x 2.7 meter room?

```
from python_units import v
import python_units as pu

soccer_ball_diameter = v("22 cm")
soccer_ball_radius = soccer_ball_diameter / 2
soccer_ball_volume = 4/3 * pu.pi * soccer_ball_radius ** 3
print(soccer_ball_volume)               

        #prints: 0.005575279762570685 m**3

room_length = v("5 m")
room_width = v("5 m")
room_height = v("2.7 m")
room_volume = room_length * room_width * room_height
print(room_volume)                      

        #prints: 67.5 m**3

number_of_soccer_balls_in_room = room_volume / soccer_ball_volume
print(number_of_soccer_balls_in_room)   

        #prints: 12107.015768635918

# Answer 12107 soccer balls in one room
```

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


## What you, at this time, cannot do:
- exp
- value ** value (value ** constant works!)
