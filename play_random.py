from game import Game
import random

game = Game()
while not game.is_end_state():
    legal_moves = game.get_legal_moves()
    game.move(random.choice(legal_moves), False)
