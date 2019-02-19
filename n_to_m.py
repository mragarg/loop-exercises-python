run_1 = True
run_2 = True

while(run_1 == True or run_2 == True):
    start = input("Start from: ")
    try:
        start = int(start)
        run_1 = False
    except:
        print("Invalid start.")

    end = input("End on: ")
    try:
        end = int(end)
        run_2 = False
    except:
        print("Invalid end.")

while(start < (end + 1)):
    print(start)
    start += 1