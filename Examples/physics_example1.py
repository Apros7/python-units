import units_python as up
from units_python import v

## EXAMPLE ##

# How many soccer balls (diameter of 22 cm) can fit inside a 5 x 5 x 2.7 meter room?

##         ##

soccer_ball_diameter = v("22 cm")
soccer_ball_radius = soccer_ball_diameter / 2
soccer_ball_volume = 4/3 * up.pi * soccer_ball_radius ** 3
print(soccer_ball_volume.raw())               

        #prints: 0.005575279762570685 m**3

room_length = v("5 m")
room_width = v("5 m")
room_height = v("2.7 m")
room_volume = room_length * room_width * room_height
print(room_volume.raw())                      

        #prints: 67.5 m**3

number_of_soccer_balls_in_room = room_volume / soccer_ball_volume
print(number_of_soccer_balls_in_room.raw())   

        #prints: 12107.015768635918

# Answer 12107 soccer balls in one room