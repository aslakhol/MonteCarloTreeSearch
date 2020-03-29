import random
from config import nim as nim_config
from config import ledge as ledge_config
from config import general as general_config
from ledge import Ledge
from nim import Nim


class Game:
    def __init__(self, initial_state=""):
        self.starting_player = self.initialize_starting_player()
        self.current_player = self.starting_player
        self.game = self.select_game(initial_state)

    def select_game(self, initial_state):
        name = general_config["game"]
        try:
            if name == "nim":
                return self.setup_nim(initial_state)
            elif name == "ledge":
                return self.setup_ledge(initial_state)
            else:
                raise Exception("Invalid name in game configuration")
        except:
            raise Exception("Invalid game configuration")

    def setup_nim(self, initial_state):
        pieces = initial_state if initial_state else nim_config["pieces"]
        return Nim(pieces=pieces, max_take=nim_config["max_take"])

    def setup_ledge(self, initial_state):
        board = initial_state if initial_state else ledge_config["initial_board"]
        return Ledge(initial_board=board)

    def initialize_starting_player(self):
        config = general_config["starting_player"]
        if config == "one":
            return 1
        elif config == "two":
            return 2
        elif config == "mix":
            return 1 if random.random() > 0.5 else 2

    def switch_current_player(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

    def move(self, action, verbose):
        self.game.move(action)
        if verbose:
            print(self.game.get_verbose(self.current_player, action))
        self.switch_current_player()
        return self

    def is_end_state(self):
        return self.game.is_end_state()

    def generate_child_states(self):
        return [
            (action, Game(self.get_state()).move(action, False))
            for action in self.get_legal_moves()
        ]

    def get_legal_moves(self):
        return self.game.get_legal_moves()

    def get_state(self):
        return self.game.get_state()

    def reward(self):
        if self.current_player == 1:
            return self.game.reward()
        else:
            return self.game.reward() * -1

    def play_randomly(self):
        while not self.is_end_state():
            legal_moves = self.get_legal_moves()
            self.move(random.choice(legal_moves), False)
        return self.reward()

    def __str__(self):
        return f"GAME: player: {self.current_player}, state: {self.game.get_state()}"

    def __repr__(self):
        return self.__str__()
