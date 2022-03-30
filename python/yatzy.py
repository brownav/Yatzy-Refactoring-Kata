class Yatzy:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, d5: int):
        self.dice = [d1, d2, d3, d4, d5]

    def chance(self):
        """Scores the sum of all dice, no matter what they read"""
        return sum(self.dice)

    def yatzy(self):
        """If all dice have the same number, score 50 points"""
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
        """Scores the sum of the two highest matching dice"""
        reversed_sorted_dice = sorted(self.dice, reverse=True)

        for i in range(len(reversed_sorted_dice) - 1):
            if reversed_sorted_dice[i] == reversed_sorted_dice[i + 1]:
                return reversed_sorted_dice[i] * 2
        return 0

    def _sum_dice_target(self, target):
        count = self.dice.count(target)
        return count * target

    def two_pair(self):
        """Scores the sum of the two highest matching dice"""
        reversed_sorted_dice = sorted(self.dice, reverse=True)

        sum = 0
        pairs = 0
        i = 0
        while i < len(self.dice) - 1:
            if reversed_sorted_dice[i] == reversed_sorted_dice[i + 1]:
                sum += reversed_sorted_dice[i] * 2
                pairs += 1
                i += 1
            if pairs == 2:
                return sum
            i += 1
        return 0

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if tallies[i] >= 4:
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if t[i] >= 3:
                return (i + 1) * 3
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
