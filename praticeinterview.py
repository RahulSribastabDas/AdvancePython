#loop programs
#Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


#Sum of first N numbers
n = int(input("Enter number: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum:", total)


#Multiplication table
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#Functions
#Function to add two numbers
def add(a, b):
    return a + b
print("Addition:", add(5, 3))
