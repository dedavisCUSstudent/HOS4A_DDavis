def first(n):
    return n[0]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print(sort_list_first([(5,2), (2,1), (4,4), (3,2), (1,2)])) #Should sort by n[0] or first element of the tuple

#What if we use n[1] instead of n[1]
def first(n):
    return n[1]

def sort_list_first(tuples):
    return sorted(tuples, key=first)

print(sort_list_first([(5,2), (2,1), (4,4), (3,2), (1,2)]))