# The next two lines are lists. The first one has strings and integer and the second one consists of five integers
list1 = ['physics', 'chemistry', 1997, 2000] 
list2 = [1, 2, 3, 4, 5]

#print("list1[0] : ", list1[0]) # This command will display the first element in list1 which is 'physics' 
#print("list2[1:5] : ", list2[1:5]) # This command will display indexes 1-4 in list2 which is everything except 1 [2, 3, 4, 5]

#print(f"Value before update: {list2}") # This command will print list2 as it is on line 3. [1, 2, 3, 4, 5]
#list2[2] = 10 # We are making an addition to list2 by inserting 10 at index 2.
#print(f"Value after update: {list2}") # This command prints list2 after updating it.

#Adding elements using Append
#list1.append(2020)
#print("New list", list1)

#Adding elements using Insert
list1.insert(0, 'Python')
print("After inserting: ", list1)