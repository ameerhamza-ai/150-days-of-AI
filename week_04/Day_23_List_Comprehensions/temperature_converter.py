celsius = [0, 10, 20, 30, 40, 100]

# Convert Celsius to Fahrenheit and format the output strings
fahrenheit_strings = [f"{c}°C = {(c * 9/5) + 32}°F" for c in celsius]

# Print each converted value
for result in fahrenheit_strings:
    print(result)
