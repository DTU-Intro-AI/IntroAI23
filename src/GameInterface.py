from Board import Checkers

checkers = Checkers()

print("Welcome to Checkers!")
print("Instructions: ...")
while (not checkers.isFinished()):
    print("{}'s turn!".format(checkers.get_turn()))
    checkers.printBoard()
    print("What piece would you like to move?")
    from_x = input("    enter x cord: ")
    from_y = input("    enter y cord: ")
    print("What square would you like to move to?")
    to_x = input("  enter x cord: ")
    to_y = input("  enter y cord: ")
    
    print("{} moving from ({}, {}) to ({}, {})".format(checkers.get_turn(), from_x, from_y, to_x, to_y))
    checkers.move((int(from_y), int(from_x)), [(int(to_y), int(to_x))])

print("Game over! {} won!!")

