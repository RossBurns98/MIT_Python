# Lambda, Tuples and Lists

**Anonymous Function**

- Sometimes don't want to name functions, especially simple ones. Eg like a 2 line one.
- Can use anonymous procedure with 'Lambda'
- Lambda creates a procedure/function object, which doesn't have a name tied to it

def is_even(x):
    return x%2 == 0

*Lambda alternative to above simple function*
lambda x: x%2 == 0

- share same parameter and body.

- Lambda is a **one time use function** due to it being nameless.

# NEW DATA TYPE

- Seen scalar types before: int, float, bool
- Seen one compound type: string

- two more compund data types: **Tuples** and **Lists**.


# Tuples

- **Indexable ordered sequence** of objects:
    - Objects can be any type - int, string, tuple, tuple of tuples.
- Cannot change element values, **immutable**

te = () #empty tuple
ts = (2,) #comma hear denotes tuple, if left out just an int.

t = (2, 'mit', 3) # multiple object tuple

t[0] - evaluates to 2
(2, 'mit', 3) + (5,6) - evaluates to (2, 'mit', 3, 5, 6), concatenates two tuples together into new one.
t[1:2] - slice tuple, goes to ('mit',)
t[1:3] - slice tuple, goes to ('mit',3)
len(t) - goes to 3
max((3, 5, 0)) - goes to 5
t[1] = 4 - error, can't change object.

seq = (2, 'a', 4, (1,2))

print(len(seq)) - 4
print(len(seq[3])) - 2
print(seq[3][0]) - 1 #accessing tuple inside the tuple and indexing that.

- Can be used to quickly swap variable values:

x = 1
y = 2
(x, y) = (y, x)

- **Allow us to bypass return only allowing the return of one value, it can return one tuple containing multiple values, like:**

def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return(q, r)
 both = quotient_and_remainder(10,3)
 (quot, rem) = quotient_and_remainder(5,2)

 # Variable Number of Arguments

- Python has some built in functions which take variable number of args, like min
- Python allows user to have same capability using the *** notation**

example would be mean:

def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

mean(1,2,3,4,5,6) - (1,2,3,4,5,6) is args.

# Lists

- Indexable ordered sequence of objects
    - Usually homogeneous (all ints, floats, strings, lists)
    - but can be mixed(uncommon)

- **Denoted** by [].
- **Mutable**, meaning specific elements values can be changed within list.

**Lists of Slicing etc..**

a_list = [] - empty list 
L = [2, 'a', 4, [1, 2]] - List contained in a list at L[3].
[1, 2] + [3, 4] - [1, 2, 3, 4]
len(L) - evaluates to 4.
L[0] - 2
L[2] + 1 - evaluates to 5
i = 2
L[i - 1] - goes to 'a' since L[1] is 'a'.
max([3, 5, 0]) - goes to 5

# Iterating over a List (same for Tuples)

- Compute the sum of elements in a list.
- common pattern:

total = 0
for in in range(len(L)):
    total += L[i]
print(total)

More readable and concise version:

total = 0
for in in L:
    total += i
print(total)

Function version of Above code:

def list_sum(L):
    total = 0
    for i in L:
        total += i
    return total