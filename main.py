from utils import square, is_even, celsius_to_fahrenheit

# Prompt the user for an input number
user_input_str = input("Enter a number: ")
user_input = float(user_input_str)

# Calculate values using the imported functions
sq = square(user_input)
even_status = "even" if is_even(user_input) else "odd"
fahr = celsius_to_fahrenheit(user_input)

# Print results
print(f"Square: {sq}")
print(f"Number is: {even_status}")
print(f"Fahrenheit equivalent: {fahr}")
