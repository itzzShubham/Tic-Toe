import random as r
matrix = [[0,0,0],[0,0,0],[0,0,0]]
x = 1
o = 2

def display(matrix):
 for i in range(3):
    for j in range(3):
        print(matrix[i][j], end =" ")
    print("")
    

while(win = False):
count =0
if (count % 2 != 0):
    print("Chance of Player 1 (X): ")
    print("Where you want to put X:")
    count++
    game
elif:
    row = int(input("Enter row :"))
    col = int(input("Enter column :"))
    count++


print("Chance of Player 2 (O): ")
print("Where you want to put O:")

def isempty(matrix):
    if matrix[row][col] == 0:
        return True
    
def game(row,col,matrix,x):
   count = 0
   if(isempty(matrix) == True):
        if (row == 0 and col == 0):
            matrix[0][0] = x
        elif (row == 0 and col == 1):
            matrix[0][1] = x
        elif (row == 0 and col == 2):
            matrix[0][2] = x
        elif (row == 1 and col == 0):
            matrix[1][0] = x
        elif (row == 1  and col == 1):
            matrix[1][1] = x
        elif (row == 1 and col == 2):
            matrix[1][2] = x
        elif (row == 2 and col == 0):
            matrix[2][0] = x
        elif (row == 1  and col == 1):
            matrix[2][1] = x
        elif (row == 2 and col == 2):
            matrix[2][2] = x
