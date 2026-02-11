# 1) Print numbers from 1 to 10 using a loop.
for i in range(1, 11):
    print(i)

# 2) Print even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3) Print the sum of first N natural numbers.
n = int(input("Enter N: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print("Sum:", sum_n)

# 4) Print the multiplication table of a given number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 5) Count the number of digits in a given number.
num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Digits:", count)

# 6) Reverse a number using a while loop.
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)

# 7) Find the factorial of a number.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# 8) Print all prime numbers between 1 and 50.
for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# 9) Check whether a number is prime or not.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 10) Find the sum of digits of a number.
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)

# 11) Print Fibonacci series up to N terms.
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 12) Print all Armstrong numbers between 100 and 1000.
for num in range(100, 1000):
    temp = num
    sum_cube = 0
    while temp > 0:
        digit = temp % 10
        sum_cube += digit ** 3
        temp //= 10
    if num == sum_cube:
        print(num)

# 13) Find the product of digits of a number.
num = int(input("Enter a number: "))
product = 1
while num > 0:
    product *= num % 10
    num //= 10
print("Product:", product)

# 14) Print pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
    print("*" * i)

# 15) Find the largest element in a list using loop.
lst = [10, 25, 5, 40, 15]
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("Largest:", largest)

# 16) Count how many even and odd numbers are in a list.
lst = [1, 2, 3, 4, 5, 6]
even = odd = 0
for num in lst:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

# 17) Print numbers from 1 to 100 skipping multiples of 5.
for i in range(1, 101):
    if i % 5 != 0:
        print(i)

# 18) Calculate power of a number without using **.
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result *= base
print("Power:", result)

# 19) Find the GCD of two numbers using loop.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print("GCD:", gcd)

# 20) Print a number pyramid
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
