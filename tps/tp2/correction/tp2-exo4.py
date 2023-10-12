sample_dict = {'a': 100, 'b': 200, 'c': 300}

print("valeur a verifier")
val = int(input())
valFound = False

'''
for n in sample_dict:
    if sample_dict[n] == val:
        print(str(val)+" est present à la clé "+ str(n))
        valFound = True
        break

if not valFound:
    print(str(val)+" non present")
'''

# variante
if val in sample_dict.values():
    print(f"{val} present in dict")