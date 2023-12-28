

class Board_cell:
    def __init__(self, is_ship, is_hit):
        self.is_ship = is_ship
        self.is_hit = is_hit

computer_board = [Board_cell(False, False) for _ in range(100)]
user_board = [Board_cell(False, False) for _ in range(100)]
user_score = 0

def define_ship(begin, end):
    for x in range(begin, end):
        user_board[x].is_ship = True

define_ship(45, 48)
define_ship(1, 4)
define_ship(85, 88)
define_ship(63, 66)
define_ship(20, 23)

def draw_boards():
    print("                 ",chr(7140) ,"Battleship Game", chr(7140))
    print("       Your board                     Computer board  ")
    print(chr(4502) * 56)
    print("   A B C D E F G H I J    ",chr(8214),"      A B C D E F G H I J")
    for x in range(10):
        row_number = ""
        if x < 9:
            row_number += "0"
        row_number += str(x + 1) + " "
        output = row_number
        print(row_number, end="")
        for y in range(10):
            cell = user_board[x * 10 + y]
            if cell.is_ship:
                if cell.is_hit:
                    print("o", end=" ")
                else:
                    print("$", end=" ")
            else:
                if cell.is_hit:
                    print("x", end=" ")
                else:
                    print("_", end=" ")

        print("   ", chr(8214), "  ", row_number, end="")
        for y in range(10):
            if computer_board[x * 10 + y].is_ship and computer_board[x * 10 + y].is_hit:
                print("o", end=" ")
            else:
                print("_", end=" ")

        print()

draw_boards()

def validate_cordinate(position: str) -> bool:
    input_length = len(position)
    
    if input_length < 2 or input_length > 3:
        print("Input is in incorrect format!")
        return False
    position = position.upper()
    char = position[input_length - 1]
    
    if char.isdigit():
        print("Input is in incorrect format!")
        return False
    char = position[0]
    if ~char.isdigit():
        print("Input is in incorrect format!")
        return False
    return True

def hit(position: str):
    input_length = len(position)
    position = position.upper()
    char = position[input_length - 1]
    
    global user_score
    x = (int(position.replace(char, "")) - 1) * 10
    y = 0
    
    if char == "A":
        y = 0
    elif char == "B":
        y = 1
    elif char == "C":
        y = 2
    elif char == "D":
        y = 3
    elif char == "E":
        y = 4
    elif char == "F":
        y = 5
    elif char == "G":
        y = 6
    elif char == "H":
        y = 7
    elif char == "I":
        y = 8
    elif char == "J":
        y = 9
    else:
        print("Invalid cordinate.")
        return
    cell = user_board[x + y]
    if cell.is_hit == True:
        print("The position is a duplicate, please enter new position.")
    else:
        cell.is_hit = True
        if cell.is_ship:
            user_score += 1
    



game_over = False
while game_over == False:
    position = input("Enter the position: ")
    if validate_cordinate(position):
        hit(position)
        draw_boards()
        game_over = user_score == 15