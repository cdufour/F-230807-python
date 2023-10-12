#import utils
from utils import sumList as suml

values = []
while True:
    userInput = int(input("Saisir un chiffre (0 pour quitter le programme):"))
    if userInput == 0:
        break
    else:
        values.append(userInput) # ajout de la valeur saisie à la liste des valeurs

# exemple de chaînage de méthodes str
valuesFormatted = str(values).replace('[', '(').replace(']', ')')

#print("Sommes des valeurs saisies:", utils.sumList(values))
print("Sommes des valeurs saisies:", suml(values), valuesFormatted)
