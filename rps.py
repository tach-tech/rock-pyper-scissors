# demander si le mec veut jouer 
# si il dit oui le faire jouer
# boucle, de jeux 
# Adverssaire décide avec un rand
# Si il dit non annuler la boucle et exit la boucle, le programme s'arrete 
import random

life = 3
point = 0

while True:
    print(life)
    e_choice = ["r", "p", "s"]
    choice = input("Que choisissez-vous ? (r , p ou s)")
    random.shuffle(e_choice)
    if choice == "r" and e_choice[0] == "r":
        print("Egalité !")
    elif choice == "r" and e_choice[0] == "p":
        life -= 1
        print(f"Perdu ! Il vous reste {life} vie(s)")
        if life == 0:
            print(f"Vous avez perdu ! Vous avez {point} point(s)")
            print("vous avez perdu un point")
            break
    elif choice == "r" and e_choice[0] == "s":
        point += 1
        print(f"Gagné ! Vous avez gagné un point ! ")
    if choice == "p" and e_choice[0] == "r":
        point += 1
        print(f"Gagné ! Vous avez gagné un point ! ")
    elif choice == "p" and e_choice[0] == "p":
        print("Egalité !")
    elif choice == "p" and e_choice[0] == "s":
        life -= 1
        print(f"Perdu ! Il vous reste {life} vie(s)")
        if life == 0:
            print(f"Vous avez perdu ! Vous avez {point} point(s)")
            print("vous avez perdu un point")
            break
    if choice == "s" and e_choice[0] == "r":
        life -= 1
        print(f"Perdu ! Il vous reste {life} vie(s)")
        if life == 0:
            print(f"Vous avez perdu ! Vous avez {point} point(s)")
            break
    elif choice == "s" and e_choice[0] == "p":
        point += 1
        print(f"Gagné ! Vous avez gagné un point ! ")
    elif choice == "s" and e_choice[0] == "s":
        print("Egalité !")
    else:
        print("Réessayez, je n'ai pas compris, tapez 'r' , 'p' ou 's'")
        

print("Au revoir !")