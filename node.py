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
    player = None

    def __init__(self, is_root, parent, game_object):
        self.is_root = is_root
        self.game_object = game_object
        self.parent = parent
        self.reward = game_object.reward()
        self.player = game_object.current_player

        if is_root:
            self.expand()

    def expand(self):
        if self.children:
            return
        self.children = [
            (
                SAP[0],
                MonteCarloSearchNode(is_root=False, parent=self, game_object=SAP[1]),
            )
            for SAP in self.game_object.generate_child_states()
        ]

    def is_fully_expanded(self):
        print("hello")
        if not self.children:
            return False
        for child_SAP in self.children:
            if child_SAP[1].visited == False:
                return False
        return True

    def populate_children(self, possible_moves):
        pass

    def __str__(self):
        return f"root: {self.is_root}, player: {self.player}, fully expanded: {self.fully_expanded}, reward: {self.total_simulation_reward}, visits: {self.total_number_of_visits}, game state: {self.game_object.get_state()}"

    def __repr__(self):
        return f"|visits: {self.total_number_of_visits}, reward: {self.total_simulation_reward}, c: {len(self.children)}|"
