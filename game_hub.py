def rpc():

    print("\n|---------------------------------------------|")
    print("|Welcome to Rock, Paper, Scissors, lets begin!|")
    print("|---------------------------------------------|")
            
   

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

#----------------------------------------------------------------------------------------------------------------
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
        print("Lets guees that number!")
    elif answer == "4":
        print("4")
    elif answer == "5":
        print("Thank you for playing {}, Goodbye!".format(name))
        exit
    else:
        print("lets play tik tak toe!")