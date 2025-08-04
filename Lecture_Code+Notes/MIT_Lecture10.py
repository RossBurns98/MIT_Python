# l = [1,2,3,4]
# 
# l.append(4)
# 
# print(l)
# 
# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 + L2
# L3.append(L4)
# L = L1.append(L3)
# 
# print(L1)
# print(L2)
# print(L3)
# print(L4)
# print(L)

# Make function which meets reqs

# def make_ord_list(n):
#     '''
#     n is a positive int
#     Return List containing all ints in order from 0 to n inclusive
#     '''
#     P = []
#     for i in range(0,n+1):
#         P.append(i)
#     return P
            
# print(make_ord_list(6))

# def remove_elem(L,e):
#     '''
#     L is a list
#     Returns new Lists with the same order
#     as L but no elements equal to e.
#     '''
#     newlist = []
#     for i in L: # i is not index
#         if i != e:
#             newlist.append(i)
#     return newlist

# L = [1,2,4,2]
# print(remove_elem(L,2))

# Write a function that meets reqs

# def count_words(sen):
#     '''
#     sen is a string representing a sentence
#     Returns how many words are in the sentence.
#     '''
#     L1 = sen.split(' ')
#     return len(L1)

# print(count_words("Hello it's me"))

#write a function that meets req

def sort_words(sen):
    '''
    sen is a string representing a sentence
    Returns a list containing all the words in the sen
    but in sorted order
    '''
    L1 = sen.split(' ')
    return sorted(L1)

print(sort_words('look at this photograph'))
