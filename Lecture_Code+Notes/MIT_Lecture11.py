# Build to req
def remove_all(L,e):
    '''
    L is a list
    Mutates L to remove all elements equal to e
    Returns None (Mutates L)
    '''
    Lcopy = L[:] #Make copy to store
    L.clear() # Empty L
    for i in Lcopy:
        if i != e:
            L.append(i) #Adding elements

L = [1,2,2,2]
remove_all(L,2)
print(L)

P = [1,2,3,4]
P.pop(2)
print(P)

#Playing with Alias

old_list = [[1,2], [3,4], [5,'foo']]
new_list = old_list

new_list[2][1] = 6
print(new_list)
print(old_list) # Same as new_list

# Surface Level clone example

old = [[1,2],[3,4],[5,6]]
new = old[:]

old.append([7,8])

print(old)
print(new)

old[1][1] = 9

print(old)
print(new)