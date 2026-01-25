print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[_______]
*******************************************************************************
''')
print("Bienvenue à l'ile au trésor.")
print("Votre but est d'arriver à trouver le coffre au trésor.")
intersection = input("Vous arrivez à une intersection. Que faites-vous? Tapez <<droite>> pour tourner à droite, tapez <<gauche>> pour tourner à gauche.\n\r")

#intersection

if intersection == "gauche":
    print("Après un kilomètre de marche vous arrivez devant un château.")
    print("Vous êtes à la moitié du pont-levis quand vous vous demandez si c'est une bonne idée de rentrer dans le château.")
    chateau = input("Voulez-vous entrer? Tapez <<oui>> pour entrer, <<non>> pour revenir sur vos pas.\n\r")

#chateau

    code = 4
    guess = 0
    if chateau == "oui":
        print("Vous entrez dans le château.")
        print("À l'entrée, il y a un coffre fort de la taille d'un adulte")
        coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

        while coffre_fort <= 1 or coffre_fort >= 5:
            print("Vous avez écrit une réponse invalide. Retapez")
            coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))


        if code != coffre_fort:
            print("Mauvaise réponse. Un piège s'est ouvert en dessous de vos pieds et vous êtes TOMBÉS dans des pics d'aciers.")
            print("GAME OVER")

        else:
            print('''Bonne réponse!
Vous entrez dans la pièce et vous trouvez le trésor.
Bien joué!!!''')

    if chateau == "non":
            print('''En revenant sur vos pas vous vous retrouvez soudain dans un labyrinthe.
Une inscription est gravée sur le mur:
Qui qu'on que essayera de sortir de l'enceinte du chateau après y être entré,
se retrouvera coincé à tout jamais dans un labyrinthe sans fin...
GAME OVER''')


#réponse:

elif intersection == "droite":
    print("Vous entrez dans une forêt enchantée. ")
    print("Vous voyez des fées. ")
    fee = input('''Allez-vous leur parler.
Si vous voulez leur parlez tapez <<oui>>,
si vous voulez les espionner pour être sur de leur bonnes intentions tapez <<non>>.\n\r''')
    code = 4
    guess = 0
# fée réponse
    if fee == "oui":
        print("Après avoir parler avec les fées, et leur avoir expliqué ta mission, elles t'expliquèrent où trouver le coffre aux trésor.")
        print("Donc après vous être rendus aux château oû il a le coffre au trésor, vous entrez dans le château.")
        print("À l'entrée, il y a un coffre fort de la taille d'un adulte")
        coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

        while coffre_fort <= 1 or coffre_fort >= 5:
            print("Vous avez écrit une réponse invalide. Retapez")
            coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))
        if code != coffre_fort:
            print("Mauvaise réponse. Un piège s'est ouvert en dessous de vos pieds et vous êtes TOMBÉ dans des pics d'aciers.")
            print("GAME OVER")

        else:
            print('''Bonne réponse!
Vous entrez dans la pièce et vous trouvez le trésor.
Bien joué!!!''')

    elif fee == "non":
        print('''Malheureusement, pendant que vous êtiez en train de les espionners pour être sûr de leurs bonnes intentions, elles ont vu les buissons bouger.
        Donc croyant que vous êtiez une quelconque bête sauvage, elles vous on transformé en pousière. Ne sachant pas que vous vouliez seulement leurs parler.''')
    else:
        print("Vous avez écrit une réponse invalide. Retapez.")
        print("Vous entrez dans une forêt enchantée. ")
        print("Vous voyez des fées. ")
        fee = input('''Allez-vous leur parler.
            Si vous voulez leur parlez tapez <<oui>>,
            si vous voulez les espionner pour être sur de leur bonnes intentions tapez <<non>>.\n\r''')

else:
    print("Vous avez écrit une réponse invalide. Retapez.")
    print("Bienvenue à l'ile au trésor.")
    print("Votre but est d'arriver à trouver le coffre au trésor.")
    intersection = input("Vous arrivez à une intersection. Que faites-vous? Tapez <<droite>> pour tourner à droite, tapez <<gauche>> pour tourner à gauche.\n\r")
    if intersection == "gauche":
        print("Après un kilomètre de marche vous arrivez devant un château.")
        print(
            "Vous êtes à la moitié du pont-levis quand vous vous demandez si c'est une bonne idée de rentrer dans le château.")
        chateau = input("Voulez-vous entrer? Tapez <<oui>> pour entrer, <<non>> pour revenir sur vos pas.\n\r")

        # chateau

        code = 4
        guess = 0
        if chateau == "oui":
            print("Vous entrez dans le château.")
            print("À l'entrée, il y a un coffre fort de la taille d'un adult")
            coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

            while coffre_fort <= 1 or coffre_fort >= 5:
                print("Vous avez écrit une réponse invalide. Retapez")
                coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

            if code != coffre_fort:
                print(
                    "Mauvaise réponse. Un piège s'est ouvert en dessous de vos pieds et vous êtes TOMBÉ dans des pics d'aciers.")
                print("GAME OVER")

            else:
                print('''Bonne réponse!
Vous entrez dans la pièce et vous trouvez le trésor.
Bien joué!!!''')

        if chateau == "non":
                print('''En revenant sur vos pas vous vous retrouvez soudain dans un labyrinthe.
Une inscription est gravée sur le mur:
Qui quiconque essayera de sortir de l'enceinte du chateau après y être entré,
se retrouvera coincé à tout jamais dans un labyrinthe sans fin...
GAME OVER''')

    # réponse:

    elif intersection == "droite":
        print("Vous entrez dans une forêt enchantée. ")
        print("Vous voyez des fées. ")
        fee = input('''Allez-vous leur parler.
Si vous voulez leur parlez tapez <<oui>>,
si vous voulez les espionner pour être sur de leur bonnes intentions tapez <<non>>.\n\r''')
        code = 4
        guess = 0
        if fee == "oui":
            print("Après avoir parler avec les fées, et leur avoir expliqué ta mission, elles t'expliquèrent où trouver le coffre aux trésor.")
            print("Donc après vous être rendus aux château oû il a le coffre au trésor, vous entrez dans le château.")
            print("À l'entrée, il y a un coffre fort de la taille d'un adulte")
            coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

            while coffre_fort <= 1 or coffre_fort >= 5:
                print("Vous avez écrit une réponse invalide. Retapez")
                coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

            if coffre_fort != code:
                print("Mauvaise réponse. Un piège s'est ouvert en dessous de vos pieds et vous êtes TOMBÉ dans des pics d'aciers.")
                print("GAME OVER")

            else:
                print('''Bonne réponse!
Vous entrez dans la pièce et vous trouvez le trésor.
Bien joué!!!''')


        elif fee == "non":
            print('''Malheureusement, pendant que vous êtiez en train de les espionners pour être sûr de leurs bonnes intentions, elles ont vu les buissons bouger.
Donc croyant que vous êtiez une quelconque bête sauvage, elles vous on transformé en pousière. Ne sachant pas que vous vouliez seulement leurs parler.''')
        else:
            print("Vous avez écrit une réponse invalide. Retapez.")
            print("Vous entrez dans une forêt enchantée. ")
            print("Vous voyez des fées. ")
            fee = input('''Allez-vous leur parler.
Si vous voulez leur parlez tapez <<oui>>,
si vous voulez les espionner pour être sur de leur bonnes intentions tapez <<non>>.\n\r''')
            code = 4
            guess = 0
            if fee == "oui":
                print(
                    "Après avoir parler avec les fées, et leur avoir expliqué ta mission, elles t'expliquèrent où trouver le coffre aux trésor.")
                print(
                    "Donc après vous être rendus aux château oû il a le coffre au trésor et être entré, vous entrez dans le château.")
                print("À l'entrée, il y a un coffre fort de la taille d'un adulte")
                coffre_fort = input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r")

                while coffre_fort <= 1 or coffre_fort >= 5:
                    print("Vous avez écrit une réponse invalide. Retapez")
                    coffre_fort = int(input("Le code est un nombre de 1 à 5. Inscrivez votre réponse.\n\r"))

                if coffre_fort != code:
                    print(
                        "Mauvaise réponse. Un piège s'est ouvert en dessous de vos pieds et vous êtes TOMBÉS dans des pics d'aciers.")
                    print("GAME OVER")

                else:
                    print('''Bonne réponse!
Vous entrez dans la pièce et vous trouvez le trésor.
Bien joué!!!''')

