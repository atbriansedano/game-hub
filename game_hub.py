"""
Game Hub Application

This is a simple game hub application that allows you to choose
and play different types of games on teh python console. You can choose test your knowledge
by playing the trivia game, battle againts the machine in an intense
game of rock, paper, scissors, or you can try your luck with guess
the number

"""
__author__ = "Brain Sedano"
__contact__ = "atbriansedano@gmail.com"
__date__ = "2022/10/15"

from itertools import count
import random

#This function contains the code for the game guess the number
def guessfunc():

    print("\n*------------------------------------------------------------------------*")
    print("|Welcome to Guess the Number!, pick a number from 1 to 10, you get 3 trys|")
    print("*------------------------------------------------------------------------*\n")
    
    #this variable is going to contain the random number form 1 to 10 
    #that the user will need to guess
    randomizer = random.randint(1, 10)

    #This variable will keep track of the number of guesses through each iteration
    count = 0

    #While loop to iterate through the guesses
    while True:
        
        #Prompt for user input
        guess = input("Your Guess: ")
        count += 1

        #If and nested if statement to make sure user input is a non zero digit
        if guess.isdigit():
            guess = int(guess)
            if guess <= 0:
                print("\n0 is not a valid number, please pick a number from 1 to 10")
        else:
            print("\n'{}' is not a digit, try again".format(guess))
            guessfunc()

        #This if statement will verify fi the user has guessed thhe correct number        
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

            #This if statement will end the game if the use has not guessed the number
            #by the 3rd iteration
            if count == 3:
                print("Number: {}".format(randomizer))
                choice = input("\nTough luck, all out of guesses, the number was {}! Play again? Y/N: ".format(randomizer))
                if choice.lower() == "y":
                    guessfunc()
                else:
                    break
                break          

#This function contains the code for the game rock, paper, scissors
def rpc():
    print("\n|---------------------------------------------|")
    print("|Welcome to Rock, Paper, Scissors, lets begin!|")
    print("|---------------------------------------------|")

    #Variables to keep track of iterations, round wins and round losses
    count = 0
    wins = 0
    losses = 0

    #These lists contain custom phrases that will let the user know who won each round
    win_print = ["Point goes to... HUMANITY!", "A critical blow to WALL-E... Point goes to the flesh bag",
    "Domo Arigato the point does not go to MR. Robato!"]

    loss_print = ["Looks like Androids do dream of electric sheep... Point goes to the replicants!",
    "Looks like Asimov forgot the fourth law of robotics... Winning! point goes to I-Robot",
    "1001101... Translation: Point goes to the OS"]

    #This list contains the possible options the user cna pick from
    weapon = ["rock", "paper", "scissors"]

    #While loop to iterate through the game
    while True:

        #Tracking the number of rounds
        count += 1
        print("\nReady? Round: {}\nROCK...PAPER...SCISSOOOORS!".format(count))
        choice = input("Choice: ")

        #If statement to verify if the user input is amungst the available options
        if choice.lower() not in weapon:
            print("Oops, {} is'nt a rock, paper or scissors, please try again.".format(choice))
            continue
        
        #Variables that will be responsible for the computers random choice
        randomize = random.randint(0,2)
        computer_choice = weapon[randomize]
        print("Copmuter: {} - You: {}".format(computer_choice,choice))

        #if and elif statements that will keep track of the users victores 
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

        #if the user loses a round, a random loss statement will be choses formt the
        #loss phrases list
        else:
           print(loss_print[randomize])
           losses += 1
        
        #if the user wins 3 rounds then the game will end
        if wins == 3:
            choice = input("Congradulations! the human race lives another day. Play again? Y/N: ")
            if choice.lower() == "y":
                rpc()
            else:
                break
            break
        
        #if the user losses 3 times then the game will end
        elif losses == 3:
            choice = input("Its Over! Singularity is now here, might as well give up... Try again? Y/N: ")
            if choice.lower() == "y":
                rpc()
            else:
                break
            break
            
#This function contains the code for the trivia game
def quiz():

    #A list containing the trivias questions
    questions = ["Is Java a type of OS?", "Which email service is owned by Microsoft?", 
    "What was Twitter’s original name?", "What year was the very first model of the iPhone released?",
    "What is often seen as the smallest unit of memory?", 
    "In what Tarantino movie does Samuel L. Jackson wear a suit?", 
    "What is Anakin Sky-Walker's alter ego?", "What Bethesda franchise is set in a nuclear dystopia?", 
    "How many bits is in a byte?", "What movie is set in the Overlook Hotel?"]

    #A list containg the questions answers
    answer = ["No", "Hotmail", "twttr", "2007", "kilobyte", 
    "Pulp Fiction", "Darth Vader", "Fallout", "8", "The Shining"]

    #Variable to keep track of the trivia score
    count = 0
    
    print("\n|--------------------------------|")
    print("|Welcome to the Quiz, lets begin!|")
    print("|--------------------------------|\n")

    #for loop to iterate through the questions
    for i in range(len(questions)):
        
        #prints the questions form the list at index i
        print("{}".format(questions[i]))

        #Users input for the answer
        user_answer = input("Answer: ")

        #if the users answer coorilates with the index of the answer
        #which share the same index to the matching question, then the 
        #answer is correct

        if user_answer.lower() == answer[i].lower():
            print("|--------|")
            print("|Correct!|")
            print("|--------|")
            count += 1
        else:
            print("|----------|")
            print("|Incorrect!|")
            print("|----------|")
        
    #if the user manages to get more than 6 questions right, then the user will win the game
    if count > 6:
        print("Congradulations! you have passed the test with a score of {}/10".format(count))
        play = input("Play again Y/N: ")
        if play.lower() == 'y':
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

#This function is responsible for the main menu
def main():

    #prompt for users name
    name = input("Welcome! Please enter your name: ")

    #While loop to iterate the menu, prompts users to choose an game
    answer = True
    while answer:
        print("""
        Hello, {}! please choose an activity:

        1. Take a Quiz
        2. Play Rock, Paper, Scissors
        3. Guess the Number
        4. Exit
        """.format(name))
        answer = input("Your choice: ")

        #if statements that verify what the user chose
        #based on the answer the corrisponding function will be called
        if answer == "1":
            quiz()
        elif answer == "2":
            rpc()
        elif answer == "3":
            guessfunc()
        elif answer == "4":
            break
        else:
            print("ErrorL Invalid Input")

    print("\nThank you for playing {}, Goodbye!".format(name))

main()