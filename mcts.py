from node import MonteCarloSearchNode
import random, math
from game import Game


class MonteCarloSearchTree:
    def __init__(self):
        self.M = 100
        self.c = math.sqrt(2)

    def suggest_action(self, root):
        for _ in range(0, self.M):
            node_to_visit = self.traverse(root)
            simulation_result = self.rollout(node_to_visit)
            self.backpropagate(node_to_visit, simulation_result)
        return self.best_child(root)

    def traverse(self, node):
        node.expand()
        while node.fully_expanded:
            node = self.best_uct(node)

        return self.pick_unvisited_child(node) or node

    def rollout(self, node):
        while not len(node.children) == 0:
            node = self.rollout_policy(node)
        return self.reward(
            node
        )  # figure out what my result is (node value -1 loss +1 win)

    def rollout_policy(self, node):
        return random.choice(node.children)

    def backpropagate(self, node, result):
        if not node.is_root:
            self.update_stats(node, result)
            self.backpropagate(node.parent, result)
        return

    def update_stats(self, node, result):
        node.total_number_of_visits += 1
        node.total_simulation_reward += result

    def best_child(self, node):
        return self.child_with_highest_number_of_visits(node)

    def child_with_highest_number_of_visits(self, node):
        return max(node.children, key=lambda x: x.total_number_of_visits)

    def pick_unvisited_child(self, node):
        print("pick unvisited", node)
        return random.choice(
            list(filter(lambda x: x.total_number_of_visits == 0, node.children))
        )

    def best_uct(self, node):
        best = node
        for child in node.children:
            child_utc = self.utc(child, node)
            if child_utc > best:
                best = child_utc

        return best

    def utc(self, node, parent):
        return self.exploitation_component(node) + self.exploration_component(
            node, parent
        )

    def exploitation_component(self, node):
        return node.total_simulation_reward / node.total_number_of_visits

    def exploration_component(self, node, parent):
        return self.c * math.sqrt(
            math.log(parent.total_number_of_visits) / node.total_number_of_visits
        )

    def reward(self, node):
        return node.reward

