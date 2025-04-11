import random
# dictionary of countries and their capitals
countries={
    "India": "New Delhi",
    "China": "Bejieng",
    "Japan": "Tokyo",
    "Iran": "Tehran",
    "France": "Paris",
    "Brazil": "Brasilia",
    "Australia":"Canberra",
    "England":"London"
}
# convert the dict keys into list to pick random countries
country_list = list(countries.keys())
# track attempts using a list of tuples
attempts=[]
print("Welcome to the capital City Quiz")
print("You have 3 attempts to guess the capital of a randonly chosen country. \n")
# randomly select a country
selected_country=random.choice(country_list)
correct_capital=countries[selected_country]
# logic section
for attempt in range(3):
    guess=input(f"Attempt {attempt+1}: What is the capital of {selected_country}?").strip()
    attempts.append((selected_country,guess))
    if guess.lower()==correct_capital.lower():
        print("Correct! Well done")
        break
    else:
        print("Wrong Answer.")

        

print(attempts)
print("Your guesses were: ")
for i, (country,guessed_capital) in enumerate(attempts,1):
    print(f"{i}. you guessed {guessed_capital} for {country}")



