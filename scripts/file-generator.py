students = ["Arthur", "Bastien", "Nathan", "Etienne"]
content = "Fichier appartenant à "

for s in students:
    # création d'un chemin de fichier
    filepath = "files/evaluation_" + s[:3].lower() + ".txt"
    f = open(filepath, "w")
    f.write(content + s)
    f.close()
    print("[+] file %s created" % filepath)