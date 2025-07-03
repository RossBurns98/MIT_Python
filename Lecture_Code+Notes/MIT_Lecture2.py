#what is the value of s1 and s2?
#b =  ":"
#c = ")"
#s1 = b + 2 * c
#print(s1)
#f = "a"
#g = " b"
#h = "3"
#s2 = (f + g) * int(h)
#print(s2)

#Checking slice using negative
# s = "abcdefgh"
# s1 = s[4:1:-2]
# print(s1)

a = "ABC d3f ghi"
a1 = a[3:len(a)-1]
print(a1)

#a2 = a[4:0:-1]
#print(a2)
#a3 = a[6:3]
#print(a3)

#Lecture Exercise
#Ask user for a verb, print "I can _ better than you" 
#where _ is the verb, and then print the verb 5 times

#verb = input("Please type any verb: ")
#print("I can"  ,verb,  "better than you!")
#print((verb + " ")*5)

#Newton's method for cube roots

#find g such that f(g,x) = g^3 - x = 0

# x = int(input("What x to find the cubed root from? "))
# g = int(input("Please guess the cubed root: "))
# print("Current estimate is =" ,g**3)

# next_g = g - (g**3 - x)/(3*g**2)
# print("Next Guess:"  ,next_g)

# num = 3000
# fraction = 1/3
# print(num*fraction, "is" ,fraction*100, "% of" ,num) #Old way of doing it, space inbetween number and & sign.

# print(num*fraction, "is" ,str(fraction*100) + "% of" ,num) # To fix had to cast percentage to a string to concatenate to % sign.

# print(f"{num*fraction} is {fraction*100}% of {num}") #Much simpler and probably more readable.

#Playing around with Boolean Stuff
# a = 3 > 2
# b = 4 > 3
# c = 5 > 6
# d = 6 > 7

# Seeing how different operators work with True and False Values
# print(a and b)
# print(a and c)
# print(c and d)
# print(a or b)
# print(a or c)
# print(c or d)
# print(a and not d)
# print(d or not c)

#Lecture Example
#Choose a secret number, ask user to guess number, print true or false based on answer.

# secret_num = 5
# guess = int(input("Guess a number: "))

# print(secret_num == guess)

#Lecture Exercise 
# Save a secret number, ask user to guess number, print whether number is too high, too low
# or equal to secret number.

# secret = 5
# guess = int(input("Guess a number: "))
# if secret > guess:
#     print("Too Low, Guess again")
# elif secret == guess:
#     print("Good Guess") 
# else:
#     print("Too High, Guess again")