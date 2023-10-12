import os

if not os.path.exists("blabla"):
    os.mkdir("blabla")
    print("[+] blabla dir created")

'''
try:
    os.mkdir("blabla")
except FileExistsError:
    print("Cannot make directory")
    exit(6)
'''

# objectif: déplacer les fichiers .log dans le dossier files/logs
for f in os.listdir("files"):
    if f.endswith(".log"):
        os.rename("files/" + f, "files/logs/" + f)
        print("[+] file %s moved" % f)


print("*** The End ***")

