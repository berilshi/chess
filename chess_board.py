import chess_pieces

class Board:

    def __init__(self):
        self.grid = []

        for i in range(8):
            self.grid.append([])

            for j in range(8):
                self.grid[i].append(None)

    """
    def find_piece(self, piece):
        row = -1
        col = -1

        for r in range(8):
            for c in range(8):
                if self.grid[r][c] is piece:
                    return [r, c]
    """

    def move_piece(self, current_location, target_location):

        piece = self.grid[current_location[0]][current_location[1]]

        if piece is None:
            return False

        is_move_legal, middle_squares = piece.move(current_location, target_location)

        for s in middle_squares:
            if self.grid[s[0]][s[1]] is not None:
                return False
        
        if (self.grid[target_location[0]][target_location[1]] is None and is_move_legal):
            self.grid[target_location[0]][target_location[1]] = piece
            self.grid[current_location[0]][current_location[1]] = None
            return True
        
        return False 

    def capture_piece(self, current_location, target_location):

        piece = self.grid[current_location[0]][current_location[1]]

        if piece is None or (self.grid[target_location[0]][target_location[1]] is None):
            return False

        is_legal, middle_squares = piece.capture(current_location, target_location)
        
        if (self.grid[target_location[0]][target_location[1]].color != piece.color) and (is_legal):

            for square in middle_squares:
                if self.grid[square[0]][square[1]] is not None:
                    return False

            self.grid[target_location[0]][target_location[1]] = piece
            self.grid[current_location[0]][current_location[1]] = None
            return True
        
        return False

    def is_square_threatened(self, target_location, attacking_color):

        piece_locations = []
        threatened = True

        for i in range(0, 8):
            for j in range(0, 8):

                square_value = self.grid[i][j]
                
                if square_value is not None:
                    if square_value.color == attacking_color:
                        piece_locations.append([i, j])

        for location in piece_locations:

            piece = self.grid[location[0]][location[1]]
            can_move, required_empty_squares = piece.capture(location, target_location)  

            if can_move:

                if required_empty_squares == []: 
                    return threatened 
                
                for square in required_empty_squares:

                    if self.grid[square[0]][square[1]] is not None:
                        return False

        return True