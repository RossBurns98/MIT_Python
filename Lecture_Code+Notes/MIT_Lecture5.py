#Binary converter
# num = int(input("Pick a number to convert to binary: "))

# if num < 0:
#     is_neg = True
#     num = abs(num)
# else:
#     is_neg = False
# result = ""
# if num == 0:
#     result = "0"
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# if is_neg:
#     result = "-" + result
# print(result)

# x = 0.625

# p = 0
# while ((2**p)*x)%1 != 0:
#     print("Remainder = " + str((2**p)*x - int((2**p)*x)))
#     p += 1

# num = int(x*(2**p))
# result = ""
# if num == 0:
#     result = "0"
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# for i in range(p - len(result)):
#     result = "0" + result
# result = result[0:-p] + "." + result[-p:]
# print("The Binary representation of the decimal " + str(x) + " is " +str(result))

#Implementation of Guess algorithm

# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001

# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1

# print("num_guesses =", num_guesses)
# print(guess, "is close to square root of", x)

#Doesn't work when using x = 54321, and higher numbers, so made a debugging print statement to check.
#x = 54321
#epsilon = 0.01
#num_guesses = 0
#guess = 0.0
#increment = 0.0001
#
#while abs(guess**2 - x) >= epsilon:
#    guess += increment
#    num_guesses += 1
#    if num_guesses%100000 == 0:
#        print("current guess =", guess)
#        print("Current guess**2 - x =", abs(guess*guess - x))
#
#print("num_guesses =", num_guesses)
#print(guess, "is close to square root of", x)

x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
print(f"num_guesses = {num_guesses}")
if abs(guess**2 - x) >= epsilon:
    print(f"Failed on square root of {x}")
    print(f"Last guess was {guess}")
    print(f"Last guess squared was {guess*guess}")
else:
    print(f"{guess} is around the square root of {x}")