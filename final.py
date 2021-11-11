import time
import sys

A = ["a","A"]
B = ["b","B"]
yes = ["y", "Y", "yes", "si"]
no = ["n", "N", "no"]

constant = ("ONLY USE A or B!!!")
constant2 = ("Answer yes or no")
def start():
    print ("\nAfter a long night of partying and drinking soda with your buds "
    "You wake up in the middle of Ireton Lawn and that is when you see a hot chick "
    "running towards you. This is a weird scenerio because no chicks have ever ran towards you "
    "what will you do!?:")
    time.sleep(2)
    print("""    A. Ask the girl why is she running and ask if she needs help
    B. Throw a rock at her """)
    decision = input("--> ")
    if decision in B:
        option_rock_throw()
    elif decision in A:
        print("Turns out that the girl is a zombie and she ate your face and now you are a zombie!"
             "################################ GAME OVER ##################################### ")
        sys.exit(0)
    else:
        print (constant)
        start()

def option_rock_throw():
    print ("\nYou knock out the girl to realize that she is one of your classmates that you had a crush on "
    "so you decide to go check on her to realize that she is a zombie so you smash her head with "
    "a rock. Now you realize that there is a horde of zombies coming for you. What will you do!?:")
    time.sleep(2)
    print("""    A. run into the church and barricade yourself
    B. run to the dorms and look for help """)
    decision = input("--> ")
    if decision in A:
        option_church()
    elif decision in B:
        print("Turns out that the dorms are full of zombies and they overrun you and you die! "
             "################################ GAME OVER ##################################### ")
        sys.exit(0)
    else:
        print (constant)
        option_rock_throw()


def option_church():
    print ("\nYou run into the church and barricade yourlsef just to find the priest in the church! "
    "the priest is the first human you have encountered and he tells you that over night there was a "
    "zombie outbreak! He then asks you if you would like to try and escape! What will your choice be!?")
    time.sleep(2)
    print("""    Yes. You both will escape together!
    No. You hold your own in the church while the priest leaves. """)
    decision = input("--> ")
    if decision in yes:
        print("In a valiant effort you and the priest make a dash while taking out some zombies. You make it out of the college "
        "into the street and run, you and the priest make it to downtown to find that the entire city has been turned into undead. You and "
        "the priest try fighting for as long as possible but in the end it is too much and both of you get taken out. "
        "################################ GAME OVER #####################################")
        sys.exit(0)
    elif decision in no:
        option_church2()
    else:
        print (constant2)
        option_church()

def option_church2():
    print("\nOn his way out the priest has a change of heart that he cannot bear to leave you behind so he stays with you. After a day of camping out in the church you hear a noise coming from the roof of the church "
    "afraid that it might be a zombie you and the priest go up to check it out and it turns out to be an incoming helicoter that takes you and the priest and now you guys are safe!!!")
    time.sleep(2)
    print("\n Congratulations you have beat the game!")
    sys.exit(0)



start()
