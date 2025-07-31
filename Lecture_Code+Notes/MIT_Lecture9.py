# Last Lecture
def apply(criteria,n):
    count = 0
    for i in range(0,n+1):
        if criteria(i):
            count +=1
    return count

def is_even(x):
    return x%2==0

# Reusable Function Version
def is_5(x):
    return x==5

# For comparison
print('apply with is_5:', apply(is_5, 10))

# Lambda usage
print('apply with anon fcn', apply(lambda x: x==5, 100))

# Other way 
print(is_even(8))
print((lambda x: x%2 == 0)(8))

seq = (2, 'a', 4, (1,2))

print(len(seq))

#Strength of Tuples
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return(q, r)

both = quotient_and_remainder(10,3)

(quot, rem) = quotient_and_remainder(5,2)


#Write a function which meets these specs

def char_counts(s):
    '''
    s is a string of lower cased characters
    returns a tuple where the first value is number of vowels
    and the second value is the number of consonants.
    '''
    vowel = 'aiueo'
    (c, v) = (0, 0)

    for i in s:
        if i in vowel:
            v += 1
        else:
            c += 1
    return(v, c)

# print(char_counts('abcd'))
# print(char_counts('zcght'))

def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1,2,3,4,5,6))