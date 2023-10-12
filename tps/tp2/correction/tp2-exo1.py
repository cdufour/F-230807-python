# Fonction qui utilise une méthode sur les listes
def calculTVA(TVA):
    prices = [14,100,30,10,8]
    TTC = []
    for i in prices:
        TTC.append(i+(TVA/100)*i)
    return TTC

# Fonction qui utilise la comprehension de liste
def calculTVA2(TVA):
    prices = [14,100,30,10,8]
    TTC = [ i+(TVA/100)*i for i in prices ]
    return TTC

saisie = float(input("Taper la TVA : "))

print("Methode liste :")
print(calculTVA(saisie))
print("Comprehension liste :")
print(calculTVA2(saisie))