from game import Game
from mcts import MonteCarloSearchTree
from node import MonteCarloSearchNode
import random

game = Game()
tree = MonteCarloSearchTree()
root_node = MonteCarloSearchNode(True, children=game.generate_child_states())


def traverse_randomly(node):
    print("traversal step")
    if len(node.children) <= 1:
        print("The end")
        return

    random_child = MCSN_from_game(random.choice(node.children))
    print(random_child)
    return traverse_randomly(random_child)


def MCSN_from_game(game_object):
    print(game_object.get_state())
    return MonteCarloSearchNode(False, game_object.generate_child_states())


# while not game.is_end_state():
#     tree.suggest_action()

traverse_randomly(root_node)
