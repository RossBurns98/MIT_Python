#Strings
- *String(str)* =  sequence of case sensitive characters (Letters, special characters, spaces, digits)
- *str* are enclosed in *single quotes or quotation marks* (try stay consistent using them).
- *Concatenate(join)* and *repeat* strings : 
a = "me"
b = "myself"
c = a + b
*Output: c = "memyself"*
d = a + " " + b
*Output: d = "me myself"*
silly = a * 3
*Output: silly = "mememe"*

**String Operation**
- len(): function used to get length of a string within the parentheses.

s = "abc"
chars = len(s)
*char = 3.*

**Slicing for one character in a string**
- Recall in computing, counting starts from 0, not 1.
- Using *square brackets*, can "index" sting which allows us to get value at certain position/index (Example of position would be: abc, here a is postion 0, b is 1, c is 2)

*Example of indexing*

s[0] --> evaluates to "a" 
s[1] --> evaluates to "b"
s[2] --> evaluates to "c"
s[3] --> outwith bound so results in error.
s[-1] --> evaluates to "c"
s[-2] --> evaluates to "b"
s[-3] --> evaluates to "a"

**Slicing to get a substring**
- String can also be sliced to get multiple characters using: [start:stop:step]
- This will get characters starting at defined start postition up to and including stop-1.
- If step is omitted such that [start:stop], step size is automatically = 1.
- +ve reads from left to right and likewise, -ve goes right to left.
*Examples*
a = "ABC d3f ghi"

a1 = a[3:len(a)-1]
print(a1) --> *Output =  d3f gh*

a2 = a[4:0:-1]
print(a2) --> *Output = d CB*

a3 = a[6:3]
print(a3) --> *Output = EMPTY STRING*

__Showing Output__
- So far output hasn't been shown to user since we've beeb using the shell, to show the end user what we want, the *print* statement is used.
- Multiple objects can be printed using a comma to seperate them, example;

a = "the"
b = 3
c = "musketeers"
print(a,b,c) --> *Output = the 3 musketeers*

- This adds spaces in between each value.
- If no spaces is desired, all values must first be a string and then use + instead of , to join them together, like so;

a = "the"
b = 3
c = "musketeers"
print(a + str(b) + c)

**Input**
- To get input, the *input* command is used, example:

text = input("Type Anything: ")

- This displays a message to user saying type anything prompting them to enter whatever they want and then saves it as a variable, *text*.
- The user inout is saved as a *String*.
- If wanting to deal with numbers, must cast to integer using int(), example;

num1 = input("Type a Number: ") #say they type 5
print(num1*5) --> _Output = 55555_

num2 = int(input("Type a Number: ")) #say 5 again
print(num2*5) --> _Output = 25_

**F-Strings**
- Using f strings evaluates things in curly brackets at runtime, automatically changes them to strings and concatenates them to the string before them, example;

num = 3000
fraction = 1/3
print(num\*fraction, "is" ,fraction\*100, "% of" ,num) #Old way of doing it, space inbetween number and & sign.

print(num\*fraction, "is" ,str(fraction\*100) + "% of" ,num) # To fix had to cast percentage to a string to concatenate to % sign.

print(f"{num*fraction} is {fraction\*100}% of {num}") #Much simpler and probably more readable.

**Conditions for Branching**

#Binding variables and values

- In CS theres is two notions of equal;
- *Assignment and Equality test*

#Variable = Value 
- Assigns value to variable, replacing any old value assigned.

#Some_expression = Other Expression
- Equality test.
- Nothing new is bound.
- Variables are replaced for their values by the computer and compared against each other.
- Whole line is then swapped for either **True** or **False**. (Boolean)

**Other Comparison Operators**
- i > j
- i => j
- i < j
- i <= j
- i == j (Equality test, if i and j are the same returns True, otherwise False.)
- i != j (Inequality test, if i and j are the same returns False, otherwise True.)

**Comparison Operators**
- not a : True if a is False, False if a is True.
- a and b : True if *both* a and b are True, otherwise False.
- a or b : True if one or both a and b are Trure, False if both False.

**Why Boolean???**
- Good for flow contol and branching. Boolean allows us to assess if something is true so that the program can then decide which part of code to execute.
- Example; If this is true, do this otherwise do that.

**Branching in Python**

Example:
if <condition>:
    <code>
    <code>
    
<rest of program>

- <condition> has a Boolean value.
- Indentation is important in Python not only for readability but also for correct execution of code.
- Above says: Do code within block if True.

Example:
if <condition>:
    <code>
    <code>
    
else:
    <code>
    <code>
    
<rest of program>

- Above code says: if <condition> is true, execute code in block then join rest of program, if <condition> is False, execute the else block then rejoin rest of program.

Example:
if <condition>:
    <code>
    <code>
    
elif <condition>:
    <code>
    <code>
    
elif <condition>:
    <code>
    <code>
    
<rest of program>

- The elif statement here pretty much keeps checking new conditions for True or False until True is met. If none are true then nothing is run.

Example:
if <condition>:
    <code>
    <code>
    
elif <condition>:
    <code>
    <code>
    
else:
    <code>
    <code>
    
<rest of program>

- By using the else statement at the end, catches the case where nothing is True such that something is still run.