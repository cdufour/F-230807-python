def hello():
    print("Hello")

def hello2():
    return "Hello again !"

def addTwo(n):
    return n + 2

def square(n):
    return n * n

def sum(a, b):
    return a + b

# ----------------------------------
hello()
print(hello2())
print(addTwo(4)) # 6
finalValue = addTwo(addTwo(addTwo(5))) # 5 => 7 => 9 => 11
print(finalValue) # 11
print(square(5))
print(sum(4, 1) * sum(square(2), square(3))) # 5 * (4 + 9) => 65