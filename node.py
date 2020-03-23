class MonteCarloSearchNode:
    root = False
    visited = False  # visited means a rollout has started here
    fully_expanded = True
    children = []
    unvisited_children = []
    total_simulation_reward = 0
    total_number_of_visits = 0

    def populate_children(self, possible_moves):
        pass
