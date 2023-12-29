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
        computer_ships()
        draw_boards()
    while check_winner() == False:
            user_turn()
            if check_winner() == False:
                computer_turn()
            draw_boards()


def check_winner() -> bool:
    if user_score == 20:
        print("You win!")
        return True
    elif computer_score == 20:
        print("You Lose!")
        return True
    return False


def user_turn():
    global user_score
    while True:
        position = input("Enter the position: ")
        if validate_cordinate(position):
            cordinate = position_translator(position)
            if hit(cordinate):
                if computer_board[cordinate].is_ship == True:
                    user_score += 1
                break


def computer_turn():
    global computer_score
    while True:
        position = random.randint(0, 99)
        if computer_hit(position):
            if user_board[position].is_ship:
                computer_score += 1
            break


def draw_ship(begin: int, direction, is_computer):
    # Set the location of the user ship by the location and direction that user entered
    
    if is_computer:
        computer_board[begin].is_ship = True
    else:
        user_board[begin].is_ship = True
    if direction == "V":
        y = 10
    else:
        y = 1
    for _ in range(3):
        begin += y
        if is_computer:
            computer_board[begin].is_ship = True
        else:
            user_board[begin].is_ship = True


def validate_direction(direction) -> bool:
    # Validate that the entry of the user should be only vertically or horizontally

    if direction != "V" and direction != "H":   
        print("Please enter either V or H.")
        return False
    return True


def define_ship():
    # Make ships for the user

    while True:
        begin = input("Please enter the starting position of your ship: ")
        if validate_cordinate(begin) == True:
            break
    while True:
        direction = input("Please enter V for Vertically and H for Horizontally shape of your ship: ").upper()
        if validate_direction(direction) == True:
            break
    
    position = position_translator(begin)
    if ship_validator(position, direction, False):
        draw_ship(position, direction, False)
    else:
        print("The position is out of grid, already taken by another ship or overlap with another ship.")
        define_ship()


def computer_ships():
    # Generate random position for computer ships

    while True:
        position = random.randint(0, 99)
        rand_direction = random.randint(1, 2)
        if rand_direction == 1:
            direction = "V"
        else:
            direction = "H"
        if ship_validator(position, direction, True):
            draw_ship(position, direction, True)
            break
        

def computer_hit(position: int) -> bool:
    # Generate random shot for computer
    if user_board[position].is_hit:
        return False
    else:
        user_board[position].is_hit = True
        return True
            
def ship_validator(position: int, direction, is_computer: bool) -> bool:
    # Validate that user can put the ship in the entry position or not

    if direction == "V":
        y = 10
    else:
        y = 1
    for _ in range(4):
        if y == 1 and position % 10 in [0, 8, 9]:
            return False
        if is_computer:
            try:
                if computer_board[position].is_ship:
                    return False
            except:
                return False
        else:
            try: 
                if user_board[position].is_ship:
                    return False
            except:
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
            elif computer_board[x * 10 + y].is_ship == False and computer_board[x * 10 + y].is_hit:
                print("x", end=" ")
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

def hit(position: int) -> bool:
    # Check the entry by the user that is duplicate or not, and if not duplicate check if it hits the ship or not

    cell = computer_board[position]
    if cell.is_hit:
        print("The position is a duplicate, please enter new position.")
        return False
    else:
        cell.is_hit = True
        return True
    
main()
