import random
import os

FILE_NAME = "NumGuesser_Rec.txt"

def read_game_records():
    """Read existing records from the file and return them as a list of tuples."""
    if not os.path.exists(FILE_NAME):
        return []
    
    records = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 4:
                records.append((int(parts[0]), parts[1], int(parts[2]), int(parts[3])))
    return records

def write_game_record(serial_number, username, score, rank):
    """Append a new record to the file."""
    with open(FILE_NAME, "a") as file:
        file.write(f"{serial_number}, {username}, {score}, {rank}\n")

""" def calculate_rank(records, new_score):
    Calculate the rank based on the current scores in the records.
    scores = [record[2] for record in records]
    scores.append(new_score)
    scores.sort(reverse=True)
    return scores.index(new_score) + 1 """


def user_guess():
    print("Welcome to NumGuesser.IO!\nYou have 7 attempts to guess the Secret Number!\nLet the game begin!")
    
    # Difficulty Selection
    while True:
        print("\nChoose your difficulty level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-100)")
        print("3. Hard (1-1000)")
        print("4. Nightmare (1-10000)")
        try:
            difficulty_level = int(input("Enter your choice (1-4): "))
            if difficulty_level == 1:
                start_num, end_num = 1, 10
            elif difficulty_level == 2:
                start_num, end_num = 1, 100
            elif difficulty_level == 3:
                start_num, end_num = 1, 1000
            elif difficulty_level == 4:
                start_num, end_num = 1, 10000
            else:
                print("Invalid choice. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Secret Number and Game Loop
    secret_number = random.randint(start_num, end_num)
    attempts = 0

    while attempts < 7:
        try:
            guess = int(input(f"Attempt {attempts + 1}/7: Guess a number between {start_num} and {end_num}: "))
            if guess < start_num or guess > end_num:
                print("Out of range! Try again.")
            elif guess == secret_number:
                print(f"Congratulations! You guessed the secret number in {attempts + 1} attempts!")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Game Over! You've used all attempts.")
    print(f"The secret number was {secret_number}.")

def bot_plays():
    print("Welcome to NumGuesser.IO! I am Xaiver_AI, your opponent.")
    print("You will guide me (H for High, L for Low, C for Correct) while I try to guess your number. Let's start!")
    
    low, high = 1, int(input("Enter the range for the game (1 to ?): "))
    attempts = 0

    while True:
        guess = random.randint(low, high)
        print(f"My guess is {guess}. Your Feedback Time!")
        feedback = input("Guide me (H/L/C): ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            if attempts == 0:
                print("Wow! I guessed it in the first attempt!")
            elif attempts == 1:
                print("I guessed it in the second attempt!")
            elif attempts == 2:
                print("I guessed it in the third attempt!")
            elif attempts == 3:
                print("I guessed it in the fourth attempt!")
            elif attempts == 4:
                print("I guessed it in the fifth attempt!")
            elif attempts == 5:
                print("I guessed it in the sixth attempt!")
            elif attempts == 6:
                print("I guessed it in the seventh attempt!")
                print(f"Congratulations {username}! You lost AHHAHHAHAHAHAH!")
            break
        else:
            print("Invalid input. Please input H, L, or C.")
            continue

        if low > high:
            print("Something went wrong. Check your inputs!")
            break
        
        # attempts += 1

# Main Program
if __name__ == "__main__":
    username = input("Enter your username to play: ")
    print(f"Hello {username}, Welcome to NumGuesser.IO !")

    while True:
        print("\nChoose a Game Mode to play: ")
        print("1. You guess the number.")
        print("2. Bot guesses the number.")
        
        try:
            mode = int(input("Enter 1 or 2: "))
            if mode == 1:
                user_guess()
            elif mode == 2:
                bot_plays()
            else:
                print("Invalid choice. Please enter 1 or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            continue

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing NumGuesser.IO! Goodbye!")
            break

#write_game_record(serial_number, username, score, rank)
write_game_record(1, "UnExplainableFish52", 100, 1)

#could not implement the score calculation and ranking system as the code was not working as expected.
#could have controlled the game loop to handle more complex scenarios and better game conclusion.

















################################################################
#Previous raw code 
# NumGuesser.IO 

# import random

# global  username
# username = "UnExplainableFish52"
# username = input("Enter your username to play!!")
# global start_num , end_num , attempts

# ch = int(input("Choose Game Mode: 1 or 2"))
# match ch:
#     case 1:
#         def user_guess():
#             print("Welcome to NumGuesser.IO!\n You have 7 attempts to guess the Secret Number!!\nLet the game begin!!!")
#             level_selection = True
#             while level_selection == True:
#                 print("\nChoose your difficulty level:")
#                 print("1. Easy (1-10)")
#                 print("2. Medium (1-100)")
#                 print("3. Hard (1-1000)")
#                 print("4. Nightmare (1-10000)")
#                 try:
#                     difficulty_level = int(input("Enter your choice (1-4): "))
#                     if difficulty_level == 1:
#                         print("You chose level 1")
#                         start_num = 1
#                         end_num = 10
#                         level_selection = False
#                     elif difficulty_level == 2:
#                         print("You chose level 2")
#                         start_num = 1
#                         end_num = 100
#                         level_selection = False
#                     elif difficulty_level == 3:
#                         print("You chose level 3")
#                         start_num = 1
#                         end_num = 1000
#                         level_selection = False
#                     elif difficulty_level == 4:
#                         print("So, You chose DEATH!?? huh?")
#                         start_num = 1
#                         end_num = 10000
#                         level_selection = False
#                     else:
#                         print("Invalid choice. Please try again!!  ")
#                 except TypeError:
#                         print('Enter a valid integer please!! ')
#                         continue
#                 except ValueError:
#                     print('Enter a valid integer please!! ')
#                     continue
#             secret_number = random.randint(start_num, end_num)
#         #game loop
#             attempts = 0
#             score = 0
#             while attempts < 7:
#                 try:
#                     attempts
#                     score
#                     guess = int(input(f"You have {7-attempts} attempts left. Guess a number between {start_num} and {end_num}: "))
#                     if guess < start_num or guess > end_num:
#                         print("Number out of range. Please try again!!")
#                         attempts += 1
#                         continue
#                     elif guess == secret_number:
#                         print("Congratulations! You guessed the secret number!!")
#                         if attempts <=3:
#                             print(f"You did it in {attempts} attempts!")
#                             score += 100 - attempts * 10
#                             print(f"Congratulations!! You just scored {100-attempts*10} points")
#                         return score
#                     else:
#                         if guess < secret_number:
#                             print("Too low! Try again!!")
#                         else:
#                             print("Too high! Try again!!")
#                         attempts += 1
#                 except TypeError:
#                     print('Enter a valid integer please!! ')
#                     continue
#                 except ValueError:
#                     print('Enter a valid VALUE please!! ')
#                     continue
#             print("Game Over!! You ran out of attempts!!")
#             print("Game Records Saved successfully!")
# #----------------------------------------------------------------
# #apply logics to start the game

# #----------------------------------------------------------------
#     case 2:
#         def bot_plays(x):
#             print(f"Greetings Mortal {username}! Welcome to NumGuesser.IO")
#             print("I am Xaiver_AI amd it is my pleasure to make your acquaintance!")
#             # print("I will be your guide through the NumGuesser.IO game.")
#             print("You will offer me hints and I will make my best guess to win the game!")
#             print("The game will end after you have answered 10 questions.")
#             print("Input H/h or L/l only while guiding !!")
#             print("Mortal!! I want you to give your best, Good luck!!")
#             high = x
#             low = 1
#             rem = " "
#             while rem != "c":
#                 if low != high:
#                     guess = random.randint(low,high)
#                 else:
#                     guess = low 
#                 rem = input(f"My guess is {guess} , Guide me!! : ").lower()
#                 if rem == "h":
#                     high = guess - 1 
#                 elif rem == "l":
#                     low = guess + 1
#                 else:
#                     print("Invalid input. Please input H/h or L/l only.")
#                     continue
#                 attempts += 1
#         print("Xaiver_AI Scored !!! !")
#         print(f"Congratulations!! You just scored {100-{attempts}*10} points")