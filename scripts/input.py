'''
print("Donne-moi ton âge")
age = input() # age sera obligatoirement str
# print("type(age)", type(age))
print("Tu as donc", age, "ans")
'''

print("Saisis un entier, je calcule son carré")
n = int(input())
square = n * n

# variante:
'''n = input()
square = int(n) * int(n)
print("Le carré de %s vaut %d" % (n, square))'''

print("Le carré de", n, "vaut", square)
print("Le carré de %d vaut %d" % (n, square))


test = input("Saisir qqch...\n")