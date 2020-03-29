class MonteCarloSearchNode:
    is_root = False
    visited = False  #
    fully_expanded = False
    reachable_game_states = []
    children = []
    total_simulation_reward = 0
    total_number_of_visits = 0
    parent = None
    move_from_parent = None
    reward = 0
    player = None

    def __init__(self, is_root, parent, game_object, move_from_parent):
        self.is_root = is_root
        self.game_object = game_object
        self.parent = parent
        self.move_from_parent = move_from_parent
        self.reward = game_object.reward()
        self.player = game_object.current_player

        if is_root:
            self.expand()
            # print("in self expand", self.children)
            print(f"init. root: {self.is_root} children: {self.children}")

    def expand(self):
        if self.children:
            return
        self.children = [
            MonteCarloSearchNode(
                is_root=False, parent=self, game_object=SAP[1], move_from_parent=SAP[0]
            )
            for SAP in self.game_object.generate_child_states()
        ]

    def is_fully_expanded(self):
        if not self.children:
            return False
        for child in self.children:
            if child.visited == False:
                return False
        return True

    def populate_children(self, possible_moves):
        pass

    def __str__(self):
        return f"NODE: root: {self.is_root}, player: {self.player}, children: {self.children}"

    def __repr__(self):
        return f"|root: {self.is_root} move from parent: {self.move_from_parent} lm: {self.game_object.game.get_legal_moves()}|"
