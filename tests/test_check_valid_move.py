from src.level import level_from_text, DIRECTIONS

def test_check_next_tile_empty_is_valid_move():
    test_data = [
        ('.\np', DIRECTIONS['UP']),
        ('p\n.', DIRECTIONS['DOWN']),
        ('.p', DIRECTIONS['LEFT']),
        ('p.', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert all(results)

def test_check_next_tile_goal_is_valid_move():
    test_data = [
        ('G\np', DIRECTIONS['UP']),
        ('p\nG', DIRECTIONS['DOWN']),
        ('Gp', DIRECTIONS['LEFT']),
        ('pG', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert all(results)

def test_check_next_tile_wall_is_not_valid_move():
    test_data = [
        ('W\np', DIRECTIONS['UP']),
        ('p\nW', DIRECTIONS['DOWN']),
        ('Wp', DIRECTIONS['LEFT']),
        ('pW', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert not any(results)

def test_check_next_tile_box_with_empty_is_valid_move():
    test_data = [
        ('.\nb\np', DIRECTIONS['UP']),
        ('.\nB\np', DIRECTIONS['UP']),
        ('p\nb\n.', DIRECTIONS['DOWN']),
        ('p\nB\n.', DIRECTIONS['DOWN']),
        ('.bp', DIRECTIONS['LEFT']),
        ('.Bp', DIRECTIONS['LEFT']),
        ('pb.', DIRECTIONS['RIGHT']),
        ('pB.', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert all(results)

def test_check_next_tile_box_with_goal_is_valid_move():
    test_data = [
        ('G\nb\np', DIRECTIONS['UP']),
        ('G\nB\np', DIRECTIONS['UP']),
        ('p\nb\nG', DIRECTIONS['DOWN']),
        ('p\nB\nG', DIRECTIONS['DOWN']),
        ('Gbp', DIRECTIONS['LEFT']),
        ('GBp', DIRECTIONS['LEFT']),
        ('pbG', DIRECTIONS['RIGHT']),
        ('pBG', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert all(results)

def test_check_next_tile_box_with_box_is_not_valid_move():
    test_data = [
        ('b\nb\np', DIRECTIONS['UP']),
        ('B\nb\np', DIRECTIONS['UP']),
        ('b\nB\np', DIRECTIONS['UP']),
        ('B\nB\np', DIRECTIONS['UP']),
        ('p\nb\nb', DIRECTIONS['DOWN']),
        ('p\nb\nB', DIRECTIONS['DOWN']),
        ('p\nB\nb', DIRECTIONS['DOWN']),
        ('p\nB\nB', DIRECTIONS['DOWN']),
        ('bbp', DIRECTIONS['LEFT']),
        ('Bbp', DIRECTIONS['LEFT']),
        ('bBp', DIRECTIONS['LEFT']),
        ('BBp', DIRECTIONS['LEFT']),
        ('pbb', DIRECTIONS['RIGHT']),
        ('pbB', DIRECTIONS['RIGHT']),
        ('pBb', DIRECTIONS['RIGHT']),
        ('pBB', DIRECTIONS['RIGHT']),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction = test_datum
        results.append(level_from_text(level_string).check_valid_move(direction))
    assert not any(results)
