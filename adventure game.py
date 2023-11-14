def start_game():
    print("Welcome to the Bamboozled Adventure Game!")
    print("You find yourself in a perplexing maze of illusions.")
    print("There are three paths ahead: shimmering, shadowy, and misty.")
    direction = input("Which path will you choose? (shimmering/shadowy/misty): ").lower()

    if direction == "shimmering":
        go_shimmering()
    elif direction == "shadowy":
        go_shadowy()
    elif direction == "misty":
        go_misty()
    else:
        print("Invalid input. Please choose 'shimmering', 'shadowy', or 'misty'.")
        start_game()

def go_shimmering():
    print("\nYou chose the shimmering path.")
    print("You encounter a glowing orb emitting riddles.")
    print("Do you solve the riddles or ignore them?")
    action = input("What will you do? (solve/ignore): ").lower()

    if action == "solve":
        print("Congratulations! You solved the riddles and gained wisdom.")
        print("You proceed deeper into the maze.")
        print("You've successfully navigated the illusions!")
    elif action == "ignore":
        print("The orb fades away, leaving you lost in confusion.")
        print("Game Over!")
    else:
        print("Invalid input. Please choose 'solve' or 'ignore'.")
        go_shimmering()

def go_shadowy():
    print("\nYou chose the shadowy path.")
    print("You encounter an enigmatic figure offering a challenge.")
    print("Do you accept the challenge or avoid it?")
    choice = input("What will you do? (accept/avoid): ").lower()

    if choice == "accept":
        print("You faced the challenge and emerged victorious!")
        print("Congratulations! You've gained insight.")
        print("You navigate through the illusions.")
        print("You've successfully overcome the shadowy obstacles!")
    elif choice == "avoid":
        print("By avoiding the challenge, you get trapped in the shadows.")
        print("Game Over!")
    else:
        print("Invalid input. Please choose 'accept' or 'avoid'.")
        go_shadowy()

def go_misty():
    print("\nYou chose the misty path.")
    print("You encounter an alluring mirage of treasure.")
    print("Do you investigate the mirage or stay cautious?")
    decision = input("What will you do? (investigate/cautious): ").lower()

    if decision == "investigate":
        print("The mirage was an illusion! You fall into a trap.")
        print("Game Over!")
    elif decision == "cautious":
        print("Your cautious approach leads you safely through the mist.")
        print("Congratulations! You've outsmarted the illusions.")
        print("You successfully navigate the maze!")
    else:
        print("Invalid input. Please choose 'investigate' or 'cautious'.")
        go_misty()

# Start the Bamboozled adventure game
start_game()
