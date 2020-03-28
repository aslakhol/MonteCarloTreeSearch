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

# for _ in range(0, 500):
#     print(_)
#     game = Game()
#     tree = MonteCarloSearchTree()
#     root_node = MonteCarloSearchNode(is_root=True, game_object=game, parent=None)
#     suggested_action = tree.suggest_action(root_node)
#     move = suggested_action.game_object.get_state()

#     moves[move] = moves.get(move, 0) + 1

# print(moves)


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
                print("here we go")

                action = tree.suggest_action(root_node)  # root node
                print(action)
                print("about to move")
                game.move(action)

                # do the move
                # update loop condition
                print(game.current_player)
            # update who is the winner
            # update stats with who wins.
            print("episode finished")


agent = Agent(1, True)

agent.play(1)
