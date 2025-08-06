# Dictionaries

- storing say student data and grades in list format can get messy quickly with the amount of students as well as the intricacy of functions needed to pull relevant data from list.

# Cleaner Way: Dictionaries

- Nice to use one data structure, no seperate lists.
- Nice to index utem of interest directly
- Python dictionary has entries that map key:value

# A Python Dictionary 

- Stores pairs of data as an entry
    - Key(any immutable object)
        - str,float,int,bool,tuple,etc
    -value(any data object)
        - same as above as well as lists and other dicts
- Curly Brackets for dicts

my_dict = {} # Syntax for making empty dict
d = {4:16} # dict with one entry
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}

# Dictionary Lookup

- Similar to indexing into a list 
- Looks up the KEY
- Returns the value associated with the Key
    - if no key found, returns error.

# Dictionary Operations

grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}

- Add an entry:
    grades['Grace'] = 'A' # Adds 'Grace' if not already there
- Change an entry
    grades['Grace'] = 'C' # Overwrites old value.
- Delete entry
    del(grades['Ana']) # Removes Ana and value from dict

- All above mutate dict

- Test if key in dictionary

'John' in grades -> returns True
'Daniel' in grades -> returns False
'B' in grades -> returns False

- can iterate over dict, but assume theres no order. 

- get an iterable that acts like a tuple of all keys
    grades.keys() -> returns dict_keys([blah])
    list(grade.keys()) -> returns ['blah']
- get an iterable that acts like a tuple of all dict values
    grades.values()
    *Same idea as .keys*

# Dictionary Operations (useful way to iterate over dict entries)

- again, assume no order
- get iterable that acts like tuple of all items
    grades.items()
    returns both keys and values as a pair in a tuple

- iterating iver key,value tuple:
    for k,v in grades.items():
        print(f"key {k} has value {v})

# Dictionary Keys and Values

- Dicts are mutable objects (aliasing/cloning rules)
    - use = sign to make alias
    - use d.copy() to make copy (d = dict name)
- Assume no order
- Dict values
    - Any type(immutable and mutable)
        - could be lists or even other dict
    - can be duplicates
- keys 
    - must be unique
    - immutable(int, float, bool, string, tuple)
        - really needs something hashable, but for now thinking immutable is fine.
    - be careful with floats as keys

# Why IMMUTABLE/HASHABLE

- dictionary is stored in memory in a special way

- step 1: Function run on dict key
    - function maps any obj to an int
    eg. map "a" to 1, "b" to 2 so ab could map to 3
    - the in is the position in a block of memory addresses.
- step 2: at the memory address, store the dict value
- to do a lookup using a key, run same function
    - if obj is immutable/hashable then you get same int back
    - if changed then function gives different int back

# Recap on List vs Dicts

**List**
- Ordered sequence of elements (index)
- Look up elements by integer index
- Indices have an order
- Index = integer
- Value can be any type

**Dict**
- Matches "keys" to values
- Look up one item by another item
- No guarenteed order
- Key = anything immutable/hashable
- value = anything

# Example: Find most common words in a song's lyrics

**Goal**
1) Create Frequency Dict mapping str:int

2) Find word that occurs most often and how many times
    - Use a lost, in case more than one word with same number
    - Return tuple(list, int) for (words_list, highest_freq)

3) Find words that appear at least x amount of time
    - Let user choose "at least X amount of times"
    - return a list of tuples, each tuple us (list, int) containinf list of words ordered by frequency 
 (see code file)