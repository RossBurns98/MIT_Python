#Using bisection method to find square root approximation

# x = 54321
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high+low)/2.0

# while abs(guess**2 - x) >= epsilon:
#     if guess**2 < x:
#         low = guess        
#     else:
#         high = guess
#     guess = (high+low)/2.0
#     num_guesses += 1
# print(f"num_guesses = {num_guesses}")
# print(f"{guess} is close to square root of {x}.")

#Using new method to get the edge cases (0<x<1) sorted out

# x = 0.5
# epsilon = 0.01
# low = x
# high = 1
# guess = (high+low)/2.0

# while abs(guess**2 - x) >= epsilon:
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f"{guess} is close to square root of {x}")

#More Robust Code for all cases
# x = float(input("Pick a positive number: "))
# epsilon = 0.01
# if x >= 1:
#     low = 1
#     high = x
# else:
#     low = x
#     high = 1
# num_guesses = 0

# guess = (high + low)/2.0

# while abs(guess**2 - x) >= epsilon:
#     print(f" num_guesses: {num_guesses}, high: {high}, low: {low} ")
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1
# print(f"{guess} is close to square root of {x}.")
# print(f"num_guesses = {num_guesses}")

#Lecture Exercise
#Find cube root for some positve cubic using bisection method

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0

# while abs(guess**3 - cube) > epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f"The cube root of {cube} is {guess}")

#Code for Newton-Raphson

epsilon = 0.01
k = 54321
guess = k/2.0
num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print("num_guesses = " + str(num_guesses))
print("Square root of " + str(k) + " is about " + str(guess))
