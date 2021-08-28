# =========================================================================
# @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
# =========================================================================

import sys
import os
from random import randint
from MineSweeperBoard import *
sys.path.append('/Users/Gio0/Develop/Python/Buscaminas/PUJ-Buscaminas')
from lib.python3.PUJ.Model.Logistic import Logistic as PujLog

# -------------------------------------------------------------------------
if len(sys.argv) < 4:
    print("Usage: python", sys.argv[0], "width height mines")
    sys.exit(1)
# end if
w = int(sys.argv[1])
h = int(sys.argv[2])
m = int(sys.argv[3])
board = MineSweeperBoard(w, h, m)

while not board.have_won() and not board.have_lose():
    print(board)
    i = randint(0, board.width() - 1)
    j = randint(0, board.height() - 1)
    board.click(j, i)
# end while

print(board)
if board.have_won():
    print("You won!")
elif board.have_lose():
    print("You lose :-(")
# end if

# eof - $RCSfile$
