# Variables primitives
temperature = 2
pi = 3.14
isEarthRound = True
training = "Initiation au langage Python"

# Affichage des types des variables
print("*** Types des variables ***")
print(temperature, type(temperature))
print(pi, type(pi))
print(isEarthRound, type(isEarthRound))
print(training, type(training))

"""
print(2+2)
print(temperature + temperature)
temperature = 2.5
print(temperature, type(temperature))
print(temperature + temperature, type(temperature + temperature))
"""

# Quelques opérations sur les variables
print("\n*** Quelques opérations sur les variables ***")
print(temperature + 10)
print(training + "3") # concaténation entre deux chaînes
print(pi + 10)
print(isEarthRound + 10) # conversion implicite de True en 1
print("Le double de pi est:", pi * 2)
print( "Le double de pi est: " + str(pi * 2) )

doublePi = pi * 2 # stockage en variable de la valeur retournée par l'expression arithmétique
print("doublePi", type(doublePi)) # float
doublePiStr = str(doublePi)
print("doublePiStr", type(doublePiStr))

c = '4'
print(2 + int(c)) # 6



