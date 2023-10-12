f = open("files/demo.txt", "r")
#print(type(f))
content = f.read()
f.close()

newContent = content.replace("demo", "test")

print(content)
print(newContent)

# écriture dans un fichier (append mode)
f2 = open("files/new.txt", "a")
f2.write(newContent + '\n')
f2.close()