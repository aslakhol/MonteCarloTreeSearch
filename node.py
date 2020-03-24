class MonteCarloSearchNode:
    is_root = False
    visited = False  #
    fully_expanded = False
    reachable_game_states = []
    children = []
    total_simulation_reward = 0
    total_number_of_visits = 0
    parent = None
    reward = 0

    def __init__(self, is_root, parent, game_object):
        self.is_root = is_root
        self.game_object = game_object
        self.parent = parent
        self.reward = game_object.reward()

    def expand(self):
        self.children = [
            MonteCarloSearchNode(is_root=False, parent=self, game_object=game)
            for game in self.game_object.generate_child_states()
        ]

    def populate_children(self, possible_moves):
        pass

    def __str__(self):
        return f"root: {self.is_root}, fully expanded: {self.fully_expanded}, children: {self.children}, total reward: {self.total_simulation_reward}, total visits: {self.total_number_of_visits}, game state: {self.game_object.get_state()}"
