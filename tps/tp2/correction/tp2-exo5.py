x = [4, 6, 8, 24, 12, 2]

def maxliste(x):
    i=len(x) - 1
    max=0
    while i >=0 :
        if x[i]>max:
            max=x[i]
        i -= 1
    return max
    

print("Le max de la liste est : %d" % maxliste(x))

x2 = [4, 6, 8, 24, 12, 2,123,45678823,8,9,0]
print("Le max de la liste est : %d" % maxliste(x2))