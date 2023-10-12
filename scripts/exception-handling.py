try:
    #print(toto) # NameError
    [1,2,3][3]
except NameError:
    print("Problème de nom")
#except IndexError:
#    print("Problème d'index")
except:
    print("Erreur")
    