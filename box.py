user_width = int(input("Width? "))
user_height = int(input("Height? "))

row = 0
column = 0

#To accomodate the first and last rows
user_height -= 2

#Print top row (all *)
print("*" * user_width)


while(row < user_height):
    print("*" + (" " * (user_width - 2)) + "*")
    row += 1

#Print last row (all *)
print("*" * user_width)
