# Making Copy of list

- Can make copy of list by duplicating all elements into a new list.

Lcopy = L[:]

: here pretty much uses the slicing technique [a:b:c] start at a end at b in steps of c. [:] pretty much defaults to start at 0, end at the last value in steps of 1.

- Without it would just override original 

# Ops on Lists: Remove

- Delete element at a **specific index** with del(L[index])
- Remove element at **end of list** with L.pop(), returns removed element (can also call specific index)
- Remove a **specific element** with L.remove(element).
    - Only removes first occurence of element.
    - if it doesn't exists returns error.

# Aliasing

- Alias another name for the same object.
- Assigning (=) on a mutable object like L, creates a new alias not a clone.

- Surface level copying like L2 = L1[:] copies elements exactly but don't share changes unless the element itself is mutable. 

- Example on .py file

- So copys shallow structure but if object is mutable on its own are shared instead of copied.

- changing new list also edits the old list, except for [7,8] in old.

- importing copy, using copy.copy is a shallow copy, copy.deepcopy is a deep copy.
- Deep copy makes it such that nothing is shared, all individual.

# Lists in Memory

- Seperate idea of Object vs name we gave it
    - list is object in memory
    - name points to object
- = creates aliases
- if a copy is wanted, tell python explicitly.