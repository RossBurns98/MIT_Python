# Functions as Objects

Last Lecture Function:

def is_even(i):
    """
    Input: i, a positive integer
    Returns True if i is even and False otherwise
    """
    return i%2 == 0

- If return is dropped from above, Python returns a None value.
- None is a value type called NoneType, represents absence of a value.

## Example's of Print and Return in Functions

def add(x,y):
    return x+y
def mult(x,y)
    print(x*y)

add(2,3) - Returns 2+3 but doesn't print anything
print(add(2,3)) Prints 5

mult(3,4) - Prints 12.
print(mult(3,4)) - Prints 12 then None due to lack of return statement.

__Return vs Print__

- __Return__ only has meaning within a function.
- *Only one* return can be used within a function.
- all code *before* the return function is run but any *after* a return function will not be run/used.
- Has associated value, passed back to function caller.

- Print can be used outside functions.
- any amount of print statements can be used within a function.
- any code after a print statement is still executed.
- Also has value associated with it, output into the console.
- Print statement on its own returns None value.

print(print(5)) - Outputs 5 then None.

Using and reusing functions make code much more readable and more simple to follow.

## Function Scope

__Understanding Function Calls__

- How does Python execute a function call?
- How does Pyhton know what value is associated with a variable name?

- It **Creates a new environment** with every call!!!
    - Like a mini program it needs to complete
    - The mini program runs with assigning its parameters to some inputs.
    - It does work (functions body)
    - Returns a value.
    - Environment vanishes after value is returned.

## Environments

- **Global Environment**
    - Where we interactt with Python.
    - Where Program starts.
- Invoking Function makes new environment (frame/scope).

## Variable Scope

- Formal parameters are bound to the value of input parameters
- Scope is a mapping of names on objects.

**Code example**

def f(x): ~ *Formal Parameter*
    x = x + 1
    print('in f(x): x =', x)
    return x

x = 3 ~ *Actual Parameter*
z = f(x) ~ *Makes new environment*

## Other example

- Inside a function can access a variable outside a function.
- However, it cannot alter this defined outside. Results in an Error.

## Higher Order Operations

- Objects in Python have a type:
    - int, bool, float, str, NoneType, function
- Objects can be:
    - Used as an argument to a procedure.
    - Returned as a value from a procedure.
- Functions are **First Class Objects**.
- Treat them like the other types.
    - They can be aruguments to another function.
    - They can be returned by another function.

# Summary

- Functions are First class objects.
    - They have a **Type**
    - Can be **assigned as a value** bound to a name.
    - Can be used as an **argument** to another procedure.
    - Can be **returned** as a value from another procedure.

- Be careful about environments:
    - Main program runs in Global Environment.
    - Calling a function makes a new temp environment for that function.
- Enables creation of nice, concise and clean code.