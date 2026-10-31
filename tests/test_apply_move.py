from src.level import level_from_text, DIRECTIONS

def test_apply_move_next_tile_empty_change():
    test_data = [
        ('.\np', DIRECTIONS['UP'], 'p\n.'),
        ('p\n.', DIRECTIONS['DOWN'], '.\np'),
        ('.p', DIRECTIONS['LEFT'], 'p.'),
        ('p.', DIRECTIONS['RIGHT'], '.p'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)

def test_apply_next_tile_goal_change():
    test_data = [
        ('G\np', DIRECTIONS['UP'], 'P\n.'),
        ('p\nG', DIRECTIONS['DOWN'], '.\nP'),
        ('Gp', DIRECTIONS['LEFT'], 'P.'),
        ('pG', DIRECTIONS['RIGHT'], '.P'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)

def test_apply_next_tile_wall_no_change():
    test_data = [
        ('W\np', DIRECTIONS['UP'], 'W\np'),
        ('p\nW', DIRECTIONS['DOWN'], 'p\nW'),
        ('Wp', DIRECTIONS['LEFT'], 'Wp'),
        ('pW', DIRECTIONS['RIGHT'], 'pW'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)

def test_apply_next_tile_box_with_empty_change():
    test_data = [
        ('.\nb\np', DIRECTIONS['UP'], 'b\np\n.'),
        ('.\nB\np', DIRECTIONS['UP'], 'b\nP\n.'),
        ('p\nb\n.', DIRECTIONS['DOWN'], '.\np\nb'),
        ('p\nB\n.', DIRECTIONS['DOWN'], '.\nP\nb'),
        ('.bp', DIRECTIONS['LEFT'], 'bp.'),
        ('.Bp', DIRECTIONS['LEFT'], 'bP.'),
        ('pb.', DIRECTIONS['RIGHT'], '.pb'),
        ('pB.', DIRECTIONS['RIGHT'], '.Pb'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)

def test_apply_next_tile_box_with_goal_change():
    test_data = [
        ('G\nb\np', DIRECTIONS['UP'], 'B\np\n.'),
        ('G\nB\np', DIRECTIONS['UP'], 'B\nP\n.'),
        ('p\nb\nG', DIRECTIONS['DOWN'], '.\np\nB'),
        ('p\nB\nG', DIRECTIONS['DOWN'], '.\nP\nB'),
        ('Gbp', DIRECTIONS['LEFT'], 'Bp.'),
        ('GBp', DIRECTIONS['LEFT'], 'BP.'),
        ('pbG', DIRECTIONS['RIGHT'], '.pB'),
        ('pBG', DIRECTIONS['RIGHT'], '.PB'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)

def test_apply_next_tile_box_with_box_no_change():
    test_data = [
        ('b\nb\np', DIRECTIONS['UP'], 'b\nb\np'),
        ('B\nb\np', DIRECTIONS['UP'], 'B\nb\np'),
        ('b\nB\np', DIRECTIONS['UP'], 'b\nB\np'),
        ('B\nB\np', DIRECTIONS['UP'], 'B\nB\np'),
        ('p\nb\nb', DIRECTIONS['DOWN'], 'p\nb\nb'),
        ('p\nb\nB', DIRECTIONS['DOWN'], 'p\nb\nB'),
        ('p\nB\nb', DIRECTIONS['DOWN'], 'p\nB\nb'),
        ('p\nB\nB', DIRECTIONS['DOWN'], 'p\nB\nB'),
        ('bbp', DIRECTIONS['LEFT'], 'bbp'),
        ('Bbp', DIRECTIONS['LEFT'], 'Bbp'),
        ('bBp', DIRECTIONS['LEFT'], 'bBp'),
        ('BBp', DIRECTIONS['LEFT'], 'BBp'),
        ('pbb', DIRECTIONS['RIGHT'], 'pbb'),
        ('pbB', DIRECTIONS['RIGHT'], 'pbB'),
        ('pBb', DIRECTIONS['RIGHT'], 'pBb'),
        ('pBB', DIRECTIONS['RIGHT'], 'pBB'),
    ]

    results = []
    for test_datum in test_data:
        level_string, direction, expected = test_datum
        results.append(
            str(level_from_text(level_string).apply_move(direction)).strip() \
                == expected.strip()
        )
    assert all(results)
