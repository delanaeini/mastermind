import random


def generate_digits_list(): #generate mastermind list for user to guess
    digits_list = []
    for i in range(4):
        digits_list.append(random.randint(0,9))
    return digits_list


def mastermind_feedback(computer_digits, user_digits):
    feedback_list = []
    
    for i in range(len(computer_digits)):
        if user_digits[i] == computer_digits[i]:
            user_digits[i] = -1
            feedback_list.append("o")  #in the right place
            continue
        else:
            for j in range(len(user_digits)):
                if user_digits[j] == computer_digits[i]:
                    user_digits[j] = -1
                    feedback_list.append("x")  #at the wrong place
                    break
    random.shuffle(feedback_list) #randomize feedback, so the user doesn't see the feedback in the correct order of digits.
    return feedback_list


#directions of the game:
print("\x1B[1m \n====    Mastermind : The game's directions    ==== \n \x1B[0m")
print("\nThe computer has stored four random digits in its memory, and your job is to guess what they are.\n")
print("\nFor every digit that you guess right but is not in the correct position, you will get an 'x', and for every digit you guess right and it is in the correct position, you will get an 'o'.\n")
print("\nThe order of 'x's and 'o's will be random. You will not get a feedback for incorrect digits.\n")
print("\nYou can enter 'Q' to quit, or keep guessing until you get the digits (and their positions) right.\n")
print("\n\x1B[3mNote that the computer might have stored the same digit in multiple positions!\x1B[0m\n")
print("\n\nWelcome to the game!")


computer_digits = generate_digits_list()
feedback_list = []
num_tries = 0

while True:
    if feedback_list == ['o', 'o', 'o', 'o']:
        print("Good job!! You got it right!\n\n")
        break
    
    user_input = input("\nPlease enter four digits: ")
    if user_input == "q" or user_input == "Q":
        print("You have successfully left the game.")
        break

    elif not user_input.isnumeric() or len(user_input) != 4:
        print("Please only enter four digits")

    else:
        user_digits = list(map(int, user_input))
        feedback_list = mastermind_feedback(computer_digits, user_digits)
        for f in feedback_list: #formatting the feedback in a non-list way
            print(f, end=' ') 

        num_tries += 1
        print("\nThis was your try number", num_tries, ".")
        continue
