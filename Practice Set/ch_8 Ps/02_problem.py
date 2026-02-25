# Write a python program using function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(fahrenheit):
    celsius = (fahrenheit -32) * (5/9)
    return celsius

fahrenheit = float(input("Enter the fahrenheit: "))
celsius = celsius_to_fahrenheit(fahrenheit)

print(celsius_to_fahrenheit(fahrenheit))
