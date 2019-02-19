triangle_height = 5
total_space = 2 * triangle_height - 2

# #This for loop is for the rows
# for i in range(0, triangle_height):

#     #This for-loop prints the spaces before the *
#     for j in range(0, total_space):
#         print(end=" ")

#     total_space -= 1

#     #This for loop is used to print the *
#     for j in range(0, i+1):
#         print("* ", end="")

#     print(" ")

row = 0
while(row < triangle_height):
    space = triangle_height - row - 1 #Number of spaces before *
    while(space > 0):
        print(end=" ") #Used end= because it prevents \n
        space -= 1 
    star = row + 1 #how many stars do we need per row
    while(star > 0):
        print("*", end=" ")
        star -= 1 
    row += 1 #Goes to the next row
    print() #After printing a row, this helps us go to next line
