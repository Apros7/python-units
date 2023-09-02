## EXAMPLE ##
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