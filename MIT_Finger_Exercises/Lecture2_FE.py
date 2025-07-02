# Assume you are given a variable named number (has a numerical value). 
# Write a piece of Python code that prints out one of the following strings: 

# positive if the variable number is positive,
# negative if the variable number is negative,
# zero if the variable number is equal to zero.

number = int(input("Choose any number, I'll even take negative ones: "))
if number > 0:
    print("Positive.")
elif number == 0:
    print("Zero.")
else:
    print("Negative.")