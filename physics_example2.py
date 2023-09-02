
## EXAMPLE ##
from python_units import v
import python_units as pu

# 1) What are their average page?
# Method 1: Making two difference Value instances:
# 96 km in 8 hours

distance = v("96 km")
time = v("8 hours")
speed = distance / time
print(speed) # outputs: 3.33 m/s
print(speed.to("km/h")) # outputs: 12 km/t

# Method 2: Making it all happen in one Value instance
speed = v("96 km / 8 hours")
print(speed) # outputs: 3.33 m/s
print(speed.to("km/h")) # outputs: 12 km/t

# Method 3: Calculating value then making Value instance
speed_without_unit = 96 / 8
speed = v(f"{speed_without_unit} km/h")
print(speed) # outputs: 3.33 m/s
print(speed.to("km/h")) # outputs: 12 km/t
