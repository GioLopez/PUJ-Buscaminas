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

weights = [-0.67425597, -0.25557734,  1.21907006, -0.5388088,  -0.84763563,  1.2426736, -0.08496626, -0.07428249 ]
bias = 0.06357287
logistic_model = PujLogistic(weights, bias)

patches = [[9 for row in range(height)] for columns in range(width)]
neighbours = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
]


while not board.have_won() and not board.have_lose():
    print(board)

    max_confidence = -1
    max_column = -1
    max_row = -1
    for column in range(width):
        for row in range(height):
            if patches[column][row] == 9:
                list_neighbours = []

                for neigh in neighbours:
                    neigh_column = column + neigh[0]
                    neigh_row = row + neigh[1]

                    if neigh_column < 0 or neigh_row < 0 or neigh_column >= width or neigh_row >= height:
                        list_neighbours.append(9)
                    else:
                        list_neighbours.append(patches[neigh_column][neigh_row])

                confidence = logistic_model(list_neighbours, threshold=False)
                if confidence > max_confidence:
                    max_confidence = confidence
                    max_row = row
                    max_column = column
    patches[max_column][max_row] = board.click(max_row, max_column)

print(board)
if board.have_won():
    print("You won!")
elif board.have_lose():
    print("You lose :-(")
