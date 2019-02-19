#Ability ot print how text that is surrounded by stars (*)

#Prompts user for the text to be within the banner
banner_text = input("Text? ")

#Sets the width and height to accomodate the user's text
user_width = len(banner_text) + 4
user_height = 3

row = 0
column = 0

#To accomodate the first and last rows
user_height -= 2

#Print top row (all *)
print("*" * user_width)


while(row < user_height):
    print("* " + (banner_text) + " *")
    row += 1

#Print last row (all *)
print("*" * user_width)
