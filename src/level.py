TRAVERSABLE_TILES = {'.', 'G'}
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}

class Level:
    """
    Tile key:

          | Regular | Goal   | Wall
    ------|---------|--------|------
    Empty |    .    |   G    |  W
    ------|---------|--------|------
    Box   |    b    |   B    |     
    ------|---------|--------|------
    Player|    p    |   P    |      

    """
    def __init__(self, layout):
        self.layout = layout # TODO: Validate map data
        self.num_rows = len(self.layout)
        self.num_cols = len(self.layout[0]) # Board is rectangular

    def player_location(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if self.layout[y][x].lower() == 'p':
                    return x, y

    def check_valid_move(self, direction):
        player_x, player_y = self.player_location()
        direction_x, direction_y = direction

        if not all([0 <= player_x + direction_x < self.num_cols,
            0 <= player_y + direction_y < self.num_rows]):
            return False

        target_tile_content = \
            self.layout[player_y + direction_y][player_x + direction_x]

        if target_tile_content.lower() == 'b': # A box tile
            if not all([0 <= player_x + 2*direction_x < self.num_cols,
                0 <= player_y + 2*direction_y < self.num_rows]):
                return False

            box_target_tile_content = \
                self.layout[player_y + 2*direction_y][player_x + 2*direction_x]

            return box_target_tile_content in TRAVERSABLE_TILES

        elif target_tile_content in TRAVERSABLE_TILES: # Can walk directly on the tile
            return True
        else: # A wall
            return False


    def __str__(self):
        result = ''
        for row in self.layout:
            for col in row:
                result += col
            result += '\n'
        result = result[:-1]
        return result

    def __repr__(self):
        return self.__str__()


def level_from_text(string):
    return Level(list(string.strip().split('\n')))

def level_from_file(path):
    level = None

    with open(path, 'r') as level_file:
        level = level_from_text(level_file.read())

    if level is None:
        raise Exception(f'Failed to read level file at {path}')

    return level
