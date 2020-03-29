from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
from config import general as config
import random


class Agent:
    def __init__(self):
        self.episodes = config["episodes"]
        self.M = config["M"]
        self.c = config["c"]
        self.verbose = config["verbose"]

        self.stats = {1: 0, 2: 0}

    def play(self):
        for _ in range(1, self.episodes + 1):
            game = Game()
            mcst = MonteCarloSearchTree(config["M"], config["c"])
            node = MonteCarloSearchNode(
                is_root=True, game_object=game, parent=None, move_from_parent=None
            )
            while not game.is_end_state():
                action, node = mcst.suggest_action(node)
                current_player = game.current_player
                game.move(action, self.verbose)
            self.stats[current_player] += 1
        print(self.stats)


agent = Agent()
agent.play()
