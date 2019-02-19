user_input = input("Countdown Starts at: ")
count = int(user_input)

if(count > 20):
    count = int(input("Number can not be larger than 20. Please enter another number: "))

while count > 0:
    print(count)
    count -= 1
