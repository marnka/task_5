from app import addition

def test_addition():
    assert addition(3, 4) == 7
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-3, -7) == -10