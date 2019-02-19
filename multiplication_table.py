first_multi = 1
second_multi = 1

while(first_multi < 11):
    while(second_multi < 11):
        print("%d X %d = %d" % (first_multi, second_multi, (first_multi*second_multi)))
        second_multi += 1
    
    first_multi += 1
    second_multi = 1