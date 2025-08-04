# Mutability

- Lists are **mutable**.
- Assigning a new variavle to an index **changes** the previous value to the new one.

Example:
L = [2, 4, 3]
L[1] = 5 - L = [2, 5, 3]

# Append

- Add an element to the end of a list with L.append(element), L is the list name.
- Mutates the list

Example

L = [2,1,3]
L.append(5) -> L now = [2,1,3,5]

# What is the dot?

- Everything in python is object
- Object has data
- Object types have associated operations
- Access info with object_name.do_something()
- Same as doing append with L
- Append = operation
- L = object
- () = parameter

# String to List

- Convert **string to list** with list(s).

- s.split(), **splits a string in a character parameter**, splits on spaces if no parameter is called.

# List to string

- Convert a **list of strongs back to a string**
- Use ''.join(L) to turn a **list of strings into a bigger string**.
- Use a character in the '', to add the character between each element.
- Only works on lists with only string elements.

# Interesting Operations

**L.append()** = add element to end of list (mutates)
**L.sort()** = sorts elements (mutates)
**L.reverse()** = reverses list (mutates)
**sorted()** = returns a sorted version of L, need to make a new variable (doesn't mutate)

L = [9,6,0,3]
L.append(5) -> [9,6,0,3,5]
a = sorted(L) -> [0,3,5,6,9]
b = L.sort() -> L = [0,3,5,6,9] and returns None for b
L.reverse() -> L = [9,6,5,3,0] and returns None.

reverse and sort are functions so they need () but don't need anything on them to work.

# Lists support Iteration

- Make a function which squares each element and mutates.

def square_list(L):
    for i in range(len(L)):
        L[i] = L[i]**2

- Doesn't need return since its mutating the list.

# Combining Lists

- Concatenation, + operator, creates **new** list with copies.
- Mutate list with **L.extend(some_list)**

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2 -> [1,2,3,4,5,6]

L1.extend([0,6]) -> mutates L1 to [1,2,3,0,6]
L2.extend[([1,2],[3,4]]) -> L2 mutates to [4,5,6,[1,2],[3,4]]

# Removing all element

- L.clear mutates a list by remvoing all elements.
- Can check to see if its the same thing in memory using id() in console.

# Summary 
- Lists and tuples provide a way to organise data which supports iteration.
- Tuples are immuatable(like strings)
    - Useful for data which doesn't need to change.
- Lists are mutable
    - Can modify object by changing element at an index
    - can modify by adding elements at the end
    - Useful in dynamic solutions