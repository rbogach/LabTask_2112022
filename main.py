sizeString = input("Fill in the number to make your matrix")
size = int(sizeString)
print("Identity matrix")
for row in range(0, size):
    for col in range(0, size):
        if row == col:
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")
    print()
