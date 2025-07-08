#Assume you are given a string variable named my_str. 
#Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. 
#For example, if my_str = "abcdefg" then your code should print out aceg.

#Bit more verbose than the actual solution given to us but this was what popped into my head.
my_str = "abcdefg"
s = ""
for i in range(len(my_str)):
    if i%2 == 0:
        s += my_str[i]
print(s)

#Actual solution
s = ''
for i in range(0,len(my_str),2):
 s += my_str[i]
print(s)

#Would say mine is probably more dumbed down and readable atleast, 
#although theirs is more concise and quicker since it only uses even numbers to begin with.