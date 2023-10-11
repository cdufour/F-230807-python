import sys

try:
    m = int(sys.argv[1])
    if m > -1 and m < 1001:
        for i in range(11):
            print(f"{m} x {i} = {m*i}")
    else:
        print("Value out of bounds (0,1000) !!")
except IndexError:
    print("No arg provided")