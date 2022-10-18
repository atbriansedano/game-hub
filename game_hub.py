from itertools import count
import random

def guessfunc():

    print("\n*------------------------------------------------------------------------*")
    print("|Welcome to Guess the Number!, pick a number from 1 to 10, you get 3 trys|")
    print("*------------------------------------------------------------------------*\n")
    randomizer = random.randint(1, 10)
    count = 0

    while True:
        
        guess = input("Your Guess: ")
        count += 1

        if guess.isdigit():
            guess = int(guess)
            if guess <= 0:
                print("\n0 is not a valid number, please pick a number from 1 to 10")
        else:
            print("\n'{}' is not a digit, try again".format(guess))
            guessfunc()
                
        if guess == randomizer:
            choice = input("\nWow, you got it! Want to play again? Y/N: ")
            if choice.lower() == "y":
                guessfunc()
            else:
                break
        else:
            if guess < randomizer:
                print("Oof! too low\n")
            elif guess > randomizer:
                print("Oof! too high\n")

            if count == 3:
                print("Number: {}".format(randomizer))
                choice = input("\nTough luck, all out of guesses, the number was {}! Play again? Y/N: ".format(randomizer))
                if choice.lower() == "y":
                    guessfunc()
                else:
                    break          


def rpc():
    print("\n|---------------------------------------------|")
    print("|Welcome to Rock, Paper, Scissors, lets begin!|")
    print("|---------------------------------------------|")

    count = 0
    wins = 0
    losses = 0

    win_print = ["Point goes to... HUMANITY!", "A critical blow to WALL-E... Point goes to the flesh bag",
    "Domo Arigato the point does not go to MR. Robato!"]

    loss_print = ["Looks like Androids do dream of electric sheep... Point goes to the replicants!",
    "Looks like Asimov forgot the fourth law of robotics... Winning! point goes to I-Robot",
    "1001101... Translation: Point goes to the OS"]

    weapon = ["rock", "paper", "scissors"]

    while True:
        count += 1
        print("\nReady? Round: {}\nROCK...PAPER...SCISSOOOORS!".format(count))
        choice = input("Choice: ")

        if choice.lower() not in weapon:
            print("Oops, {} is'nt a rock, paper or scissors, please try again.".format(choice))
            continue

        randomize = random.randint(0,2)
        computer_choice = weapon[randomize]
        print("Copmuter: {} - You: {}".format(computer_choice,choice))
            
        if choice.lower() == "rock" and computer_choice == "scissors":
            print(win_print[randomize])
            wins += 1

        elif choice.lower() == "paper" and computer_choice == "rock":
            print(win_print[randomize])
            wins += 1

        elif choice.lower() == "scissors" and computer_choice == "rock":
            print(win_print[randomize])
            wins += 1

        elif choice.lower() == computer_choice:
            print("A tie? ew...")

        else:
           print(loss_print[randomize])
           losses += 1
        
        if wins == 3:
            choice = input("Congradulations! the human race lives another day. Play again? Y/N: ")
            if choice.lower() == "y":
                rpc()
            else:
                break
        elif losses == 3:
            choice = input("Its Over! Singularity is now here, might as well give up... Try again? Y/N: ")
            if choice.lower() == "y":
                rpc()
            else:
                break
            

def quiz():

    questions = ["Is Java a type of OS?", "Which email service is owned by Microsoft?", 
    "What was Twitter’s original name?", "What year was the very first model of the iPhone released?",
    "What is often seen as the smallest unit of memory?", 
    "In what Tarantino movie does Samuel L. Jackson wear a suit?", 
    "What is Anakin Sky-Walker's alter ego?", "What Bethesda franchise is set in a nuclear dystopia?", 
    "How many bits is in a byte?", "What movie is set in the Overlook Hotel?"]

    answer = ["No", "Hotmail", "twttr", "2007", "kilobyte", 
    "Pulp Fiction", "Darth Vader", "Fallout", "8", "The Shining"]
    count = 0
    
    print("\n|--------------------------------|")
    print("|Welcome to the Quiz, lets begin!|")
    print("|--------------------------------|\n")

    for i in range(len(questions)):
        print("{}".format(questions[i]))
        user_answer = input("Answer: ")
        if user_answer.lower() == answer[i].lower():
            print("|--------|")
            print("|Correct!|")
            print("|--------|")
            count += 1
        else:
            print("|----------|")
            print("|Incorrect!|")
            print("|----------|")
        

    if count > 6:
        print("Congradulations! you have passed the test with a score of {}/10".format(count))
        play = input("Play again Y/N: ")
        if play.lower == 'y':
            quiz()
        else:
            exit
    else:
        print("Better luck next time! You scored {}/10".format(count))
        play = input("Play again Y/N: ")
        if play.lower() == 'y':
            quiz()
        else:
            exit


name = input("Welcome! Please enter your name: ")

answer = True
while answer:
    print("""
    Hello, {}! please choose an activity:

    1. Take a Quiz
    2. Play Rock, Paper, Scissors
    3. Guess the Number
    4. Tik Tak Toe
    5. Exit
    """.format(name))
    answer = input("Your choice: ")

    if answer == "1":
        quiz()
    elif answer == "2":
        rpc()
    elif answer == "3":
        guessfunc()
    elif answer == "4":
        print("4")
    elif answer == "5":
        break
    else:
        print("lets play tik tak toe!")

print("\nThank you for playing {}, Goodbye!".format(name))