**Motivation**

Motivating Code for the Lecture:

x = 0
for i in range(10):
    x += 0.1
print(x == 1)
print(x, "==", 10*0.1)

- This code compares what we believe to be, 1 == 1. 
- However with the use of floating point numbers, python stores them with slight errors such that, we are actually comparing 0.999999999999 == 1.0, _which isn't the same._

**Main Point**

- Don't use == to test floats
    - Should instead see if theyre within a small amount of one another.
- What is *Printed* isn't always what is stored in *memory*.
- Be *careful* in making algorithms with floats.

**EFFECT of APPROXIMATION on our ALGORITHMS**

- *Exact* answer may not be *accessible*.
- Need to find ways to get *good enough* answer, i.e. close to ideal.
- Need to work around using exhaustive enumeration since possible answers is in thery infinite.
- Floating point *approximation errors* are important.

**APPROXIMATION**

- Find an answer that is *"good enough"*
    - e.g., find r such that r*r is within a small distance of x.
    - Use epsilon: given x we want r such that |r**2 - x| < epsilon.
- Algorithm
    - Start with a guess which is *Known to be too small* - say g.
    - Incriment by a small value - call it a - to give a new guess g.
    - check if g**2 is close enough to x (within epsilon)
    - Continue until get a good enough answer.
- Looking at all possible values of g + k*a for integer values of k - similar to exhaustive enumeration.
    - can't test all possibilities as infinte.

**APPROXIMATION ALGORITHM**

- In this case we have *2 parameters* to set:
    - epsilon (how close we are to answer?)
    - increment (how much to increase or guess?)

- Performance varies based on these values
    - In speed 
    - In accuracy

- Decreasing increment size --> slower program, yet likely better approximation.

Example code:

x = 36
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1

print("num_guesses =", num_guesses)
print(guess, "is close to square root of", x)

- Above code doesn't always terminate, for lare values it takes lots of time but it does work relatively well.

- So as seen with above code as well as code in .py document, **we can overshoot the epsilon** value. 
- Therefore, another *end condition is required*.

**Approximation Lessons Learned**

- Can't use == to check for exit condition, needs to be +- of actual value.
- Need to take care that we don't jump the exit condition and loop forever.
- Tradeoffs exists, **can make an algorithm which is 10x more procise than another whilst being 100x slower**.
- Need to think how close we want to be to an answer when setting parameters of algorithm.
- For good/great answers, this can be quite slow, which begs the question, _"Is there anything better for this"_
- Yes there is! (Next lecture).
- Something which skips lots of the pointless values, ie theres no way that the sqrt of 54321 is gonna be less than 100 so they were pointless to do, so we need something which checks and skips these things quickly (**Bisection method.**)

**Summary**

- Floating point numbers produce problems and inconsistencies.
- They can't be represented in memory exactly.
    - Operations on floats produce errors, more operations = larger error.
- Approximation methods use floats
    - Like Guess-and-check except
    [1] We use a float as increment
    [2] We stop at a close enough asnwer, not exact.
- NEVER USE == TO COMPARE FLOATS in stopping condition.
- Take care incase of overshooting the +- boundary.