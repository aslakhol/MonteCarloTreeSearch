import random
from config import nim as nim_config
from config import ledge as ledge_config
from config import general as general_config
from ledge import Ledge
from nim import Nim


class Game:
    def __init__(self, initial_state=""):
        self.verbose = general_config["verbose_mode"]
        self.starting_player = self.get_starting_player(
            general_config["starting_player"]
        )
        self.current_player = self.starting_player
        if general_config["game"] == "nim":
            pieces = initial_state if initial_state else nim_config["pieces"]
            self.game = Nim(pieces=pieces, max_take=nim_config["max_take"])
        elif general_config["game"] == "ledge":
            board = initial_state if initial_state else ledge_config["initial_board"]
            self.game = Ledge(initial_board=board)
        else:
            raise Exception("Wrong game configuration")

    # Initialize starting player
    def get_starting_player(self, config):
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

    def move(self, action):
        self.game.move(action)
        if self.verbose:
            print(self.game.get_verbose(self.current_player, action))
        self.switch_current_player()
        return self

    def is_end_state(self):
        return self.game.is_end_state()

    def generate_child_states(self):
        return [
            (action, Game(self.get_state()).move(action))
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
            self.move(random.choice(legal_moves))
        return self.reward()

    def __str__(self):
        return f"GAME: player: {self.current_player}, state: {self.game.get_state()}"

    def __repr__(self):
        return self.__str__()
