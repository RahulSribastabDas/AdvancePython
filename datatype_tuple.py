# 1) Create a tuple and print its elements using loop.
t1 = (10, 20, 30, 40)
for item in t1:
    print(item)

# 2) Find the length of a tuple.
t2 = (1, 2, 3, 4, 5)
print("Length:", len(t2))

# 3) Find the maximum and minimum element in a numeric tuple.
t3 = (5, 2, 9, 1, 7)
print("Max:", max(t3))
print("Min:", min(t3))

# 4) Count how many times an element occurs in a tuple.
t4 = (1, 2, 2, 3, 2, 4)
print("Count of 2:", t4.count(2))

# 5) Find the index of a given element in a tuple.
t5 = (10, 20, 30, 40)
print("Index of 30:", t5.index(30))

# 6) Convert a list into a tuple and vice-versa.
lst = [1, 2, 3]
t6 = tuple(lst)
print("List to Tuple:", t6)
lst2 = list(t6)
print("Tuple to List:", lst2)

# 7) Check whether a tuple contains a specific value.
t7 = (10, 20, 30)
print(20 in t7)

# 8) Slice a tuple to get alternate elements.
t8 = (1, 2, 3, 4, 5, 6)
print("Alternate elements:", t8[::2])

# 9) Reverse a tuple without using reverse().
t9 = (1, 2, 3, 4)
print("Reversed:", t9[::-1])

# 10) Find the sum of all numeric elements in a tuple.
t10 = (10, 20, 30)
print("Sum:", sum(t10))

# 11) Remove duplicate elements from a tuple.
t11 = (1, 2, 2, 3, 4, 4)
t11_unique = tuple(set(t11))
print("Without duplicates:", t11_unique)

# 12) Create a tuple of squares for numbers 1 to 10.
t12 = tuple(i*i for i in range(1, 11))
print("Squares:", t12)

# 13) Unpack a tuple into multiple variables.
t13 = (10, 20, 30)
a, b, c = t13
print(a, b, c)

# 14) Find common elements between two tuples.
t14a = (1, 2, 3, 4)
t14b = (3, 4, 5, 6)
common = tuple(set(t14a) & set(t14b))
print("Common elements:", common)

# 15) Sort a tuple in ascending order.
t15 = (5, 2, 9, 1)
sorted_t15 = tuple(sorted(t15))
print("Sorted:", sorted_t15)

# 16) Create a nested tuple and access inner elements.
t16 = ((1, 2), (3, 4), (5, 6))
print("Inner element:", t16[1][0])  # 3

# 17) Check whether a tuple is palindrome.
t17 = (1, 2, 3, 2, 1)
print("Palindrome:", t17 == t17[::-1])

# 18) Replace an element in a tuple (hint: conversion).
t18 = (10, 20, 30)
lst18 = list(t18)
lst18[1] = 99
t18 = tuple(lst18)
print("After replace:", t18)

# 19) Merge two tuples without using +.
t19a = (1, 2, 3)
t19b = (4, 5, 6)
merged = tuple(list(t19a) + list(t19b))
print("Merged:", merged)

# 20) Write a program to find the second largest element in a tuple.
t20 = (10, 50, 20, 40, 30)
unique = list(set(t20))
unique.sort()
print("Second largest:", unique[-2])
