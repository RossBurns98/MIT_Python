**break STATEMENT**

- When python registers this, immediatly exits the loop it is in.
- Skips remaining expressions in block.
- Exits only *innermost* loop.
- In below example, <expression_b> is never actually evaluated since the break statement exits that block of code.

while <condition_1>:
    while <condition_2>:
        <expression_a>
        break
        <expression_b>
    <expression_c>

**MID LECTURE SUMMARY**

- Objects have types
- Expressions are evaluated to one value and then bound to a variable name.

- Branching
    - if, else, elif
    - Program executes one set of code or another depending on variables.

- Looping Mechanisms
    - while and for loops
    - Code executes repeatedly while some condition is true.
    - Code executes repeatedly for all values in a sequence.

**Guess-and-Check**

- Process called *exhaustive enumeration*
- Applies to problems where:
    - A value for the solution can be *guessed*
    - You can *check* if the soultion is correct.
- Can *keep guessing* until:
    - Solution is found
    -All values have been guessed.

**Guess-and-Check Square Root**

- Basic Idea: 
    - Given an *int*, say *x*, want to see if there is another int which is its square root.
    - Start with a *guess* and check to see if its right.
    - To be *systematic*, start with *guess* = 0, then 1, then 2 etc.
- If *x* is a perfect square, we will eventually find its root and stop.

- What to do if *x* isn't a perfect square?
    - Need to know when to stop.
    - Use algebra - if *guess* squared is larger than *x*, then stop.

*Guess-and-Check SQUARE ROOT*
- in code file doesn't include negative, it would automatically terminate.
- Need to *Check for negative inputs* and handle accordingly.

**_While_ loops or _for_ loops**

- Seen that for loops are more clean looking since they work over a sequence.
    - Since we don't need to set up the iterant ourselves
    - also less likely to lead to errors.

