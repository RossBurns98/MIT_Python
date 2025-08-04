def all_true(n, Lf):
    """ n is an int
        Lf is a list of functions that take in an int and return a Boolean
    Returns True if each and every function in Lf returns True when called 
    with n as a parameter. Otherwise returns False. 
    """
    # Your code here
    flag = True # Good to set initial condition.
    for f in Lf:
        if not f(n): # Could be done using: if f(n) == False
            flag = False
            break  # Stops loop after one failure
    return flag

# Generic list of simple functions, Lf.
def is_even(x): return x % 2 == 0
def greater_than_5(x): return x > 5
def less_than_10(x): return x < 10
Lf = [is_even,greater_than_5,less_than_10]
# Examples:    
print(all_true(6,Lf))