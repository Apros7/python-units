## EXAMPLE ##
from python_units import v
import python_units as pu

soccer_ball_diameter = v("22 cm")
soccer_ball_radius = soccer_ball_diameter / 2
soccer_ball_volume = 4/3 * pu.pi * soccer_ball_radius ** 3
print(soccer_ball_volume)

room_length = v("5 m")
room_width = v("5 m")
room_height = v("2.7 m")
room_volume = room_length * room_width * room_height
print(room_volume)

number_of_soccer_balls_in_room = room_volume / soccer_ball_volume
print(number_of_soccer_balls_in_room)