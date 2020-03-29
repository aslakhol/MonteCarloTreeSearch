from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
import random


class Agent:
    def __init__(self, episodes, verbose):
        self.episodes = episodes
        self.verbose = verbose
        self.stats = {1: 0, 2: 0}

    def play(self, starting_player):
        for _ in range(1, self.episodes + 1):
            # print("Starting episode...")
            game = Game()
            mcst = MonteCarloSearchTree()
            node = MonteCarloSearchNode(
                is_root=True, game_object=game, parent=None, move_from_parent=None
            )
            while not game.is_end_state():  # game is not completed
                action, node = mcst.suggest_action(node)  # root node
                current_player = game.current_player
                game.move(action, self.verbose)
            self.stats[current_player] += 1
            # print(f"Player {current_player} wins the game!")
        print(self.stats)


agent = Agent(50, False)

agent.play(1)
