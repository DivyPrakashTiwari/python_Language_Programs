# Get the score from the user
score = int(input("Enter the score: "))

# Define the grade ranges
A_RANGE = range(90, 101)
B_RANGE = range(80, 90)
C_RANGE = range(70, 80)
D_RANGE = range(60, 70)

# Determine the grade based on the score
if score in A_RANGE:
    grade = 'A'
elif score in B_RANGE:
    grade = 'B'
elif score in C_RANGE:
    grade = 'C'
elif score in D_RANGE:
    grade = 'D'
else:
    grade = 'F'

# Print out the grade
print("The grade is: ", grade)