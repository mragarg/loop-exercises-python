secret_number = 5

print("I am thinking of a number between 1 and 10.")

while(True):
    user_input = input("What's the number? ")
    try:
        user_input = int(user_input)
        break
    except:
        print("You did not type a number. Try again.")

guess_count = 5
while(guess_count > 0):        
    if(user_input == secret_number):
        print("Yes! You Win!")
        guess_count = 1
        break
    elif(user_input > secret_number):
        print("%d is too high, try again." % user_input)
    else:
        print("%d is too low, try again." % user_input)
    guess_count -= 1
    print("You have %d guess(es) left." % (guess_count))
    if(guess_count == 0):
        play_again = input("Do you want to play again (Y or N)? ").upper()
        if(play_again == "Y"):
            guess_count = 5
        else:
            exit()
    user_input = int(input("What's the number? "))