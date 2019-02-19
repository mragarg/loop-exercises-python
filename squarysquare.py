num_of_lines = int(input("How big is the square? "))

def Squarysquare(numb):
    lines = 0
    result_string = ""
    while lines < numb:
        lines += 1
        result_string += ("*" * numb) + "\n"
    return result_string.rstrip()


print(Squarysquare(num_of_lines))