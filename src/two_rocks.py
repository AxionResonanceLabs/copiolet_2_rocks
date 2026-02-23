class TwoRocks:
    def __init__(self, rock1_weight, rock2_weight):
        self.rock1_weight = rock1_weight
        self.rock2_weight = rock2_weight

    def total_weight(self):
        return self.rock1_weight + self.rock2_weight

    def average_weight(self):
        return self.total_weight() / 2

    def heavier_rock(self):
        return max(self.rock1_weight, self.rock2_weight)

# Example usage:
# two_rocks = TwoRocks(3, 5)
# print(two_rocks.total_weight())  # Output: 8
# print(two_rocks.average_weight())  # Output: 4.0
# print(two_rocks.heavier_rock())  # Output: 5