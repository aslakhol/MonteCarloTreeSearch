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
        for episode in range(1, self.episodes + 1):
            print("Starting episode...")
            game = Game()  # init here
            tree = MonteCarloSearchTree()  # init here
            root_node = MonteCarloSearchNode(
                is_root=True, game_object=game, parent=None, move_from_parent=False
            )
            print(game.is_end_state())
            while not game.is_end_state():  # game is not completed

                action = tree.suggest_action(root_node)  # root node
                game.move(action)

                # do the move
                # update loop condition
                print(game.current_player)
            # update who is the winner
            # update stats with who wins.
            print("episode finished")


agent = Agent(1, True)

agent.play(1)
