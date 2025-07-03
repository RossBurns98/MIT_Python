#Iteration

__CONTROL FLOW: while LOOPS__

*Example:*

while <condition>:
    <code>
    <code>
    . . .

- <condition>, evaluates to True or False (Boolean).
- If condition is *True*, execute all steps inside code block.
- Check <condition> again
- *Repeat* until <condition> is *False*.
- If it is never *False*, the program will continuously loop forever...
- If they start running indefinitely, ctrl + c halts the program.

**Common Flow Tip**

- if for example, I am iterating through a set of numbers in a sequence using a *while* loop, to ensure that the loop doesn't run indefinetly, I need to make sure to alter the variable within the loop itself, example:

#This code would run forever just printing 0.
n = 0
while n < 5:
    print(n)

#Better code, ensure n increases towards meeting the condition.
n = 0
while n < 5:
    print(n)
    n = n + 1

This is apparently quite a common pattern; another example would be this code for 4 factorial:

x = 4
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
print(f"{x} factorial is {factorial}.")

**Note: += and *= here mean: i += 1 <=> i = i + 1, factorial *= i <=> factorial = factorial * i**

**Structure of for Loops**

Example structure:

for <variable> in <sequence_of_values>:
    <code>

- Each time iterating through the loop, variable takes a new value.
- ie first time through <variable> takes the first value, second time through <variable> takes the second value, this continues until values run out.

*Example:*

for <variable> in range (<some_num>):
    <code>
    <code>

for n in range(5):
    print(n)

- so for this example, first time through variable takes on 0, second time 1, third time 2.
- This continues upto but not including 5, so the last shown value would be 4.

*Note on range()*
- Range can either be written like: range(x), range(x,y) or range(x,y,z).
- range(x) starts iterating at 0 up to x-1 in a step size 1.
- range(x,y) goes from x to y-1 in a step size of 1.
- range(x,y,z) goes from x to y-1 in step sizes of z.


**SUMMARY**
- while Loops
    - Loop as long as a condition is true.
    -Need to ensure that an infinite loop isn't entered.

- for Loops
    - Can loop over *ranges* of numbers.
    - Can loop over *elements* of a string.