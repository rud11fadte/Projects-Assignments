print("hello")
a=5
b=9

def sum(x , y):
    return x + y

def diff(x , y):
    return x - y

def mul(x , y):
    return x * y

def div(x , y):
    return x / y

print(f"summation : {sum(a , b)}")
print(f"difference : {diff(a , b)}")
print(f"multiplication: {mul(a , b)}")
print(f"division : {div(a , b)}")

def sumNumbers(n):
    total = 0
    for num in range (1, n+1):
        total += num
    return total
print(f"sum of numbers in list : {sumNumbers(10)}")    

def factorial(n):
    product = 1
    for num in range (1, n+1):
        product *= num
    return product
print(f"factorial of number : {factorial(5)}")

def isodd(n):
    if n % 2 != 0:
        return True
    else:
        return False
print(f"is number odd : {isodd(7)}")

def sumeven(n):
    total = 0
    for num in range (1, n+1):
        if num % 2 == 0:
            total += num
    return total
print(f"sum of even numbers : {sumeven(10)}")

numbers=[15,20,45,10]
name="Dattadeep shetgaonkar"

print(numbers)
print(name)

def printList(lst):
    for item in lst:
        print(item,end=" | ")
printList(numbers)
print(" ")
printList(name)
print(" ")

def evenNumbers(lst):
    even_nums = []
    for num in lst:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
print(f"even numbers in list : {evenNumbers(numbers)}")

def sumevenInList(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total
print(f"sum of even numbers in list : {sumevenInList(numbers)}")





