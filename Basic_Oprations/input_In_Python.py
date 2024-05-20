# This script calculates the area of a triangle using Heron's formula

# Request user input for the height of the triangle
h = int(input("Enter the height of the triangle: "))

# Request user input for the base of the triangle
b = int(input("Enter the base of the triangle: "))

# Calculate the area of the triangle using the formula 0.5 * height * base
ar = 0.5 * h * b

# Print the result
print("The area of the triangle is", ar)