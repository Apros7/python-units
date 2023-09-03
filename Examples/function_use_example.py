import units_python as up
from units_python import v

my_value = v("9 m^2")
my_copied_value = my_value.copy()
print(my_copied_value)

my_value = v("9 m**2")
my_value_sqrt = up.sqrt(my_value)
print(my_value_sqrt) # outputs "3 m"

other_value = v("21 m^3")
my_value_3sqrt = up.nsqrt(my_value, 3)
print(my_value_sqrt) # outputs "3 m"

third_value = v("3.1415926535 m")
third_value_rounded = up.round(third_value, 4)
print(third_value_rounded) # outputs "3.1416 m"