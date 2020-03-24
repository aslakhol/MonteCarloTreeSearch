from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
import random

# game = Game()
# tree = MonteCarloSearchTree()
# root_node = MonteCarloSearchNode(is_root=True, game_object=game, parent=None)
# print("Begin")
# suggested_action = tree.suggest_action(root_node)
# print("Suggested action:", suggested_action)

# print()

# print(suggested_action)

moves = {}

for _ in range(0, 1000):
    game = Game()
    tree = MonteCarloSearchTree()
    root_node = MonteCarloSearchNode(is_root=True, game_object=game, parent=None)
    suggested_action = tree.suggest_action(root_node)
    print("Suggested action:", suggested_action)
    move = 10 - suggested_action.game_object.get_state()

    moves[move] = moves.get(move, 0) + 1

print(moves)

