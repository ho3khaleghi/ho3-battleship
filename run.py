import random

class Board_cell:
    def __init__(self, is_ship, is_hit):
        self.is_ship = is_ship
        self.is_hit = is_hit

computer_board = [Board_cell(False, False) for _ in range(100)]
user_board = [Board_cell(False, False) for _ in range(100)]
user_score = 0
computer_score = 0

def main():
    # The main logic of the game which can control the flow of the code aswell

    draw_boards()
    for _ in range(5):
        define_ship()
        draw_boards()
    game_over = False
    while game_over == False:
        position = input("Enter the position: ")
        if validate_cordinate(position):
            cordinate = position_translator(position)
            hit(cordinate)
            draw_boards()
            game_over = user_score == 15 or computer_score == 15


def draw_ship(begin: int, direction):
    # Set the location of the user ship by the location and direction that user entered
    
    user_board[begin].is_ship = True
    if direction == "V":
        y = 10
    else:
        y = 1
    for _ in range(3):
        begin += y
        user_board[begin].is_ship = True


def validate_direction(direction) -> bool:
    # Validate that the entry of the user should be only vertically or horizontally

    if direction != "V" and direction != "H":   
        print("Please enter either V or H.")
        return False
    return True


def define_ship():
    while True:
        begin = input("Please enter the starting position of your ship: ")
        if validate_cordinate(begin) == True:
            break
    while True:
        direction = input("Please enter V for Vertically and H for Horizontally shape of your ship: ").upper()
        if validate_direction(direction) == True:
            break
    
    position = position_translator(begin)
    if ship_validator(position, direction):
        draw_ship(position, direction)
    else:
        print("The position is already taken by another ship or overlap with another ship.")
        define_ship()


def computer_ships():
    # Generate random position for computer ships
    # random.randint(1, 100)
    pass
        

def computer_hit():
    # Generate random shot for computer

    pass
            
def ship_validator(position: int, direction) -> bool:
    # Validate that user can put the ship in the entry position or not

    if direction == "V":
        y = 10
    else:
        y = 1
    for _ in range(4):
        if user_board[position].is_ship:
            return False
        position += y
    return True

def draw_boards():
    # Draw the user board and computer board

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


def validate_cordinate(position: str) -> bool:
    # Validate the cell entry by user

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
    if char.isdigit() == False:
        print("Input is in incorrect format!")
        return False
    return True

def position_translator(position: str) -> int:
    # Translate the position that user entered to integer between 1 to 100

    input_length = len(position)
    position = position.upper()
    char = position[input_length - 1]
    
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
    return x + y

def hit(position: int):
    # Check the entry by the user that is duplicate or not, and if not duplicate check if it hits the ship or not

    global user_score
    cell = user_board[position]
    if cell.is_hit == True:
        print("The position is a duplicate, please enter new position.")
    else:
        cell.is_hit = True
        if cell.is_ship:
            user_score += 1
    
main()