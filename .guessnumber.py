def ultimate_lol():
    import art

    import random

    def npc_number():
        return random.randint(1, 100)

    npc = npc_number()
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level_user = input("Choose a difficulty. Type 'easy' or 'hard'")

    def level_choice(level_user):
        if level_user == "easy":
            return 10
        else:
            return 5

    for turns in range(level_choice(level_user)):
        guess = int(input("What's your guess?: "))
        if guess > npc:
            print("Too high. Try again.")
            print("You have", (level_choice(level_user) - 1) - turns, "guesses left.")
            if level_choice(level_user) - 1 - turns == 0:
                print(f"{npc} was number choosen by PC")
                print("You lost, try to read the instructions if the number is low or too high")
        elif guess < npc:
            print("Too low. Try again.")
            print("You have", (level_choice(level_user) - 1) - turns, "guesses left.")
            if level_choice(level_user) - 1 - turns == 0:
                print(f"{npc} was number choosen by PC")
                print("You lost, try to read the instructions if the number is too low or too high")
        elif guess == npc:
            print("Great! You guessed it")
            print(print(f"{npc} was number choosen by PC. You stil have", (level_choice(level_user) - 1) - turns,
                        "guesses left."))
            break

    print("Thank you for playing!")


ultimate_lol()
