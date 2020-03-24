from node import MonteCarloSearchNode
import random, math
from game import Game


class MonteCarloSearchTree:
    def __init__(self):
        self.M = 1000
        self.c = math.sqrt(2)

    def suggest_action(self, root):
        for _ in range(0, self.M):
            node_to_visit = self.traverse(root)
            simulation_result = self.rollout(node_to_visit)
            self.backpropagate(node_to_visit, simulation_result)
        return self.best_child(root)

    def traverse(self, node):
        node.expand()
        while node.is_fully_expanded():
            node = self.best_uct(node)

        return self.pick_unvisited_child(node) or node

    def rollout(self, node):
        node.visited = True
        return node.game_object.play_randomly()  # this is our rollout policy

    def backpropagate(self, node, result):
        if node:
            self.update_stats(node, result)
            self.backpropagate(node.parent, result)
        return

    def update_stats(self, node, result):
        node.total_number_of_visits += 1
        node.total_simulation_reward += result

    def best_child(self, node):
        return self.child_with_highest_number_of_visits(node)

    def child_with_highest_number_of_visits(self, node):
        print("Is root:", node.is_root)
        print(node.children)
        return max(node.children, key=lambda x: x.total_number_of_visits)

    def pick_unvisited_child(self, node):
        unvisited_children = list(
            filter(lambda x: x.total_number_of_visits == 0, node.children)
        )
        return random.choice(unvisited_children) if unvisited_children else False

    def best_uct(self, node):
        return max(node.children, key=lambda child: self.utc(child, node), default=node)

    def utc(self, node, parent):
        return self.exploitation_component(node) + self.exploration_component(
            node, parent
        )

    def exploitation_component(self, node):
        print(
            "reward:",
            node.total_simulation_reward,
            "visits:",
            node.total_number_of_visits,
            node.total_simulation_reward / node.total_number_of_visits,
        )
        return node.total_simulation_reward / node.total_number_of_visits

    def exploration_component(self, node, parent):
        return self.c * math.sqrt(
            math.log(parent.total_number_of_visits) / node.total_number_of_visits
        )

    def reward(self, node):
        # print("reward from mcts")
        if node.player == 1:
            return node.reward

        else:
            return -node.reward

