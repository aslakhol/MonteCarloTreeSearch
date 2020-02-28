class Nim:
    board = []

    def __init__(self, pieces, max_take):
        if pieces > 0 and max_take > 0:
            self.pieces = pieces
            self.max_take = max_take
        else:
            raise ValueError("Initialized to illegal game state")

        print("nim", pieces)

    def take_pieces(self, amount):
        if amount > 0 and amount < self.pieces:
            self.pieces -= amount
        else:
            raise ValueError("Illegal move")

        return self.is_end_state()

    def is_end_state(self):
        return self.pieces == 1


Nim(2, 1)
