student1 = {
    "age": 25,
    "lastname": "PASCAL",
    "firstname": "Blaise",
    "isGood": True
}

print(student1)

# ajout d'une clé/valeur
student1["grades"] = [17, 12, 19.5]
print(student1)

# modification d'une valeur
student1["age"] = 27
print(student1)

# modification multiple
student1.update({ "age": 22, "firstname": "Blaisou", "demo": "demo" })
print(student1)

# suppression d'une clé
student1.pop("demo")
print(student1)

# itération sur les valeurs de student1
print("-----------------------------")
for v in student1.values():
    print(v)

# itération sur les clés de student1
print("-----------------------------")
for k in student1.keys():
    print(k)

# itération sur les clés et les valeurs de student1
print("-----------------------------")
for k,v in student1.items():
    print(k, v)

