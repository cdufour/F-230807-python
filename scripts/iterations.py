'''
Objectif: afficher 5 fois "Bonjour"

Solution 1
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
print("Bonjour")
'''

# Solution 1, boucle while
count = 1
while count <= 5:
    print("Bonjour")
    count += 1 # incrémentation de 1

count2 = 5
while count2 > 0:
    print("Bye", count2)
    count2 -= 1 # décrémentation de 1

# Solution 3, for..in..range
for n in range(100):
    print("Coucou", n)
    # sortie de boucle prématurée
    if n == 4:
        break

