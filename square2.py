user_input = input("How big is the square? ")
try:
    user_input = int(user_input)
except:
    pass

star_string = ""
star_column = ""

row = 0
column = 0


while(row < user_input):
    while(column < user_input):
        star_column += "*"
        column += 1

    star_string += star_column + "\n"
    row += 1

print(star_string)