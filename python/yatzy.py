class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int):
        self.dice = [d1, d2, d3, d4, d5]

    def chance(self):
        """Scores the sum of all dice, no matter what they read."""
        return sum(self.dice)

    def yatzy(self):
        """If all dice have the same number, score 50 points."""
        if len(set(self.dice)) == 1:
            return 50
        return 0

    def ones(self):
        return self._sum_dice_target(1)

    def twos(self):
        return self._sum_dice_target(2)

    def threes(self):
        return self._sum_dice_target(3)

    def fours(self):
        return self._sum_dice_target(4)

    def fives(self):
        return self._sum_dice_target(5)

    def sixes(self):
        return self._sum_dice_target(6)

    def score_pair(self):
        """Scores the sum of the two highest matching dice."""
        self.dice.sort()
        self.dice.reverse()

        for i in range(len(self.dice) - 1):
            if self.dice[i] == self.dice[i + 1]:
                return self.dice[i] * 2
        return 0

    def two_pair(self):
        """Scores the sum of the two highest matching dice"""
        self.dice.sort()
        self.dice.reverse()

        sum = 0
        pairs = 0
        i = 0
        while i < len(self.dice) - 1:
            if self.dice[i] == self.dice[i + 1]:
                sum += self.dice[i] * 2
                pairs += 1
                i += 1
            if pairs == 2:
                return sum
            i += 1
        return 0

    def three_of_a_kind(self):
        """If there are three dice with the same number, score the sum of these dice."""
        dice_map = dict.fromkeys(self.dice, 0)

        for die in self.dice:
            dice_map[die] = dice_map[die] + 1
            if dice_map[die] == 3:
                return die * 3
        return 0

    def four_of_a_kind(self):
        """If there are four dice with the same number, score the sum of these dice."""
        first_elem_count = self.dice.count(self.dice[0])
        last_elem_count = self.dice.count(self.dice[-1])

        if first_elem_count >= 4:
            return self.dice[0] * 4
        elif last_elem_count >= 4:
            return self.dice[-1] * 4
        else:
            return 0

    def small_straight(self):
        """If dice are sequential starting at 1 and ending at 5, score 15 points."""
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def large_straight(self):
        """If dice are sequential starting at 2 and ending at 6, score 20 points."""
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def full_house(self):
        """If the dice are two of a kind and three of a kind, score the sum of all the dice."""
        dice_map = dict.fromkeys(self.dice, 0)
        if len(dice_map) != 2:
            return 0

        for die in self.dice:
            dice_map[die] = dice_map[die] + 1

        total = 0
        for die in dice_map:
            if dice_map[die] != 2 and dice_map[die] != 3:
                return 0
            else:
                total += die * dice_map[die]
        return total

    def _sum_dice_target(self, target):
        count = self.dice.count(target)
        return count * target
