TRAVERSABLE_TILES = {'.', 'G'}
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}
DIRECT_MOVE_TRANSITIONS = {
    'p': '.',
    'P': 'G',
    '.': 'p',
    'G': 'P',
}
BOX_MOVE_TRANSITIONS = {
    'p': '.',
    'P': 'G',
    'b': 'p',
    'B': 'P',
    '.': 'b',
    'G': 'B',
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
        if type(layout) is not list:
            raise Exception(f'Expected layout to be a list, got {layout} instead')
        if len(layout) > 0:
            if type(layout[0]) is not list:
                raise Exception(f'Expected layout to be a list of lists, got {layout} instead')

            types_and_lengths_match = []
            for row in layout:
                if len(row) > 0:
                    for col in row:
                        types_and_lengths_match.append(type(col) is str and len(col) == 1)
            if not all(types_and_lengths_match):
                raise Exception(f'Expected layout to be a list of lists of chars, got {layout} instead')

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

    def apply_move(self, direction):
        if not self.check_valid_move(direction):
            return Level(self.layout.copy())

        player_x, player_y = self.player_location()
        direction_x, direction_y = direction

        target_tile_content = \
            self.layout[player_y + direction_y][player_x + direction_x]

        new_layout = self.layout.copy()

        if target_tile_content.lower() == 'b': # A box move
            player_tile_content = \
                new_layout[player_y][player_x]
            box_tile_content = \
                new_layout[player_y + direction_y][player_x + direction_x]
            box_target_tile_content = \
                new_layout[player_y + 2*direction_y][player_x + 2*direction_x]

            new_layout[player_y][player_x] = \
                BOX_MOVE_TRANSITIONS[player_tile_content]
            new_layout[player_y + direction_y][player_x + direction_x] = \
                BOX_MOVE_TRANSITIONS[box_tile_content]
            new_layout[player_y + 2*direction_y][player_x + 2*direction_x] = \
                BOX_MOVE_TRANSITIONS[box_target_tile_content]
        else: # A direct move
            player_tile_content = \
                new_layout[player_y][player_x]
            target_tile_content = \
                new_layout[player_y + direction_y][player_x + direction_x]

            new_layout[player_y][player_x] = \
                DIRECT_MOVE_TRANSITIONS[player_tile_content]
            new_layout[player_y + direction_y][player_x + direction_x] = \
                DIRECT_MOVE_TRANSITIONS[target_tile_content]

        return Level(new_layout)

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
    layout = []
    for row in string.strip().split('\n'):
        layout.append(list(row))

    return Level(layout)

def level_from_file(path):
    level = None

    with open(path, 'r') as level_file:
        level = level_from_text(level_file.read())

    if level is None:
        raise Exception(f'Failed to read level file at {path}')

    return level
