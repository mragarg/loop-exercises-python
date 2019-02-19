star_string = ""
star_column = ""

row = 0
column = 0


while(row < 5):
    while(column < 5):
        star_column += "*"
        column += 1

    star_string += star_column + "\n"
    row += 1

print(star_string)