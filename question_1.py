#question 1 task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!") 

#question 1 task 2 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    cave_action = input("Do you want to light a torch, or proceed in the dark? ")
    if cave_action =="light a torch":
        print("You light a torch and proceed into the cave and you find hidden treasure!")
    else:
        print("You dont light a torch and proceed into the cave stumbling around in the dark.")

#quesion 1 task 3 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    cave_action = input("Do you want to light a torch, or proceed in the dark? ")
    if cave_action =="light a torch":
        print("You light a torch and proceed into the cave and you find hidden treasure!")
    else:
        print("You dont light a torch and proceed into the cave stumbling around in the dark.")
else:
    pass