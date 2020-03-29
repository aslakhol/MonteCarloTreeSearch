class Nim:
    board = []

    def __init__(self, pieces, max_take):
        if pieces > 0 and max_take > 0:
            self.pieces = pieces
            self.max_take = max_take
        else:
            raise ValueError("Initialized to illegal game state")

    def move(self, action):
        amount = action[0]
        if amount > 0 and amount <= self.pieces:
            self.pieces -= amount
        else:
            print(f"Remaining pieces: {self.pieces} Attempted move: take {amount}")
            raise ValueError("Illegal move")

        return self.is_end_state()

    def is_end_state(self):
        return self.pieces == 0

    def get_legal_moves(self):
        return [[i] for i in range(1, min(self.max_take, self.pieces) + 1)]

    def get_state(self):
        return self.pieces

    def reward(self):
        if self.pieces == 0:
            return 1
        return 0

    def get_verbose(self, currentPlayer, action):
        return f"Player {currentPlayer} selects {action[0]} stones: remaining stones = {self.pieces}"
