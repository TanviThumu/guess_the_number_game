import random

# Easy level function where the user has to guess a number between 1 and 10
def guess_easy_level():
    secret = random.randint(1, 10)  
    attempts = 0
    max_attempts = 3
    print("Should guess number between 1 to 10")
    print("You have 3 chances to guess the right number")
    while attempts < max_attempts:
        n = int(input("Enter your guess number: "))
        attempts += 1

 # Check if the guess is less than, greater than, or equal to the secret number
        if n < secret:
            print("Number is less than the secret number. Try again.")
        elif n > secret:
            print("Number is higher than the secret number. Try again.")
        else:
            print("Congratulations! You have guessed the right number!")
            break

# Check if maximum attempts are reached and offer to reveal the answer
        if attempts == max_attempts:
            print("Your attempts are completed. Please try again.")
            ans = input("Do you want to know the answer? (Yes/No)? ").lower()
            if ans == "yes":
                print(f"{secret} is the number you should have guessed.")
            break
        # Offer hint after 2 attempts
        if(attempts ==2):
            hint=input("Need any hint?? (Yes/No)").lower()
            if(hint == "yes"):
                if secret%2 == 0:
                    print("Hint: The number is even")
                else:
                    print("Hint: The number is odd")
            elif(hint=="no"):
                print("No hint")
            else:
                print("Invalid choice.")

# Medium level function where the user has to guess a number between 1 and 50
def guess_medium_level():
    secret = random.randint(1, 50)  
    attempts = 0
    max_attempts = 6
    print("Should guess number between 1 to 50")
    print("You have 6 chances to guess the right number")
    while attempts < max_attempts:
        n = int(input("Enter your guess number: "))
        attempts += 1

# Check if the guess is less than, greater than, or equal to the secret number
        if n < secret:
            print("Number is less than the secret number. Try again.")
        elif n > secret:
            print("Number is higher than the secret number. Try again.")
        else:
            print("Congratulations! You have guessed the right number!")
            break

# Check if maximum attempts are reached and offer to reveal the answer
        if attempts == max_attempts:
            print("Your attempts are completed. Please try again.")
            ans = input("Do you want to know the answer? (Yes/No)? ").lower()
            if ans == "yes":
                print(f"{secret} is the number you should have guessed.")
            break
        # Offer hint after 4 attempts
        if(attempts ==4):
            hint=input("Need any hint?? (Yes/No)").lower()
            if(hint == "yes"):
                if secret%2 == 0:
                    print("Hint: The number is even.")
                else:
                    print(" Hint: The number is odd")
            elif(hint=="no"):
                print("No hint")
            else:
                print("Invalid choice.")
    
# High level function where the user has to guess a number between 1 and 100
def guess_high_level():
    secret = random.randint(1, 100)  
    attempts = 0
    max_attempts = 10
    print("Should guess number between 1 to 100")
    print("You have 10 chances to guess the right number")
    while attempts < max_attempts:
        n = int(input("Enter your guess number: "))
        attempts += 1

# Check if the guess is less than, greater than, or equal to the secret number
        if n < secret:
            print("Number is less than the secret number. Try again.")
        elif n > secret:
            print("Number is higher than the secret number. Try again.")
        else:
            print("Congratulations! You have guessed the right number!")
            break

# Check if maximum attempts are reached and offer to reveal the answer
        if attempts == max_attempts:
            print("Your attempts are completed. Please try again.")
            ans = input("Do you want to know the answer? (Yes/No)? ").lower()
            if ans == "yes":
                print(f"{secret} is the number you should have guessed.")
            break
        # Offer divisibility hints after 7 attempts
        if(attempts ==7):
            hint_choice=input("Need any hint?? (Yes/No)").lower()
            if(hint_choice == "yes"):
                div = hint(secret)
                for divisor in range(2, 11):
                    status = "is" if div[divisor] else "is not"
                    print(f"The secret number {status} divisible by {divisor}.")
            if(hint=="no"):
                print("No hint")
            else:
                print("Invalid choice.")

# Hint function provides divisibility checks for the high-level mode
def hint(secret):
    result = {}
    #Divisibility check of 2
    result[2] = secret % 2 == 0

    #Divisibility check of 3
    digit_sum = sum(int(digit) for digit in str(secret))
    result[3] = digit_sum % 3 == 0

    #Divisibility check of 4
    last_two = int(str(secret)[-2:]) if len(str(secret)) > 1 else secret
    result[4] = last_two % 4 == 0

    #Divisibility check of 5
    last_digit = int(str(secret)[-1])  
    result[5] = last_digit in (0, 5)

    #Divisibility check of 6
    result[6] = result[2] and result[3]

    #Divisibility check of 7
    result[7] = secret % 7 == 0

    #Divisibility check of 8
    last_three = int(str(secret)[-3:]) if len(str(secret)) > 2 else secret
    result[8] = last_three % 8 == 0

    #Divisibility check of 9
    result[9] = digit_sum % 9 == 0

    #Divisibility check of 10
    result[10] = last_digit == 0

    return result

#User selects difficulty level
def game():
    choice = input("Select your choice as:\n1. Easy level\n2. Medium level\n3. High level\n").lower()
    if choice == "1" or choice == "easy level":
        guess_easy_level()
    elif choice == "2" or choice == "medium level":
        guess_medium_level()
    elif choice == "3" or choice=="high level":
        guess_high_level()
    else:
        print("Invalid choice. Please enter you input as 1 or 2 or 3 (or) enter your input as Easy level or Medium level or High level.")
    
    again = input("Do you want to play again? (Yes/No): ").lower()
    if again == "yes":
        game()           # Restart the game
    elif again == "no":
        print("Hope you enjoyed the game. Thank you!")     # Exit the game
    else:
        print("Invalid input.")
        choice()   # Handle invalid input

game()