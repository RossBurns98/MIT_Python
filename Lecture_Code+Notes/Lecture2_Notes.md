__Strings__
- *String(str)* =  sequence of case sensitive characters (Letters, special characters, spaces, digits)
- *str* are enclosed in *single quotes or quotation marks* (try stay consistent using them).
- *Concatenate(join)* and *repeat* strings : 
a = "me"
b = "myself"
c = a + b
*Output: c = "memyself"*
d = a + " " + b
*Output: d = "me myself"*
silly = a * 3
*Output: silly = "mememe"*

**String Operation**
- len(): function used to get length of a string within the parentheses.

s = "abc"
chars = len(s)
*char = 3.*

**Slicing for one character in a string**
- Recall in computing, counting starts from 0, not 1.
- Using *square brackets*, can "index" sting which allows us to get value at certain position/index (Example of position would be: abc, here a is postion 0, b is 1, c is 2)

*Example of indexing*

s[0] --> evaluates to "a" 
s[1] --> evaluates to "b"
s[2] --> evaluates to "c"
s[3] --> outwith bound so results in error.
s[-1] --> evaluates to "c"
s[-2] --> evaluates to "b"
s[-3] --> evaluates to "a"

**Slicing to get a substring**
- String can also be sliced to get multiple characters using: [start:stop:step]
- This will get characters starting at defined start postition up to and including stop-1.
- If step is omitted such that [start:stop], step size is automatically = 1.