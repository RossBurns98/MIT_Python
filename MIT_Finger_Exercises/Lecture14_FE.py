# Part 1
def keys_with_value(aDict, target):
    """
    aDict: a dictionary
    target: an integer or string
    Assume that keys and values in aDict are integers or strings.
    Returns a sorted list of the keys in aDict with the value target.
    If aDict does not contain the value target, returns an empty list.
    """
    SList = [] #list to hold wanted nums
    for i in aDict: # i is a key
        if aDict[i] == target: # aDict[i] accesses value of key and compares
            SList.append(i) # if ==, adds to list
    return sorted(SList)    
 # Your code here
# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target)) # prints the list [1,5]

# Part 2
def all_positive(d):
    """
    d is a dictionary that maps int:list
    Suppose an element in d is a key k mapping to value v (a non-empty list).
    Returns the sorted list of all k whose v elements sums up to a
    positive value.
    """
    PList = [] # empty list for k with p sum of v
    for k,v in d.items(): # turns to items so can work with k and v
        summed = sum(v) # extra line for me, just sums
        if summed > 0: # checks if greater
            PList.append(k) # if greater, add to PList 
    return sorted(PList)

 # Your code here
# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d)) # prints the list [1, 2]