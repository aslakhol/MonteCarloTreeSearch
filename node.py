class MonteCarloSearchNode:
    is_root = False
    visited = False  # visited means a playout has started here
    fully_expanded = False
    children = []
    unvisited_children = []
    total_simulation_reward = 0
    total_number_of_visits = 0

    def __init__(self, is_root, children):
        self.is_root = is_root
        self.children = children

    def populate_children(self, possible_moves):
        pass

    def __str__(self):
        return f"root: {self.is_root}, visited: {self.visited}, fully expanded: {self.fully_expanded}, children: {self.children}, total reward: {self.total_simulation_reward}, total visits: {self.total_number_of_visits}"
