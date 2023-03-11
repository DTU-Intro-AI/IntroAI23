from Board import Checkers

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
    print("What square would you like to move to?")
    to_x = input("  enter x cord: ")
    to_y = input("  enter y cord: ")
    
    print("{} moving from ({}, {}) to ({}, {})".format(checkers.get_turn(), from_x, from_y, to_x, to_y))
    success = checkers.move((from_x, from_y), [(to_x, to_y)])

print("Game over! {} won!!")

