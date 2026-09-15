class Piece:

    def __init__(self, color):

        self.color = color

    def capture(self, current_location, target_location):
        return self.move(current_location, target_location)
    


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white pawn"
        
        return "black pawn"
        
    def move(self, current_location, target_location):

        if target_location[1] != current_location[1]:
            return False, []

        if self.color == "white":

            if (current_location[0] == 6) and (target_location[0] == (current_location[0] - 2)):
                 return True, [[(current_location[0] + target_location[0]) // 2, current_location[1]]]

            elif target_location[0] == (current_location[0] - 1):
                return True, []
            
        elif self.color == "black":

            if (current_location[0] == 1) and (target_location[0] == (current_location[0] + 2)):
                return True, [[(current_location[0] + target_location[0]) // 2, current_location[1]]]
            
            elif target_location[0] == (current_location[0] + 1):
                return True, []
                    
        return False, []

    def capture(self, current_location, target_location):

        if self.color == "white":

            if (current_location[0] == (target_location[0] + 1) and 
                (current_location[1] == (target_location[1] + 1) or current_location[1] == (target_location[1] - 1))):
                return True, []
            
        elif self.color == "black":
                    
                if (current_location[0] == (target_location[0] - 1) and 
                    (current_location[1] == (target_location[1] + 1) or current_location[1] == (target_location[1] - 1))):
                    return True, []

        return False, []



class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white knight"
        
        return "black knight"

    def move(self, current_location, target_location):

        if ((abs(current_location[0] - target_location[0]) == 1) and 
            (abs(current_location[1] - target_location[1]) == 2)) or (
            (abs(current_location[0] - target_location[0]) == 2) and 
            (abs(current_location[1] - target_location[1]) == 1)):
            return True, []

        return False, []



class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white rook"
        return "black rook"

    def move(self, current_location, target_location):

        required_empty_squares = []
        direction = 0

        if ((current_location[0] == target_location[0]) and (target_location[1] != current_location[1])) or (
            (current_location[1] == target_location[1]) and (target_location[0] != current_location[0])):

            if current_location[0] == target_location[0]:

                if current_location[1] < target_location[1]:
                    direction = 1
                elif current_location[1] > target_location[1]:
                    direction = -1

                for i in range(current_location[1] + direction, target_location[1], direction):
                    required_empty_squares.append([current_location[0], i])

            else:

                if current_location[0] < target_location[0]:
                    direction = 1
                elif current_location[0] > target_location[0]:
                    direction = -1

                for i in range(current_location[0] + direction, target_location[0], direction):
                    required_empty_squares.append([i, current_location[1]])

            return True, required_empty_squares

        return False, []



class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white rook"
        return "black rook"

    def move(self, current_location, target_location):

        required_empty_squares = []
        direction = (0, 0)

        if (abs(current_location[0] - target_location[0]) == abs(current_location[1] - target_location[1])) and (
            current_location != target_location):

            if current_location[0] < target_location[0]:
                if current_location[1] < target_location[1]:
                    direction = (1, 1)
                elif current_location[1] > target_location[1]:
                    direction = (1, -1)

            elif current_location[0] > target_location[0]:
                if current_location[1] < target_location[1]:
                    direction = (-1, 1)
                elif current_location[1] > target_location[1]:
                    direction = (-1, -1)

            for i, j in zip(range(current_location[0] + direction[0], target_location[0], direction[0]),
                            range(current_location[1] + direction[1], target_location[1], direction[1])):
                required_empty_squares.append([i, j])

            return True, required_empty_squares

        return False, []



class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white queen"
        return "black queen"

    def move(self, current_location, target_location):

        rook = Rook(self.color)
        bishop = Bishop(self.color)

        rook_result = rook.move(current_location, target_location)

        if rook_result[0]:
        
            return rook_result

        bishop_result = bishop.move(current_location, target_location)
        
        if bishop_result[0]:
        
            return bishop_result

        return False, []



class King(Piece):

    def __init__(self, color):
        super().__init__(color)

    def __repr__(self):

        if self.color == "white":
            return "white king"
        return "black king"

    def move(self, current_location, target_location):

        if (current_location[0] == target_location[0]) and (current_location[1] == target_location[1]):
            return False, []

        elif (abs(current_location[0] - target_location[0]) == 1 or abs(current_location[0] - target_location[0]) == 0) and (
            (abs(current_location[1] - target_location[1]) == 1 or abs(current_location[1] - target_location[1]) == 0)):

            return True, []

        return False, []
    