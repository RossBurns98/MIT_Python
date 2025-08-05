# List Comprehension, Functions as Objects, Testing, Debugging

# List Comprehensions

- Applying function to each element of a sequence, then making new list is common.

**Example**

def f(L):
    Lnew = []
    for e in L:
        Lnew.append(e**2)
    return Lnew

- So common that Python lets you do it in one line, **List Comprehension**.
    - Workflow for this: Create List, apply function to elements of list, Optionally only apply function to elements which satisfy a test.

**List Comprehension Version of Example**

Lnew = [e**2 for e in L] 

**New Example**

def f(L):
    Lnew = []
    for e in L:
        if e%2 == 0:
            Lnew.append (e**2)
    return Lnew

Lnew = [e**2 for e in L if e%2 == 0]

- In general, syntax is:   
[expression for elem in iterable if test]

- Can use List Comprehension for tuples too and other iterables, like range().

[[e,e**2] for e in range(4) if e%2 != 0]
- can even return lists in List Comprehension.

- **Outputs List**.

- Supports multiple conditions.

# Functions: Default Parameter

- For old bisection method we hard coded epsilon but what if a user wanted to change that range?
    - we could change in the function(all calls affected. would rather each had a choice)
    - use epsilon outside function(bad)
    - or we could make it an argument of the function.

- Making argument is good but maybe some don't know what a good epsilon is/ don't care.
- would be better to give them option but also make a default value for the cases mentioned above.
- Use a default parameter.

def bisection_method(x, epsilon=0.01):
    low = 0
    high = x
    guess = (high + low)/2.0
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
    return guess

print(bisection_method(123))
print(bisection_method(123,0.5))

- Default parameter set as shown (epsilon=0.01)

- every time we have default parameters, they must go to the end.

- can be called in any way ie (bisection method(epsilon = 0.1, x = 123))

- Not ok:
    - bisection_method(epsilon=0.001, 123) ~ error
    - bisection_method(0.001, 123) ~ not error just wrong

# Functions Returning Functions

**Functions CAN return Funcitons**

def make_prod(a):
    def g(b): ~ Definition inside another function
        return a*b 
    return g ~ Not a function Call

val = make_prod(2)(3)
print(val)


**Walkthrough**
- make_prod is in global env, calling make_prod(2)(3), reads 2 first and makes new env where a = 2 and g is defined.
- The return returns g's code, so now global env knows about g which then makes make_prod(2) = g which changes:
    make_prod(2)(3) -> g(3).
- now g makes own env, g doesn't know a but can take a from the caller, make_prod. here b is 3 and a is 2 so g returns 6 to global env.
- which makes val = 6.

- This can be done in a more verbose, less chained way:

doubler = make_prod(2) ~ doubler = g, a = 2
val = doubler(3) ~ really g(3), b = 3, a from doubler/make_prod
print(val) 

**Why bother?**

Good Design:
- Good code like decomp and abstraction.
- Another structure tool for code 
Interrupting Execution:
- Control flow example.
- way to achieve partial execution, allowing use of result somewhere else before finishing.

# Testing and Debugging

**Defensive Programming:** 
    - Write specs for functions
    - Modularise programs
    - Check conditions on inputs/outputs(assertations)
**Testing/Validation:**
    - Compare input/output pairs to specs.
    - "It's not working!"
    - "How can I break this code?"
**Debugging:**
    - Study events leading to error
    - "Why is this not working?"
    - "How can I fix my program?"

# Make life easier

- From start, design code to ease debugging and testing
- use comments all the time
- break into modules which can be tested/debugged individually 
- Document constraints:
    - What do we expect the input to be?
    - what is the expected output?
- Document assumptions.

# When am I ready to test?

- Ensure code runs
    - remove syntax errors
    - remove static semantic errors
    - interpreter can usually find these.
- have a set of expected results
    - input set
    - for each input, expected output

# Classes of testing

- **Unit Testing**
    - validate each piece of program
    - test each function seperately
- **Regression Testing**
    - add bug tests as found
    - catch reintroduced errors that were fixed before
- **Integration testing**
    - Does overall program work?
    - Tend to rush to this part

# Testing Approaches

- **Intuition** about natural boundaries.
- If no natural partitions, might do **random testing**
    - Prob that code is right increases with more testing.
- **Black Box testing**
    - Code of function is black box, dont look at it.
    - Use docstring to write test cases.
- **Glass Box testing**
    - Use code itself to design test cases.
    - path complete if each potential path through code is tested once
    - leads to loads of test cases since we need to go through loops multiple ways, like avoiding while loops, going through once and going though lots.

# Debugging Steps

- creative process which gets simpler with experience.

- Study program code
    - Don't ask whats wrong
    - ask how did I get unexpected result
    - part of a family?
- **Scientific Method**
    - study available data
    - form hypothesis
    - repeatable experiments
    - pick simplest input test

# Print statements

- good way to test hypothesis

- bisection method is a good way of testing
    - put a print statement in the middle then adjust based on error, move according to error existing.