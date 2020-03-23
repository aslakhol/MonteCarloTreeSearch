from node import MonteCarloSearchNode
import random, math

# M = 100 user specifiable need to fix in below method
M = 100
c = math.sqrt(2)


def monte_carlo_tree_search(root):
    global M
    for _ in range(0, M):
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
    return reward(node)  # figure out what my result is (node value -1 loss +1 win)


def rollout_policy(node):
    return random.choice(node.children)


def backpropagate(node, result):
    if not node.root:
        update_stats(node, result)
        backpropagate(node.parent, result)
    return


def update_stats(node, result):
    node.total_number_of_visits += 1
    node.total_simulation_reward += result


def best_child(node):
    return child_with_highest_number_of_visits(node)


def child_with_highest_number_of_visits(node):
    return max(node.children, key=lambda x: x.children.total_number_of_visits)


def pick_unvisited_child(node):
    return random.choice(node.unvisited_children)


def best_uct(node):
    best = node
    for child in node.children:
        child_utc = utc(child, node)
        if child_utc > best:
            best = child_utc

    return best


def utc(node, parent):
    return exploitation_component(node) + exploration_component(node, parent)


def exploitation_component(node):
    return node.total_simulation_reward / node.total_number_of_visits


def exploration_component(node, parent):
    global c
    return c * math.sqrt(
        math.log(parent.total_number_of_visits) / node.total_number_of_visits
    )


def reward(node):
    return node.reward
