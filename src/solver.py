def backtracking_solver(level, show=False):
    stack = [[level]]
    visited = set()
    while stack:
        curr = stack.pop()
        curr_last_move = curr[-1]
        valid_moves = curr_last_move.get_valid_moves()
        for valid_move in valid_moves:
            if str(valid_move) not in visited:
                if valid_move.check_win_condition():
                    return curr + [valid_move]
                else:
                    stack.append(curr + [valid_move])
        visited.add(str(curr_last_move))
        if show:
            print(curr_last_move)
    return None

def backtracking_solver_with_stuck_pruning(level, show=False):
    stack = [[level]]
    visited = set()
    while stack:
        curr = stack.pop()
        curr_last_move = curr[-1]
        valid_moves = curr_last_move.get_valid_moves()
        for valid_move in [move for move in valid_moves if not move.has_stuck_boxes()]:
            if str(valid_move) not in visited:
                if valid_move.check_win_condition():
                    return curr + [valid_move]
                else:
                    stack.append(curr + [valid_move])
        visited.add(str(curr_last_move))
        if show:
            print(curr_last_move)
    return None
