# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
#         mysum += 1
#     print(mysum)

# even_nums = 0
# for i in range(10):
#     #i is 0,1,2,3,4.
#     if i%2 == 0: #% = Modulo, divides thing on left by thing on right and returns remainder.
#         even_nums += 1
# print(even_nums)

#Using strings and indexing, played around with it, quite wordy.
#iterates using idex variable.
#num_i = 0
# num_u = 0
# s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] == "i":
#         num_i += 1
#     elif s[index] == "u":
#         num_u += 1
# print(f"the number of i's is {num_i} and the number or u's is {num_u}.")
# print(f"the total number of i's and u's is {num_i + num_u}.")

#Simple version, iterates through s directly
# s = "demo loops - fruit loops"
# for char in s:
#     if char == "i" or char == "u":
#         print("There is an i or u.")


#Copied the lecturer's cheerleader code.
#an_letters = "aefhilmnorsxAEFHILMNORSX"
#word = input("I will cheer for you! Enter a word: ")
#times = int(input("Enthusiasm level (1-10): "))
#
#for x in word:
#    if x in an_letters:
#        print("Give me an " + x + ": " + x)
#    else:
#        print("Give me a " + x + ": " + x)
#print("What does that spell?")
#for i in range(times):
#    print(word,"!!!")

#Lecture Exercise
#Assume given a string of lowercase letters in variable "s".
#Count unique letters within the string and display amount.

# s = "abca"
# seen = ""
# for char in s:
#     if char not in seen:
#         seen += char
# print(len(seen))

# Code to find square root using Guess-and-Check
# guess = 0
# x = int(input("Enter an integer: "))
# while guess**2 < x:
#     guess += 1
# if guess**2 == x:
#     print(f"The square root of {x} is {guess}")
# else: 
#     print(f"{x} is not a perfect square")
    
# Implemented a variable to deal with negative numbers
# guess = 0
# neg_flag = False
# x = int(input("Enter an integer: "))
# if x < 0:
#     neg_flag = True
# while guess**2 < x:
#     guess += 1
# if guess**2 == x:
#     print(f"The square root of {x} is {guess}")
# else: 
#     print(f"{x} is not a perfect square")
#     if neg_flag:
#         print(f"checking did you mean {-x}?")

#Lecture Exercise
#hardcode a number, write a program to check through nums 1-10, and print if the number is found.
#for the same setup, print if the number is not found.

# secret = 8
# flag = False
# # for i in range(1,11):
# #     if i == secret:
# #         print(f"number was found from 1 - 10, it was {secret}")

# for i in range(1,11):
#     if i == secret:
#         flag = True
# if flag == True:
#     print(f"Found, it was {secret}")
# else:
#     print(f"Not found.")

#Guess-and-Check CUBE ROOT POSITIVE CUBES

# cube = int(input("Enter a positive number: "))

# for guess in range(cube + 1):
#     if guess**3 == cube:
#         print(f"Cube root of {cube} is {guess}.")

#Guess-and-Check CUBE ROOT POSITIVE and NEGATIVE CUBES

#cube = int(input("Enter a number: "))

#for guess in range(abs(cube) + 1):
#    if guess**3 == abs(cube):
#        if cube < 0:
#            guess = -guess
#        print(f"Cube root of {cube} is {guess}.")


#This form exits when the guess either meets or exceeds the cube, making it quicker/more efficient. 

# cube = int(input("Please guess a number: "))

# for guess in range(abs(cube) + 1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(f"{cube} is not a perfect cube.")
# else:
#     if cube < 0:
#         guess = -guess
#     print(f"The cube root of {cube} is {guess}.")

