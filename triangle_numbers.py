#Print First 100 Triangle Numbers
count = 1
while(count <= 100):
    triangle_number = count * (count + 1)/2
    print("%d" % triangle_number)
    count += 1