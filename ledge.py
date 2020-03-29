class Ledge:
    end_state = False

    def __init__(self, initial_board):
        self.board = [int(i) for i in initial_board]
        if not list(filter(lambda x: x == 2, self.board)):
            self.end_state = True

    def move(self, action):
        if action[0] == "PICK_UP":
            if self.board[0] == 2:
                self.end_state = True
            self.board[0] = 0
        elif action[0] == "MOVE_COIN":
            position_from = action[1]
            position_to = action[2]
            coin = self.board[position_from]
            self.board[position_to] = coin
            self.board[position_from] = 0
        else:
            raise ValueError("Illegal move")
        return self.is_end_state()

    def is_end_state(self):
        return self.end_state

    def get_legal_moves(self):
        moves = []
        coin_indices = [index for index, value in enumerate(self.board) if value != 0]
        for index in coin_indices:
            reverse = range(index - 1, -1, -1)
            for i in reverse:
                if self.board[i] != 0:
                    break
                moves.append(["MOVE_COIN", index, i])
        if self.board[0] != 0:
            moves.append(["PICK_UP"])
        return moves

    def get_state(self):
        return "".join(map(str, self.board))

    def reward(self):
        if self.end_state:
            return 1
        elif self.board[0] == 2:
            return -1
        return 0

    def get_verbose(self, currentPlayer, action):
        if action[0] == "PICK_UP":
            coin = "Copper" if not self.end_state else "Gold"
            return f"{currentPlayer} picks up {coin}: {self.board}"
        if action[0] == "MOVE_COIN":
            index = action[2]
            coin = "Copper" if self.board[index] == 1 else "Gold"
            return f"{currentPlayer} moves {coin} from cell {action[1]} to {index} : {self.board}"
