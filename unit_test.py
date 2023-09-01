from python_units import v

value1 = v("5 km")
value2 = v("519 m")
factor = value1 / value2

unit_test = [
    value1 + value2 == "5519.0 m",
    value1 - value2 == "4481.0 m",
    value1 * value2 == f"{float(5000 * 519)} m**2",
    value1 * 2 == f"{float(5000 * 2)} m",
    value1 * factor == f"{5000 * 9.633911368015415} m"
]

print(unit_test)