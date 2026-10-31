from level import level_from_file
from solver import backtracking_solver

LEVEL_FILE_PATH = 'level.txt'

if __name__ == '__main__':
    level = level_from_file(LEVEL_FILE_PATH)
    solution = backtracking_solver(level, True)
    print(solution[-1])
