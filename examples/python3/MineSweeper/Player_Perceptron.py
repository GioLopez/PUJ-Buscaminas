# =========================================================================
# @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
# =========================================================================
import random
import sys, os
from random import randint
from MineSweeperBoard import *
sys.path.append(os.path.join( os.getcwd( ), '../../../lib/python3'))
from lib.python3.PUJ.Model.Logistic import Logistic as PujLogistic

# -------------------------------------------------------------------------
if len(sys.argv) < 4:
    print("Usage: python", sys.argv[0], "width height mines")
    sys.exit(1)
# end if
width = int(sys.argv[1])
height = int(sys.argv[2])
mines = int(sys.argv[3])
board = MineSweeperBoard(width, height, mines)

weights = [-0.38564548, -4.19527307, 0.48126624, 0.25850804, -1.46453883, -2.66257381, -0.28437442, 8.02342586, -7.00469692, 1.55610172, 2.82969498, -3.10644083, 2.37723717, 3.49617572, 2.97081675, 1.37867055, -3.5449626, 1.96189007, -0.30941269, -1.20977446, -1.84815403, 2.18323952, -3.86809174, -2.30665896]
bias = 0.68268195
logistic_model = PujLogistic(weights, bias)

patches = [[9 for row in range(height)] for columns in range(width)]
neighbours = [
    [-2, -2],
    [-2, -1],
    [-2, 0],
    [-2, 1],
    [-2, 2],
    [-1, 2],
    [0, 2],
    [1, 2],
    [2, 2],
    [2, 1],
    [2, 0],
    [2, -1],
    [2, -2],
    [1, -2],
    [0, -2],
    [-1, -2],
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1]
]


while not board.have_won() and not board.have_lose():
    print(board)

    max_confidence = -1
    max_column = -1
    max_row = -1
    for column in range(width):
        for row in range(height):
            if patches[row][column] == 9:
                list_neighbours = []

                for neigh in neighbours:
                    neigh_column = column + neigh[0]
                    neigh_row = row + neigh[1]

                    if neigh_column < 0 or neigh_row < 0 or neigh_column >= width or neigh_row >= height:
                        list_neighbours.append(10)
                    else:
                        list_neighbours.append(patches[neigh_column][neigh_row])

                confidence = logistic_model(list_neighbours, threshold=False)
                if confidence > max_confidence:
                    max_confidence = confidence
                    max_row = row
                    max_column = column
    #         print(column, row, confidence)
    #         print("\t", patches)
    print('#'*8, max_row, max_column, max_confidence)
    patches[max_row][max_column] = board.click(max_column, max_row)

print(board)
if board.have_won():
    print("You won!")
elif board.have_lose():
    print("You lose :-(")
