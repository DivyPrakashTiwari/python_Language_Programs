# Take input from the user for two numbers
a=int(input("enter the number 1"))
b=int(input("enter the number 2"))

# Swap the values of a and b using a temporary variable c
c=a
a=b
b=c

# Print the result of swapping with a third variable
print("swaping with third variable")
print("after swapingv number 1 value is ", a)
print("after swapingv number 2 value is ",b)

# Swap the values of a and b without using a temporary variable
a,b=b,a

# Print the result of swapping without a third variable
print("swaping without third variable")
print("after swapingv number 1 value is ", a)
print("after swapingv number 2 value is ",b)