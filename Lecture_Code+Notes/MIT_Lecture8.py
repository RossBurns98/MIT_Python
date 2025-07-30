# Fix this code:

def is_triangular(n):
    """
    n is an int > 0
    Returns True if n is triangular, i.e. equals a continued summation of natural numbers (1+2+3+4+...+k)
    False Otherwise
    """
    total = 0
    for i in range(n + 1):
        print(i)
        total += i
        if total == n:
            return(True)
    return(False)


# Changed range to n + 1, instead of n, also changed print to return.

# Function version of bisection method code from a previous lecture

def bisection_method(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

# Write code which finds how many numbers share the same square root.

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have same square root within epsilon of n
    """
    count = 0
    # Using larger n than n**2, so that any possible values aren't missed
    for i in range(n**3):
        # Sqrt of i with bisection method
        sqrt = bisection_method(i)
        if abs(n - sqrt) < epsilon:
            count += 1
    return count

print(count_nums_with_sqrt_close_to(10, 0.1))

def f(y):
    x = 1
    x += 1
    print(x)

x = 5
f(x)
print(x)