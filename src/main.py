from level import level_from_file
from solver import backtracking_solver_with_stuck_pruning

LEVEL_FILE_PATH = 'level.txt'

if __name__ == '__main__':
    level = level_from_file(LEVEL_FILE_PATH)
    solution = backtracking_solver_with_stuck_pruning(level)
    print(solution[-1])
