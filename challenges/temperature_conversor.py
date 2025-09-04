"""
Developing a temperature conversor that converts between Celsius and Fahrenheit.
The program should take a temperature value and its unit (Celsius or Fahrenheit) as input
and return the converted temperature.

"""
# Converting celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
# Converting fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Main function to convert temperature based on unit
def convert_temperature(temperature, unit):
    if unit == 'C':
        return celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        return fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Unit must be 'C' for Celsius or 'F' for Fahrenheit")

# Using and testing the funcitons
temperature_c = 25
temperature_f = 77

converted_f = convert_temperature(temperature_c, 'C')
converted_c = convert_temperature(temperature_f, 'F')

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")
