#List
list1 = [1, 2, 3, 4, 5]
print("Original List:", list1)
#Appending an element
list1.append(6)
print("After Appending 6:", list1)
#Removing an element
list1.remove(3)
print("After Removing 3:", list1)
#Accessing elements
print("Element at index 2:", list1[2])  
#Slicing the list
print("Sliced List (index 1 to 4):", list1[1:4])
#Iterating through the list
for item in list1:
    print("List Item:", item)   
#Length of the list
print("Length of List:", len(list1))
#Sorting the list
list1.sort(reverse=True)
print("Sorted List in Descending Order:", list1)
#Finding the index of an element
index_of_4 = list1.index(4)
print("Index of element 4:", index_of_4)
#extending the list
list2 = [7, 8, 9]
list1.extend(list2)
print("After Extending with [7, 8, 9]:", list1)
#reversing the list
list1.reverse() 
print("Reversed List:", list1)
#inserting an element at a specific position
list1.insert(2, 10) 
print("After Inserting 10 at index 2:", list1)
#counting occurrences of an element
count_of_2 = list1.count(2) 
print("Count of element 2:", count_of_2)
#popping an element
popped_element = list1.pop()
print("Popped Element:", popped_element)
print("List after Popping an element:", list1)
#clearing the list
list1.clear()   
print("List after Clearing:", list1)