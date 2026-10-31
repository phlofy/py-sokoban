from src.level import level_from_text

def test_check_win_condition():
    assert not level_from_text('pbG').check_win_condition()
    assert level_from_text('.pB').check_win_condition()
