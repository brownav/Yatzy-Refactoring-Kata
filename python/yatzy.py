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

    def _sum_dice_target(self, target):
        count = self.dice.count(target)
        return count * target

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

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[0] == 1
            and tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
        ):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (
            tallies[1] == 1
            and tallies[2] == 1
            and tallies[3] == 1
            and tallies[4] == 1
            and tallies[5] == 1
        ):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if tallies[i] == 2:
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if tallies[i] == 3:
                _3 = True
                _3_at = i + 1

        if _2 and _3:
            return _2_at * 2 + _3_at * 3
        else:
            return 0
