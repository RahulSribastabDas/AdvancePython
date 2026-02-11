#1)Create a set and print its elements
s = {1, 2, 3, 4, 5}
print(s)

#2) Add an element to a set
s = {1, 2, 3}
s.add(4)
print(s)

#3) Add multiple elements to a set
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)

#4) Remove an element using remove() and discard()
s = {1, 2, 3, 4}

s.remove(2)     # Error if not present
s.discard(5)    # No error if not present

print(s)

#5) Remove a random element from a set
s = {10, 20, 30, 40}
removed = s.pop()
print("Removed:", removed)
print(s)

#6) Find the union of two sets
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

#7) Find the intersection of two sets
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)

#8) Find the difference between two sets
a = {1, 2, 3}
b = {2, 4}

print(a - b)

#9) Find symmetric difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)

#10) Check whether one set is a subset of another
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))

#11) Check whether two sets are disjoint
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))

#12) Convert a list with duplicates into a set
lst = [1, 2, 2, 3, 4, 4]
s = set(lst)
print(s)

#13) Find common elements between two sets
a = {1, 2, 3}
b = {2, 3, 5}

print(a.intersection(b))

#14) Find elements present in first set but not in second
a = {1, 2, 3, 4}
b = {3, 4}

print(a.difference(b))

#15) Copy a set and clear the original set
s = {1, 2, 3}
copy_set = s.copy()

s.clear()

print("Original:", s)
print("Copy:", copy_set)

#16) Compare two sets for equality
a = {1, 2, 3}
b = {3, 2, 1}

print(a == b)

#17) Iterate through a set using loop
s = {10, 20, 30}

for item in s:
    print(item)

#18) Create a frozenset and explain its use
fs = frozenset([1, 2, 3, 4])
print(fs)

#19) Find unique vowels in a string using set
text = input("Enter a string: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

found = set()

for ch in text:
    if ch in vowels:
        found.add(ch)

print("Unique vowels:", found)

#20) Menu-driven program for set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

while True:
    print("\n1.Union\n2.Intersection\n3.Difference\n4.Symmetric Difference\n5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Union:", a | b)
    elif choice == 2:
        print("Intersection:", a & b)
    elif choice == 3:
        print("Difference (a-b):", a - b)
    elif choice == 4:
        print("Symmetric Difference:", a ^ b)
    elif choice == 5:
        break
    else:
        print("Invalid choice")