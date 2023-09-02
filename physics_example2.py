
## EXAMPLE ##
from python_units import v
import python_units as pu

# 1) What are their average page?
# Method 1: Making two difference values instances:
# 96 km in 8 hours

distance = v("96 km")
time = v("8 hours")
speed = distance / time
print(speed)
print(speed.to("km/h")) # outputs: 12 km/t

speed = v("12 km/h")
print(speed)
print(speed.to("km/h"))

# Method 2: Making it all happen in one value
# speed = v("96 km / 8 hours")
# print(speed)
# print(speed.to("km/t"))