isEarthRound = False # variable bool

if isEarthRound:
    print("La terre est ronde")

message = "Deux est supérieur à un"

if 2 > 1:
    print(message)

condition = 2 > 1

if condition:
    print(message)

#n = 7
# version plus dynamique avec saisie utilisateur
n = int(input("Saisir le nombre de joueurs\n"))

sport = "foot"

if n >= 7:
    print("Assez nombreux pour joueur au", sport)
else:
    print("Nombre insuffisant pour un match de", sport)

# conditions multiples
if n >= 15:
    print("Ok pour rugby")
elif n > 10:
    print("Ok pour foot")
elif n > 5:
    print("Ok pour basket")
else:
    print("Ok pour tennis")


if n > 10:
    if n >= 15:
        print("Ok pour rugby")
    else:
        print("Ok pour foot")
    print("démo")
else:
    print("Ok pour basket et tennis")

