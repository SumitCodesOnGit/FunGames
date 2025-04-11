import random
# define the grid with tuples (row,column)
grid_positions=[(i,j) for i in range(1,4) for j in range(1,4)]
# randomly choose a treasure position
treasure_position=random.choice(grid_positions)
print(treasure_position) # to test
# dictionary to store hints for some positions
hints = {
    (1,1): "It's far from here!",
    (2,2): "Getting warmer!",
    (3,3): "Close enough!"
}
# list to track players's attempts
attempts=[]
print("Welcome to the Treasure Hunt!")
print("Guess the treasure location on 3*3 grid")

# for maxiumum 5 tries
for turn in range(5):
    guess = input(f"Attempt {turn+1}- Enter your guess as row,col (e.g, 2,3): ")
    try:
        row,col = map(int,guess.split(','))
        guess_tuple=(row,col)
        if guess_tuple not in grid_positions:
            print("Invalid position! Please choose row and column between 1 and 3")
            continue
        attempts.append(guess_tuple)
        if guess_tuple == treasure_position:
            print("Congratulations! you found the treasure!")
            break
        else:
            print("Oops! no treasure here!")
            if guess_tuple in hints:
                print("Hint:",hints[guess_tuple])
            else:
                print("No hints available for this spot")
    except:
        print("Invalid input, please enter number like 1,2")

else:
    print("Game over! You have used all your attempts")
    print("the treasure was at: ", treasure_position)

print("Your attempts: ", attempts)