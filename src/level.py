class Level:
    def __init__(self, layout):
        self.layout = layout

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
