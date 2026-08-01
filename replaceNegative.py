original = [8, 20, -10, 55, -777]
for i in original:
    print(i)

 #Changes the oringial list into all positive integers by taking the absolute value of all of the elements in the orignial list
modified_list = [abs(i) for i in original] 
print("Modified list: ", modified_list)