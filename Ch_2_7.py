# Write a python program that removes any repeated items from a list so that each item appears at most once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

# list1=[1,2,3,4,5,5,6,6,7,7,8,8]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)

# print(list2)

def remove_duplicates(input_list):
    return list(set(input_list)) #mistake

# Example list with repeated items
input_list = [1, 1, 2, 3, 4, 3, 0, 0]

# Removing duplicates
unique_list = remove_duplicates(input_list)

# Printing the list with unique items
print("List with duplicates removed:", unique_list)

        
