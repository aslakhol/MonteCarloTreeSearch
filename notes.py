def rollout_policy(state):
    # determines the actions in a simulated game based on input state
    # default uniform random
    # probably just a dict
    return action

# simulation starts at a node that has not been visited

class MonteCarloSearchTree:
    rollout_policy = {}
    policy = {}
    root_node = None


class MonteCarloSearchNode:
    visited = False  # visited means a playout has started here
    fully_expanded = True
    children = []
    total_simulation_reward = 0 
    total_number_of_visits = 0

    def visit(self):
        self.visited = True
        self.playout()
        return self.backpropagate()

    def playout(self):
        # picks moves based on rollout_policy
        # nodes are NOT visited, just because they are picked by rollout_policy
        pass

    def backpropagate(self, reward):
        # recursive function, add 
        total_simulation_reward = reward + self.total_number_of_visits
        total_number_of_visits = self.total_number_of_visits += 1 
        return total_simulation_reward and total_number_of_visits


# Leaf node is the node where the simulation started, aka the newly visited node.


# Root node to unvisited node
# unvisited nodes chosen first



# UCT: Upper Confidence Bound applied to trees
# Fancy math function we use to decide which node to follow from the visited nodes. 

# exploitation component + exploration component

# ExploiC: win / loss rate
# total simulation reward / total number of visits

# ExplorC: favors those rarely explored


# unvisited - not touched
# visited - rollout has started here
# fully expanded - rollout performed in all children
