from my_functions import *

print("Welcome to my program")
print("\nIndex - \n1. Half pyramid of numbers.\n2. Half pyramid of asterisks\n3. Full pyramid of asterisks\n"
      "4. To print all\n\n")
while True:
    index = int(input("Enter index (1, 2, 3, 4)- "))
    rws = int(input("Enter rows to be formed (must be int) - "))
    if index == 1:
        print("========================")
        print("Processing...")
        pyramid_num(rws)
        break
    elif index == 2:
        print("========================")
        print("Processing...")
        stars_pyramid(rws)
        break
    elif index == 3:
        print("========================")
        print("Processing...")
        full_pyramid(rws)
        break
    elif index == 4:
        print("========================")
        pyramid_num(rws)
        print("\n========================")
        stars_pyramid(rws)
        print("\n========================")
        full_pyramid(rws)
        break
    else:
        print("Invalid Input! Re-starting program...")
