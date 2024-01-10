import random
import emoji
import sys, subprocess

class Board_cell:
    def __init__(self, is_ship, is_hit):
        self.is_ship = is_ship
        self.is_hit = is_hit

def board_setup(size: int) -> ([Board_cell], [Board_cell]):
    computer_board = [Board_cell(False, False) for _ in range(size * size)]
    user_board = [Board_cell(False, False) for _ in range(size * size)]
    return computer_board, user_board

user_score = 0
computer_score = 0
alphabet_row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def main():
    # The main logic of the game which can control the flow of the code aswell
    while True:
        print()
        print("               🌊  ❌  🚢  🔥  〰Battleship Game〰🔥  🚢  ❌  🌊")
        print()
        print("                           Welcome to the battle ship by ho3khaleghi")
        print("❗  Rules:")
        print()
        print("1. You should choose the board size of the game between 5(5x5), 8(8x8), 10(10x10).")
        print()
        print("2. You need to decide to put your ships in the position you like to.")
        print()
        print("3. You need to choose a direction of your ship. Just remember the starting point of your ship is the first position you have chose and make sure your ship will be in the grid.")
        print()
        print("4. Start guessing computers ship positions. If u sink all of your opponent's ships you will be the winner, but if not ... sadly you will be the loser.")
        print()
        print("                      🌏  Good Luck and Have Fun! 🌏")
        print()
        size_choice = input("Enter board size for your game between 5(5x5), 8(8x8) or 10(10x10): ")
        try:
            size = int(size_choice)
            if size in [5, 8, 10]:
                break
            else:
                print("Please enter a number between 5, 8, 10.")
        except ValueError:
            print("Please enter a number.")

    computer_board, user_board = board_setup(size)

    draw_boards(user_board, computer_board, size)
    for _ in range(5):
        define_ship(size, user_board, computer_board)
        computer_ships(size, user_board, computer_board)
        draw_boards(user_board, computer_board, size)
    while check_winner(size) == False:
            user_turn(computer_board, size)
            if check_winner(size) == False:
                computer_turn(user_board, size)
            draw_boards(user_board, computer_board, size)


def check_winner(size: int) -> bool:
    winner = False
    loser = False
    if size == 5:
        if user_score == 5:
            winner = True
        elif computer_score == 5:
            loser = True
    elif size == 8:
        if user_score == 15:
            winner = True
        elif computer_score == 15:
            loser = True
    else:    
        if user_score == 20:
            winner = True
        elif computer_score == 20:
            loser = True
    if winner:
        print()
        print("🏆  You win!")
        print("Thank you for playing!")
        print()
        return True
    if loser:
        print()
        print("💀  You Lose!")
        print("Thank you for playing!")
        print()
        return True
    return False


def clear_screen():
    '''
    This function just clear the terminal after each entry in inputs
    form https://www.youtube.com/watch?v=Kmu6rmPQt4c&ab_channel=FabioMusanni-ProgrammingChannel
    '''
    operating_system = sys.platform

    if operating_system == "win32":
        subprocess.run("cls", shell=True)
    
    elif operating_system == "linux" or operating_system == "darwin":
        subprocess.run("clear", shell=True)


def user_turn(computer_board: [Board_cell], size: int):
    global user_score
    while True:
        position = input("Enter the position: ")
        if validate_cordinate(position, size):
            cordinate = position_translator(position, size)
            if hit(cordinate, computer_board):
                if computer_board[cordinate].is_ship == True:
                    user_score += 1
                break


def computer_turn(user_board: [Board_cell], size: int):
    global computer_score
    while True:
        position = random.randint(0, size * size - 1)
        if computer_hit(position, user_board):
            if user_board[position].is_ship:
                computer_score += 1
            break


def draw_ship(begin: int, direction, is_computer, size: int, user_board: [Board_cell], computer_board: [Board_cell]):
    # Set the location of the user ship by the location and direction that user entered
    
    if is_computer:
        computer_board[begin].is_ship = True
    else:
        user_board[begin].is_ship = True
    if direction == "V":
        y = size
    else:
        y = 1
    
    if size == 5:
        ship_count = 1
    elif size == 8:
        ship_count = 3
    else:
        ship_count = 4
    for _ in range(ship_count - 1):
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


def define_ship(size: int, user_board: [Board_cell], computer_board: [Board_cell]):
    # Make ships for the user

    while True:
        begin = input("Please enter the starting position of your ship: ")
        if validate_cordinate(begin, size) == True:
            break
    while True:
        if size != 5:
            direction = input("Please enter V for Vertically and H for Horizontally shape of your ship: ").upper()
        else:
            direction = "V"
        if validate_direction(direction) == True:
            break
    
    position = position_translator(begin, size)
    if ship_validator(position, direction, False, size, user_board, computer_board):
        draw_ship(position, direction, False, size, user_board, computer_board)
    else:
        print("The position is out of grid, already taken by another ship or overlap with another ship.")
        define_ship(size, user_board, computer_board)


def computer_ships(size: int, user_board: [Board_cell], computer_board: [Board_cell]):
    # Generate random position for computer ships

    while True:
        position = random.randint(0, size * size - 1)
        rand_direction = random.randint(1, 2)
        if rand_direction == 1:
            direction = "V"
        else:
            direction = "H"
        if ship_validator(position, direction, True, size, user_board, computer_board):
            draw_ship(position, direction, True, size, user_board, computer_board)
            break
        

def computer_hit(position: int, user_board: [Board_cell]) -> bool:
    # Generate random shot for computer
    if user_board[position].is_hit:
        return False
    else:
        user_board[position].is_hit = True
        return True
            
def ship_validator(position: int, direction, is_computer: bool, size: int, user_board: [Board_cell], computer_board: [Board_cell]) -> bool:
    # Validate that user can put the ship in the entry position or not

    if size == 10:
        remaining = [0, 8, 9]
    elif size == 8:
        remaining = [0, 7]
    else:
        remaining = []

    if direction == "V":
        y = size
    else:
        y = 1
    if size == 5:
        ship_count = 1
    elif size == 8:
        ship_count = 3
    else:
        ship_count = 4
    for _ in range(ship_count):
        if y == 1 and (position + 1) % size in remaining:
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

def draw_boards(user_board: [Board_cell], computer_board: [Board_cell], size: int):
    # Draw the user board and computer board

    clear_screen()
    if size == 5:
        print("        〰Battleship Game〰")
        print("   Your board       Computer board  ")
        print(chr(4502) * 35)
    elif size == 8:
        print("             〰Battleship Game〰")
        print("     Your board              Computer board")
        print(chr(4502) * 47)    
    else:
        print("                 〰Battleship Game〰")
        print("      Your board                    Computer board")
        print(chr(4502) * 55)

    print("    ", end="")
    for i in range(size):
        print(alphabet_row[i], end=" ")
    print("  ",chr(8214),"       ", end="")
    for i in range(size):
        print(alphabet_row[i], end=" ")
    print()
    for x in range(size):
        row_number = ""
        if x < 9:
            row_number += "0"
        row_number += str(x + 1) + " "
        print(row_number, end="")
        for y in range(size):
            cell = user_board[x * size + y]
            if cell.is_ship:
                if cell.is_hit:
                    print("🔥 ", end="")
                else:
                    print("🚢 ", end="")
            else:
                if cell.is_hit:
                    print("❌ ", end="")
                else:
                    print("🌊 ", end="")

        print("   ", chr(8214), "  ", row_number, end="")
        for y in range(size):
            if computer_board[x * size + y].is_ship and computer_board[x * size + y].is_hit:
                print("🔥 ", end="")
            elif computer_board[x * size + y].is_ship == False and computer_board[x * size + y].is_hit:
                print("❌ ", end="")
            else:
                print("🌊 ", end="")

        print()


def validate_cordinate(position: str, size: int) -> bool:
    # Validate the cell entry by user
    
    input_length = len(position)
    
    if input_length == 3 and position[0:2] != "10":
        return False
    if input_length < 2 or input_length > 3:
        print("Input is in incorrect format!")
        return False
    position = position.upper()
    char = position[input_length - 1]
    
    if char.isdigit():
        print("Input is in incorrect format!")
        return False
    if size == 5:
        valid_headers = "ABCDE"
    elif size == 8:
        valid_headers = "ABCDEFGH"
    else:
        valid_headers = "ABCDEFGHIJ"
    
    if not valid_headers.__contains__(char):
        print("Input is in incorrect format!")
        return False
    char = position[0]
    if char.isdigit() == False:
        print("Input is in incorrect format!")
        return False
    return True

def position_translator(position: str, size: int) -> int:
    # Translate the position that user entered to integer between 1 to 100

    input_length = len(position)
    position = position.upper()
    char = position[input_length - 1]
    
    x = (int(position.replace(char, "")) - 1) * size
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

def hit(position: int, computer_board: [Board_cell]) -> bool:
    # Check the entry by the user that is duplicate or not, and if not duplicate check if it hits the ship or not

    cell = computer_board[position]
    if cell.is_hit:
        print("The position is a duplicate, please enter new position.")
        return False
    else:
        cell.is_hit = True
        return True
    
main()
