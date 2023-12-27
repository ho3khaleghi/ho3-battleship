print("                 ",chr(7140) ,"Battleship Game", chr(7140))
print("       Your board                     Computer board  ")
print(chr(4502) * 56)
print("   A B C D E F G H I J    ",chr(8214),"      A B C D E F G H I J")

is_hit = False
is_ship = False
class Board_cell:
    def __init__(self, is_ship, is_hit):
        self.is_ship = is_ship
        self.is_hit = is_hit


#user_board = [[0]*10 for user_row in range(10)]
computer_board = [[Board_cell(False, False) for _ in range(10)] for _ in range(10)]
user_board = [[Board_cell(False, False) for _ in range(10)] for _ in range(10)]

user_board[0][0].is_ship = True
user_board[3][5].is_ship = True

for x in range(10):
    row_number = ""
    if x < 9:
        row_number += "0"
    row_number += str(x + 1) + " "
    output = row_number
    print(row_number, end="")
    for y in range(10):
        if user_board[x][y].is_ship:
            print("$", end=" ")
        else:
            print("_", end=" ")

    print("   ", chr(8214), "  ", row_number, end="")
    for y in range(10):
        if computer_board[x][y].is_ship and computer_board[x][y].is_hit:
            print("o", end=" ")
        else:
            print("_", end=" ")

    print()
