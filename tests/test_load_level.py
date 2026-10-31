import os

from src.level import level_from_text, level_from_file

LEVEL_STRING = """
..WWWWW.
WWW...W.
WGPB..W.
WWW.BGW.
WGWWB.W.
W.W.G.WW
WB.BBBGW
W...G..W
WWWWWWWW
"""

def test_load_from_text():
    level = level_from_text(LEVEL_STRING)
    assert str(level).strip() == LEVEL_STRING.strip()

def test_load_from_file():
    with open('level.txt', 'w') as level_file:
        level_file.write(LEVEL_STRING)
    assert os.path.exists('level.txt')

    level = level_from_file('level.txt')
    assert level is not None
    assert str(level).strip() == LEVEL_STRING.strip()

    os.remove('level.txt')
    assert not os.path.exists('level.txt')
