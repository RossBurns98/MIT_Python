**Abstraction**

- Abstract away details of code, such that we know its function without knowing how it actually does it.
- Like a phone, we know the volume buttons will increase and decrease volume without actually knowing how/why it does it.
- We know its interface but not its innerworkings.

- **Abstraction** _enables_ **Decomposition**

- We want to hide details of code such that we can treat it like a black box, ie we know what it takes in and what it spits out.
- We also want to reuse the black box (without copying it...)

- *Abstraction* is achieved using functions (or Procedures).
- We can create funcitons of our own.

- Functions have specifications, which can be shown using "doctrings".
- Doctrings tell users what the function does, what it requires to do it and any negatives.

- Defining a function tells python some new code is stored in memory.
- Functions are only useful when "run" ("called"/"invoked")
- They can be run multiple times
- Only runs when the run button is hit.

**Function Characteristics**

- Has a _name_.
- Has parameters (0 or more)
    - Inputs*
- Optionally has a _doctring_
    - Comment defined by """ which provides specifications for the function.
- Has a _body_, instructions to execute when function is run.
- _Returns_ something.
    - Keyword _return_

Example of writing a function:

def is_even(i):
    """
    Input: i, positive int
    Returns True if i is even, otherwise False.
    """ 
    """
    if i%2 == 0:
        return True
    else:
        return False
    
def: Keyword, define function
is_even: Function name
(i): Input
"""""": docstring
if else block: body
return: tells python to give back some value.

**What Happens when Function is called**

- For the example, calling the function requires the user to replace i, with a number.
- This number then replaces i in all of the block of code which is then run, replacing the is_even() call with either True or False.


**WHEN SOLVING PROBLEMS, DON'T CODE FIRST, THINK FIRST, TRY SOLVE A SIMPLER VERSION AND THEN ADAPT**