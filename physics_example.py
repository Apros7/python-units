from units import v, help

value = v("8 km")
value2 = v("2 m")
new_value = value + value2

print(new_value())

value = v("8 km")
value2 = v("403 m")
new_value = (value * 7) + value2
print(new_value())

## EXAMPLE ##
from units import v
import units as up

soccer_ball_diameter = v("22 cm")
soccer_ball_radius = soccer_ball_diameter / 2
soccer_ball_volume = 4/3 * up.pi * soccer_ball_radius ** 3
print(soccer_ball_volume())

room_length = v("5 m")
room_width = v("5 m")
room_height = v("5 m")
room_volume = room_length * room_width * room_height
print(room_volume)

number_of_soccer_balls_in_room = room_volume / soccer_ball_volume
print(number_of_soccer_balls_in_room())