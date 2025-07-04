#Assume you are given a positive integer variable named N. Write a piece of Python code that finds the cube root of N. 
#The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
#Hint: use a loop that increments a counter—you decide when the counter should stop.


#My solution
N = int(input("Choose a positive number: "))
for guess in range(N + 1):
    if guess**3 >= N:
        break
if guess**3 != N:
    print("error")
else:
    print(f"Cube root of {N} is {guess}")

#Given Solution
i = 1
while i**3 < N:
    i += 1
if i**3 == N:
    print(i)
else:
    print("error")