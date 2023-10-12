d = {}
print(type(d))

student1 = {
    "age": 25,
    "lastname": "PASCAL",
    "firstname": "Blaise",
    "isGood": True,
    "grades": [17, 12, 19.5]
}

student2 = {
    "age": 36,
    "lastname": "DEL PIERO",
    "firstname": "Alessandro",
    "isGood": False,
    "grades": [10, 10, 10]
}

student3 = {
    "age": 58,
    "lastname": "TOURGUE",
    "firstname": "Ivan",
    "isGood": True,
    "grades": [19, 7.5, 2.5]
}

print(student1)

# affichage de la première note obtenue par student1
print("Première de note de student1:", student1["grades"][0])

# itération sur les clés d'un dict
for k in student1:
    print(f"{k} => {student1[k]}")

# python permet d'"unpack" les clés dict (technique assez inutilisée)
#a,b,c,d,e = student1
#print(e, student1[e])

# liste de dict
students = [student1, student2, student3]

evaluation = "bon"
for s in students:
    if not s["isGood"]:
        evaluation = "mauvais"
    else:
        evaluation = "bon"
    print("%s est un %s étudiant" % ( s["firstname"], evaluation ))