age = 20
if age >= 18:
    print("You are eligible to vote")



num = 5
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")



marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")



num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print(a, "is the greatest")
elif b > a and b > c:
    print(b, "is the greatest")
else:
    print(c, "is the greatest")



age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Addition:", a + b)
elif op == "-":
    print("Subtraction:", a - b)
elif op == "*":
    print("Multiplication:", a * b)
elif op == "/":
    print("Division:", a / b)
else:
    print("Invalid operator")



n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial not possible")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial is:", fact)


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


