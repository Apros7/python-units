import python_units as pu
from python_units import v

my_value = v("9 m^2")
my_copied_value = my_value.copy()
print(my_copied_value)

my_value = v("9 m**2")
my_value_sqrt = my_value.sqrt(2)
print(my_value_sqrt) # outputs "3 m"

other_value = v("21 m^3")
my_value_3sqrt = pu.nsqrt(my_value, 3)
print(my_value_sqrt) # outputs "3 m"

third_value = v("3.1415926535 m")
third_value_rounded = pu.round(third_value, 4)
print(third_value_rounded) # outputs "3.1416 m"