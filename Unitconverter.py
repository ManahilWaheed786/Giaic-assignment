
print("Welcome to the Unit Converter!")
print("Supported units: meter, kilometer, centimeter, inch, foot")
value = float(input("Enter the value to convert: "))
from_unit = input("Convert from: ")
to_unit = input("Convert to: ")
meter_rates = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "inch": 0.0254,
    "foot": 0.3048
}
value_in_meters = value * meter_rates[from_unit]
converted_value = value_in_meters / meter_rates[to_unit]
print(f"{value} {from_unit} = {converted_value} {to_unit}")