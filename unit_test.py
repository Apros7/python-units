from python_units import v

value1 = v("5 km")
value2 = v("519 m")

unit_test = [
    value1 + value2 == "5519.0 m",
    value1 - value2 == "4481.0 m",
    # value1 * value2 == f"{5000 * 519} m**2"
]
print(value1)
print(value2)
print(value1 + value2)
print(unit_test)