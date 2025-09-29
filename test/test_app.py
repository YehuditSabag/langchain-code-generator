from app import calc_avg

def test_calc_avg():
    assert calc_avg([1, 2, 3, 4, 5]) == 3
    assert calc_avg([10, 20]) == 15
    assert calc_avg([-1, 1]) == 0