
class Ledge:
    board = []
    self.end_state = False
    def __init__(self, initial_board):
        board = [int(i) for i in initial_board]

    def move(self, action):
        if action[0] == "PICK_UP"
            if(self.board[0] == 2):
                self.end_state = True
            self.board[0] = 0 
        elif action[0] == "MOVE_COIN":
            position_from = action[1]
            number_of_steps = action[2]
            coin = self.board[position_from]
            self.board[position_from] = 0
            self.board[position_to - numberOfSteps] = coin
        else:
            raise ValueError("Illegal move")
        return self.is_end_state()

    def is_end_state(self):
        return self.end_state

    def generate_child_states(self):
        child_states = []
        for move in range self.get_legal_moves():
            game = Ledge(initial_board=self.getState())
            game.move(move)
            child_states.append(game.get_state())
        return child_states


    def get_legal_moves(self):
        moves = []
        coins_indices = [0] + [index for index, value in enumerate(self.board) if value != 0]
        for i in range(1, len(coin_indices)):
            for j in range(coin_indices[i-1], coin_indices[i]-1):
                moves.append(["MOVE_COIN",coin_indices[i], j)
        if(self.board[0] != 0):
            moves.append(["PICK_UP"])
        return moves
    
    def get_state(self):
        return "".join(map(str,self.board))


    def reward(self):
        if(self.end_state):
            return 1
        elif(self.board[0] == 2):
            return -1
        return 0

