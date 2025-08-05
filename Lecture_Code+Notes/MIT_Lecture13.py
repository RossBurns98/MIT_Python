# example of try and except not being used
def sum_digits(s):
    """
    s is a non empty string containing digits
    returns sum of all chars that are digits
    """
    total = 0
    for char in s:
        if char in "0123456789":
            val = int(char)
            total += val
    return total

# Using the if char in "0123456789" part handles existence of non ints, without this it crashes
# better way would be using except and try

def sum_digits_except(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print(f"can't convert {char}")
    return total

print(sum_digits_except('123abc'))


# Lecture challenge

def pairwise_div(Lnum, Ldenom):
    """
    Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    returns new list whose elements are pairwise division of an element in Lnum by element in Ldenom
    Raise a value error if Ldenom contains 0
    """
    L = []
    #L = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    if 0 in Ldenom:
        raise ValueError('silly')
    for i in range(len(Lnum)):
        try:
            L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError('silly')
    return L

# Asserting to ensure docsting is followed
def pairwise_div_assert(Lnum, Ldenom):
    """
    Lnum and Ldenom are non-empty lists of equal lengths containing numbers
    returns new list whose elements are pairwise division of an element in Lnum by element in Ldenom
    Raise a value error if Ldenom contains 0
    """
    assert len(Lnum) == len(Ldenom), "Lnum and Ldenom aren't equal length!"
    assert len(Lnum) and len(Ldenom) != 0, "Empty list!"
    L = []
    #L = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    if 0 in Ldenom:
        raise ValueError('silly')
    for i in range(len(Lnum)):
        try:
            L.append(Lnum[i]/Ldenom[i])
        except:
            raise ValueError('silly')
    return L

L1 = [1,2,3]
L2 = [1,2]

print(pairwise_div_assert(L1,L2))
