#1) Create a list and print all elements
lst = [10, 20, 30, 40, 50]

for item in lst:
    print(item)

#2) Find the sum of list elements
lst = [10, 20, 30, 40]
print("Sum:", sum(lst))

#3) Find the largest and smallest element
lst = [10, 5, 25, 2, 15]

print("Largest:", max(lst))
print("Smallest:", min(lst))

#4) Count even and odd numbers
lst = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in lst:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

#5) Remove duplicate elements
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print(unique)

#6) Reverse a list without using reverse()
lst = [1, 2, 3, 4, 5]
rev = lst[::-1]
print(rev)

#7) Find the second largest number
lst = [10, 20, 5, 40, 30]

lst2 = list(set(lst))
lst2.sort()
print("Second largest:", lst2[-2])

#8) Sort a list in ascending and descending order
lst = [5, 2, 9, 1]

print("Ascending:", sorted(lst))
print("Descending:", sorted(lst, reverse=True))

#9) Merge two lists without using +
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)

#10) Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = list(set(a) & set(b))
print(common)

#11) Count frequency of elements
lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print(freq)

#12) Separate positive and negative numbers
lst = [10, -5, 3, -2, 0, 7]

positive = []
negative = []

for num in lst:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("Positive:", positive)
print("Negative:", negative)

#13) Replace all negative numbers with 0
lst = [10, -5, 3, -2, 7]

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print(lst)

#14) Find the index of a given element
lst = [10, 20, 30, 40]
num = 30

print("Index:", lst.index(num))

#15) Create a list of squares using loop
squares = []

for i in range(1, 6):
    squares.append(i*i)

print(squares)

#16) Delete all even numbers from a list
lst = [1, 2, 3, 4, 5, 6]

lst = [num for num in lst if num % 2 != 0]
print(lst)

#17) Check whether a list is palindrome
lst = [1, 2, 3, 2, 1]

if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#18) Rotate list elements by K positions
lst = [1, 2, 3, 4, 5]
k = 2

rotated = lst[k:] + lst[:k]
print(rotated)

#19) Find all prime numbers in a list
lst = [2, 3, 4, 5, 6, 7, 8, 9]

primes = []

for num in lst:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("Prime numbers:", primes)

#20) Create a nested list and access inner elements
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested[0])      # First inner list
print(nested[1][2])   # Access 6
