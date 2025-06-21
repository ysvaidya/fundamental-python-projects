def game_func():
    import random 

    guess_name = random.randint(0, 100)
    print(guess_name)
    count = 6
    while count >= 1:
        print(f"- Hey boy you have only {count} chances, so choose properly. ")
        choice = int(input("Your answer -:- "))
        if choice == guess_name:
            print("You got it!.", choice)
            break
        elif guess_name -10 <= choice <= guess_name + 10:
            print("Too close! Keep trying.")
            count -= 1
        elif choice >= guess_name:
            print("Too high!.")
            count -= 1
        elif choice <= guess_name:
            print("Too low!")
            count -= 1

def main():
    while True:
        print("""
Welcome to the Number Guessing Game you player.
        Task-   You are going to guess the number between 0 to 100. 
                Game will show the number after you win or loose or time-up.
""")
    
        choice = input("Want to play. (Y/n)")
        match choice:
            case "Y":
                game_func()
            case "y":
                game_func()
            case "n":
                break



if __name__ == "__main__":
    main()