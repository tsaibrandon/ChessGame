class Piece():
    def __init__(self, name, icon, color, position):
        self.name = name
        self.icon = icon
        self.color = color
        self.position = position

    
class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Pawn",
        icon = "♟",       
        color = color,
        position = position 
        )

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Rook",
        icon = "♜",       
        color = color,
        position = position 
        )

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Knight",
        icon = "♞",       
        color = color,
        position = position 
        )

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Bishop",
        icon = "♝",       
        color = color,
        position = position 
        )

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Queen",
        icon = "♛",       
        color = color,
        position = position 
        )

class King(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "King",
        icon = "♚",       
        color = color,
        position = position 
        )