from chess_board import Board
from chess_pieces import Pawn, Knight, Rook, Bishop, Queen, King

# DEMO

b = Board()

queen = Queen("white")
rook = Rook("black")
knight = Knight("white")
pawn = Pawn("black")

# Taşları tahtaya koy
b.grid[7][3] = queen
b.grid[0][0] = rook
b.grid[7][1] = knight
b.grid[4][6] = pawn

print("BAŞLANGIÇ:")
for row in b.grid:
    print(row)

print("\nQueen hareket ediyor:")
print(b.move_piece([7, 3], [4, 3]))

print("\nKnight hareket ediyor:")
print(b.move_piece([7, 1], [5, 2]))

print("\nRook hareket ediyor:")
print(b.move_piece([0, 0], [3, 0]))

print("\nSON TAHTA:")
for row in b.grid:
    print(row)

