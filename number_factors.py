user_number = int(input("Please enter a number: "))

factors_list = []

for i in range(1,user_number + 1):
    if(user_number%i == 0):
        factors_list.append(i)
    i += 1

print(factors_list)