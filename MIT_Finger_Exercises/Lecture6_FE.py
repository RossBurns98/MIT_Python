#Assume you are given an integer 0 \<= N \\<= 1000. Write a piece of Python code that uses bisection search to guess N. 
#The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N.
#Hints: If the halfway value is exactly in between two integers, choose the smaller one.

N = int(input("Pick a number from 0 to 1000: "))
high = 1000
low = 0
guess = (high + low)//2
num_guesses = 0

while guess != N:
    if guess > N:
        high = guess
    else:
        low = guess
    guess = (high + low)//2
    num_guesses += 1
print(f"Count: {num_guesses}")
print(f"Answer: {guess}")