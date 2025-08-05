#Default Param

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

def make_prod(a):
    def g(b): # Definition inside another function
        return a*b 
    return g # Not a function Call

val = make_prod(2)(3)
print(val)