coin_count = 0

more_coin = True
while(more_coin):

    print("You have %d coin(s)." % (coin_count))
    
    user_input = input("Do you want another? ")

    if(user_input.lower() == "yes"):
        coin_count += 1
    elif(user_input.lower() == "no"):
        print("Bye")
        more_coin = False
        exit()
