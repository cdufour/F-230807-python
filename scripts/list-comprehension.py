def square(n):
    return n * n

fruits = ["poire", "pomme", "banane", "kiwi", "mangue"]
newsList = [ x for x in fruits ]
print(newsList)

numbers = [3, 8, 40, 10, 8, 15]
#squares = [ x*x for x in numbers ]
squares = [ square(x) for x in numbers if x >= 10 ]
print(squares)