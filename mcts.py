from node import MonteCarloSearchNode
import random

# M = 100 user specifiable need to fix in below method


def monte_carlo_tree_search(root):
    for _ in range(0, 500):
        node_to_visit = traverse(root)
        simulation_result = rollout(node_to_visit)
        backpropagate(node_to_visit, simulation_result)
    return best_child(root)


def traverse(node):
    while node.fully_expanded:
        node = best_uct(node)
    return pick_unvisited_child(node.children) or node


def rollout(node):
    while not node.terminal:
        node = rollout_policy(node)
    return result(node)  # figure out what my result is (node value -1 loss +1 win)


def rollout_policy(node):
    return random.choice(node.children)


def backpropagate(node, result):
    if not node.root:
        node.stats = update_stats(node, result)
        backpropagate(node.parent, result)
    return


def best_child(node):
    # pick child with highest number of visits.
    pass


def pick_unvisited_child(node):
    return random.choice(node.unvisited_children)


def best_uct(node):  # need implementation
    return node
