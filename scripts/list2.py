postCodes = [
   67200, 75012, 68520, 15000, 75020,
   67200, 75012, 68520, 15000, 75020, 
   67275, 75012, 68520, 17750, 75020, 
   75007, 75012, 68520, 75001, 75020 
]

# Combien de code postaux parisiens ?

numParis = 0 # accu

for postCode in postCodes:

    # approche 1
    #if postCode >= 75000 and postCode <= 75999:
    #    numParis += 1

    # approche 2 - chaîne de caractères ("commence par")
    postCodeStr = str(postCode)
    dpt = postCodeStr[:2] # slicing, obtention des deux premiers caractères
    if dpt == "75":
        numParis += 1


print("Nombre de codes postaux parisiens", numParis)