import random

# dictionary of secrets and words
levels ={
    "Easy": [("apple", "a common red fruit that doctor shouldn't recommend"),
             ("dog", "now a days they are far more lovable to humans")],
    "Medium": [("python", "a snake and a programming language"),
               ("planet"," a large body in the space")],
    "Hard": [("alogorithm"," a step by step procedure to solve a problem"),
             ("dictionary","a data structure in python")]
}

# list of levels
level_order=("Easy","Medium","Hard")
# greet user
print("Welcome to the Word Guessing Game")
# chose difficulty level
print("Select difficulty level")
for i, level in enumerate(level_order,1):
    print(f"{i}. {level}")

choice= int(input("Enter level (1-3) "))
secret_word, hint = random.choice(levels[level_order[choice-1]])
guessed = []
attempts = 6
print(f"\n Hint: {hint}")
while attempts >0:
    display=''
    for ch in secret_word:
         if ch in guessed:
             display += ch
         else:
             display += '_'

    print("Word: ", display)
    if display == secret_word:
        print("You won!")
        break
    # now take the input after showing the current word state
    guess = input("Guess a letter: ").lower()
    #input validation
    if not guess.isalpha() or len(guess) !=1:
        print("Enter one letter only")
        continue

    if guess in guessed:
        print("Already guessed")
    else:
        guessed.append(guess)
        if guess not in secret_word:
            attempts -= 1
            print("Wrong")

    print(f"Attempts left: {attempts}\n")

if attempts ==0:
    print(f"you lost! the word was {secret_word}")
 
