#Lecture Code Example
# where = input("You are in the lost forest. Go left or Right? ")
# while where == "right":
#     where = input("Ahh you are still lost! Keep going right? or go left this time?")
# print("Nice you made it out of the Lost forest.")

# n = abs(int(input("Enter a number:")))
# while n > 0:
#     print("x")
#     n = n - 1


#Infinte Loop
# while True:
#     print("nooooooo")


#Lecture exercise
# where = input("Go left, right, up or down? ")
# count = 0
# while where != "left":
    # where = input("Go left, right, up or down? ")
    # count = count + 1
    # if count > 2:
        # print(":(")
# print("You got out \o/")


#Example code showing loop pattern, this finds the factorial of x.
# x = 4
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f"{x} factorial is {factorial}.")


#Using a for loop to iterate over a set of values.
# for n in range(5):
#     print(n)

#Playing around with range()
# for i in range(1,4,1):
#     print(i) 

# for j in range(1,4,2):
    # print(j*2)

# for me in range(4,0,-1):
#     print("$"*me)

#Prints running sum
# mysum = 0 
# for i in range(10):
#     mysum += i
# print(mysum)

#Lecture Exercise
#Fix code, should use start and end in the range to get total sum between 
#and including those values.
#ie for start = 3 and end = 5, sum should be 12.

# mysum = 0
# start = 3
# end = 5
# for i in range(start,end+1):
#     mysum += i
# print(mysum)
#All I changed was adding a +1 after the end in range statement.