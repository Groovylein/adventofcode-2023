import pytest

from day_2 import check_game, get_valid_games, get_sum_of_valid_games


@pytest.mark.parametrize("game_input,expected", [
    ("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
    ("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
    ("8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
    ("1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
    ("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),])
def test_check_game(game_input, expected):
    # GIVEN
    # WHEN
    result = check_game(game_input)
    # THEN
    assert result is expected


def test_true_game_collector():
    # GIVEN
    game_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    # WHEN
    result = get_valid_games(game_input)
    # THEN
    expected_list = ["Game 1", "Game 2", "Game 5"]
    assert result == expected_list


def test_sum():
    # GIVEN
    game_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    # WHEN
    result = get_sum_of_valid_games(game_input)
    # THEN
    assert result == 8
