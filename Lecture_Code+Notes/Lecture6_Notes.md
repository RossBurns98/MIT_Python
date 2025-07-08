**BISECTION SEARCH**

- Apply to problems with an order to the range of possible answers.
- Suppose we know the answer is within some interval, Bisection method: 
    - Guesses **Midpoint**
    - If wrong, checks extra info to see if too high or low
    - Change Interval
    - Repeat
- Process cuts things to check in half each time
    - Exhaustive checks (Guess-and-Check) reduces them from N to N-1 each time
    - Bisection method goes from N to N/2.

**LOG GROWTH is BETTER**

- Process cuts set of things in half at each stage
    - Characteristic of Log growth
- When Comparing Guess-and-Check to Bisection method:
    - Checking answer one-by-one is linear in the number of guesses.
    - Checking answer by halfing at the midpoint each time is logarithmic on the number of guesses
    - Log algorithm is much more efficient.
    - We want O(log(n)) where possible.

**MAIN IDEA; BISECTION SEARCH TAKES ADVANTAGE OF PROPERTIES OF THE PROBLEM**

[1] The Search Space is ORDERED
[2] We Can Tell if the Guess is TOO HIGH or TOO LOW.

**The Code used in .py file**

- This took 30 guesses compared to the original 23M guesses, this is logarithmic in size of the problem such that we reduce the search space by N/2**k which converges on log_2(N).

- **HOWEVER** when we use 0< x <1, the code breaks. It gets to a point where if we use x = 0.5 that the high and low values are both 0.5 and loops infinitely.

**Notes on Bisection**

- Reduces the amount of computation time quickly.
- Over time reduces search space at a slower rate compared to the beginning.
- Works on *problems with an ordering property*, so if this isn't present, can't be done.

**Newton-Raphson Algorithm**

- *General* approximation algorithm for finding roots of a **Polynomial** in one variable.

- Showed that if g is an approximation to the root and p is a polynomial:

        g - p(g)/p'(g)

is a better approximation where p' is the derivative of p.

- Very quick, about 3 times as quick as Bisection method but limited by its specificity, ie, only useful for finding square roots of polynomials.
