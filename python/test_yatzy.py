from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance_scores_sum_of_all_dice():
    assert Yatzy(2, 3, 4, 5, 1).chance() == 15


def test_yatzy_scores_50():
    assert Yatzy(6, 6, 6, 6, 3).yatzy() == 0
    assert Yatzy(4, 4, 4, 4, 4).yatzy() == 50


def test_ones():
    assert Yatzy(6, 2, 2, 4, 5).ones() == 0
    assert Yatzy(1, 2, 3, 4, 5).ones() == 1
    assert Yatzy(1, 2, 1, 1, 1).ones() == 4


def test_twos():
    assert Yatzy(6, 1, 1, 4, 5).twos() == 0
    assert Yatzy(1, 2, 3, 4, 5).twos() == 2
    assert Yatzy(1, 2, 2, 2, 2).twos() == 8


def test_threes():
    assert Yatzy(6, 1, 1, 4, 5).threes() == 0
    assert Yatzy(1, 2, 3, 4, 5).threes() == 3
    assert Yatzy(1, 3, 3, 3, 3).threes() == 12


def test_fours():
    assert Yatzy(1, 5, 5, 5, 5).fours() == 0
    assert Yatzy(4, 4, 5, 5, 5).fours() == 8
    assert Yatzy(4, 4, 4, 5, 5).fours() == 12


def test_fives():
    assert Yatzy(4, 4, 4, 2, 3).fives() == 0
    assert Yatzy(4, 4, 3, 2, 5).fives() == 5
    assert Yatzy(4, 5, 5, 5, 5).fives() == 20


def test_sixes():
    assert Yatzy(4, 4, 4, 5, 5).sixes() == 0
    assert Yatzy(4, 4, 6, 5, 5).sixes() == 6
    assert Yatzy(6, 5, 6, 6, 5).sixes() == 18


def test_one_pair():
    assert Yatzy(3, 4, 3, 5, 6).score_pair() == 6
    assert Yatzy(5, 3, 3, 3, 5).score_pair() == 10
    assert Yatzy(5, 3, 6, 6, 5).score_pair() == 12


def test_two_pair():
    assert Yatzy(3, 3, 6, 5, 4).two_pair() == 0
    assert Yatzy(3, 3, 5, 4, 5).two_pair() == 16
    assert Yatzy(3, 3, 6, 6, 6).two_pair() == 18


def test_three_of_a_kind():
    assert Yatzy(3, 1, 2, 3, 5).three_of_a_kind() == 0
    assert Yatzy(3, 1, 1, 1, 1).three_of_a_kind() == 3
    assert Yatzy(3, 3, 3, 4, 5).three_of_a_kind() == 9
    assert Yatzy(5, 3, 5, 4, 5).three_of_a_kind() == 15


def test_four_of_a_kind():
    assert Yatzy(3, 3, 3, 2, 1).four_of_a_kind() == 0
    assert Yatzy(3, 3, 3, 3, 3).four_of_a_kind() == 12
    assert Yatzy(5, 5, 5, 4, 5).four_of_a_kind() == 20


def test_small_straight():
    assert Yatzy(1, 2, 2, 4, 5).small_straight() == 0
    assert Yatzy(2, 3, 4, 5, 6).small_straight() == 0
    assert Yatzy(1, 2, 3, 4, 5).small_straight() == 15
    assert Yatzy(3, 2, 4, 5, 1).small_straight() == 15


def test_large_straight():
    assert Yatzy(1, 2, 2, 4, 5).large_straight() == 0
    assert Yatzy(1, 2, 3, 4, 5).large_straight() == 0
    assert Yatzy(6, 2, 3, 4, 5).large_straight() == 20
    assert Yatzy(2, 3, 4, 5, 6).large_straight() == 20


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
