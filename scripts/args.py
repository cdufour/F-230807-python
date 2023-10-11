import sys

# affiche tous les arguments (type list) fournis en ligne de commande
print(sys.argv)

# affiche le premier argument "utile"
print(sys.argv[1])

# affiche le carré du premier argument
arg1 = int(sys.argv[1])
print(arg1 * arg1)