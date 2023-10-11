import random

# random version (between 1 and 10)
SECRET=random.randint(1,10)
answer=""

# infinite loop
while True:
    answer = int(input("Devine mon chiffre secret : "))

    if answer == SECRET:
        break

    if answer>SECRET:
        print("Mon chiffre est plus petit")
    else:
        print("Mon chiffre est plus grand")


# executed after loop breaking
print("Bravo ! Le chiffre secret à deviner était bien "+str(SECRET))