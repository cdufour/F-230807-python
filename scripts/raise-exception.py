#raise Exception("blaba")

def check(x):
    if x < 0:
        #print("x est négatif")
        raise Exception("Negative number forbidden")

try:
    check(-4)
except:
    print("Problème")