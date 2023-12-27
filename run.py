print("                 ",chr(7140) ,"Battleship Game", chr(7140))
print("       Your board                     Computer board  ")
print(chr(4502) * 56)
print("   A B C D E F G H I J    ",chr(8214),"      A B C D E F G H I J")
for x in range(10):
    row_number = ""
    if x < 9:
        row_number += "0"
    
    row_number += str(x + 1)
    print(row_number, "_ " * 10, "  ",chr(8214),"  ", row_number, "_ " * 10)
    
