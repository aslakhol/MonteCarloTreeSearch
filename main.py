from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
import random

game = Game()
tree = MonteCarloSearchTree()

root_node = MonteCarloSearchNode(True, children=game.generate_child_states())


print(root_node)
# while not game.is_end_state():
#     tree.suggest_action()

# while not game.is_end_state():
#     legal_moves = game.get_legal_moves()
#     game.move(random.choice(legal_moves))
