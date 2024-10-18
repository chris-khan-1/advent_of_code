from day_21_solution import get_winner


def test_get_winner():
    player_stats = {"hit_points": 8, "damage": 5, "armour": 5}
    boss_stats = {"hit_points": 12, "damage": 7, "armour": 2}
    actual = get_winner(player_stats=player_stats, boss_stats=boss_stats)
    assert actual == "player"
