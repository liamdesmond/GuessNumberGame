#Liam Roberts 11-23-22
#liam.roberts44@myhunter.cuny.edu
#Game Program

import random
def num():
    user = int(input("Enter only 1-6: "))
    while user < 1 or user > 6:
        print("Input needs to be in 1-6. Re-enter: ")
        user = int(input("Enter only 1-6: "))
    return user

def game():
    user = num()
    computer = random.randint(1,6)
    print("user: ",user)
    print("computer: ",computer)

    if user == computer:
        print("draw")
    elif user+computer in [3, 6, 7, 8]:
        print("user wins")
    else:
        print("computer wins")

def main():
    game()
if __name__ == "__main__":
    main()
