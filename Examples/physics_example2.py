from units_python import v

## PHYSICS EXAMPLE 2 ##

# A runner has been running 96 km in 8 hours. 
# 1) What are their average page?
# 2) If the runner continues at this pace, how far will they go in 46.2 minutes?

##                   ##

# # 1) What are their average page?
# # Method 1: Making two difference Value instances:
# # 96 km in 8 hours

distance = v("96 km")
time = v("8 hours")
speed = distance / time
print(speed.raw())                # outputs: 3.33 m/s
print(speed.to("km/h"))     # outputs: 12 km/t

# # Method 2: Making it all happen in one Value instance
speed = v("96 km / 8 hours")
print(speed)                # outputs: 3.33 m/s
print(speed.to("km/h"))     # outputs: 12 km/t

# # Method 3: Calculating value then making Value instance
speed_without_unit = 96 / 8
speed = v(f"{speed_without_unit} km/h")
print(speed.raw())                # outputs: 3.33 m/s
print(speed.to("km/h"))     # outputs: 12 km/t

# 2) If the runner continues at this pace, how far will they go in 46.2 minutes?
speed = v("96 km / 8 hours")
minutes = v("46.2 min")
distance = speed * minutes
print(distance.raw())             # outputs: 9240.0 m
print(distance.to("km"))    # outputs: 9.24 km