def plusTen(a):
    return a + 10

x = lambda a: a + 10
y = lambda a,b: a+b

print(x(5))
print(plusTen(5))
print(y(3,8))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(4))