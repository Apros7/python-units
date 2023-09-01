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
print(soccer_ball_volume)               #prints: 0.005575279762570685 m**3

room_length = v("5 m")
room_width = v("5 m")
room_height = v("2.7 m")
room_volume = room_length * room_width * room_height
print(room_volume)                      #prints: 67.5 m**3

number_of_soccer_balls_in_room = room_volume / soccer_ball_volume
print(number_of_soccer_balls_in_room)   #prints: 12107.015768635918

# Answer 12107 soccer balls in one room
```

## Custom functions:
If you want to use either of those, import them from units-python:
```
from units-python import v
import units-python as up

my_value = v("9 m^2")
other_value = v("21 m^3")

my_value_sqrt = up.sqrt(my_value)
print(my_value_sqrt) # outputs "3 m"

my_value_3sqrt = up.nsqrt(my_value, 3)
print(my_value_sqrt) # outputs "3 m"
```


## What you, at this time, cannot do:
- sqrt
- exp
- value ** value (value ** constant works!)
