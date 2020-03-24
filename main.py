from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
import random

game = Game()
tree = MonteCarloSearchTree()
root_node = MonteCarloSearchNode(is_root=True, game_object=game, parent=None)
print("Begin")
print("Suggested action:", tree.suggest_action(root_node))
