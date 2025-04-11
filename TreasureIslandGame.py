def treasure_island_game():
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure")

    locations={
        "start": ("You are at a crossroad. Where do you want to go? (left/right): ",["left","right"]),
        "lake": ("You came to a lake. Dp you want to swim or wait? (swim/wait): ",["swim","wait"]),
        "cabin":("You arrive at a mysterious cabin with 3 doors. One red, one blue and one yellow."
        "Which one do you chose? (red/blue/yellow): ",["red","blue","yellow"])
    }  
    outcomes= {
        "left": "You chose to go left. Good choice, you are still alive.",
        "red": "It's a room full of fire. Game Over!",
        "blue": "You enter a room of beasts. Game Over!",
        "yellow": "You found the treasure! You won",
        "swim": "You got attacked by a crocodile. Game over!",
        "right": "You fell into a hole. Game Over!",
        "wait": "A boat arrives and takes you safely to island"
    }
    choice1=input(locations["start"][0]).lower()
    if choice1 not in locations["start"][1]:
        print("Invalid choice. Game Over!")
        return
    if choice1== "right":
        print(outcomes["right"])
        return
    else:
        print(outcomes["left"])

    choice2= input(locations["lake"][0]).lower()
    if choice2 not in locations["lake"][1]:
        print("Invalid Choice. Game Over!")
        return
    if choice2 == "swim":
        print(outcomes["swim"])
        return
    else:
        print(outcomes["wait"])

    choice3= input(locations["cabin"][0]).lower()
    if choice3 in locations["cabin"][1]:
        print(outcomes[choice3])
    else:
        print("You chose a door that doesn't exist. Game Over!")


# run the game
treasure_island_game()  