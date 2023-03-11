from Board import Checkers

def checkForValidInput(to_x, to_y):
    if (len(to_x) == 0 or len(to_x) > 1) or (len(to_y) == 0 or len(to_y) > 1):
        return False

    if (not to_x.isdigit()) or (not to_y.isdigit()):
        return False
    
    return True

checkers = Checkers()

print("Welcome to Checkers!")
print("Instructions: ...")
success = True
while (not checkers.isFinished()):
    if (not success):
        print("Invalid move! Try again:")
    else:
        checkers.printBoard()
        print("{}'s turn!".format(checkers.get_turn()))
    print("What piece would you like to move?")
    from_x = input("    enter x cord: ")
    from_y = input("    enter y cord: ")

    if (checkForValidInput(from_x, from_y) == False):
        print("Invalid input! Please enter a number between 0 and 7")
        continue
    
    # List of possible to moves
    to_moves_list = []
    
    # ask the user multiple times for to moves until they press X
    while True:
        print("What square would you like to move to?")
        
        to_x = input("  enter x cord: ")
        to_x = to_x.lower()
        if len(to_moves_list) > 0 and to_x == "X".lower():
            if len(to_moves_list) == 0:
                print("You must move at least one piece!")
                continue
            else:
                break

        to_y = input("  enter y cord: ")
        to_y = to_y.lower()
        if len(to_moves_list) > 0 and to_y == "X".lower():
            if len(to_moves_list) == 0:
                print("You must move at least one piece!")
                continue
            else:
                break

        if (checkForValidInput(to_x, to_y) == False):
            print("Invalid input! Please enter a number between 0 and 7")
            continue
        to_moves_list.append((int(to_y), int(to_x)))
    
    print("{} moving from ({}, {}) to ({}, {})".format(checkers.get_turn(), from_x, from_y, to_x, to_y))
    checkers.move((int(from_y), int(from_x)), to_moves_list)

print("Game over! {} won!!")

