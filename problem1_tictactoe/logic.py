import time

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if '' not in board:
        return 'Draw'
    return None

def score_terminal(winner, depth, ai, human):
    if winner == ai:
        return 10 - depth
    if winner == human:
        return depth - 10
    return 0

def best_move_minimax(board, ai='O', human='X'):
    nodes = {'count': 0}
    start = time.perf_counter()

    def minimax(state, depth, maximizing):
        nodes['count'] += 1
        winner = check_winner(state)
        if winner:
            return score_terminal(winner, depth, ai, human)

        if maximizing:
            best_score = -999
            for i in range(9):
                if state[i] == '':
                    state[i] = ai
                    best_score = max(best_score, minimax(state, depth + 1, False))
                    state[i] = ''
            return best_score
        best_score = 999
        for i in range(9):
            if state[i] == '':
                state[i] = human
                best_score = min(best_score, minimax(state, depth + 1, True))
                state[i] = ''
        return best_score

    move = None
    best_score = -999
    for i in range(9):
        if board[i] == '':
            board[i] = ai
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i

    return {'move': move, 'nodes': nodes['count'], 'time_ms': (time.perf_counter() - start) * 1000}

def best_move_alpha_beta(board, ai='O', human='X'):
    nodes = {'count': 0}
    start = time.perf_counter()

    def alphabeta(state, depth, alpha, beta, maximizing):
        nodes['count'] += 1
        winner = check_winner(state)
        if winner:
            return score_terminal(winner, depth, ai, human)

        if maximizing:
            value = -999
            for i in range(9):
                if state[i] == '':
                    state[i] = ai
                    value = max(value, alphabeta(state, depth + 1, alpha, beta, False))
                    state[i] = ''
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break
            return value
        value = 999
        for i in range(9):
            if state[i] == '':
                state[i] = human
                value = min(value, alphabeta(state, depth + 1, alpha, beta, True))
                state[i] = ''
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return value

    move = None
    best_score = -999
    alpha, beta = -999, 999
    for i in range(9):
        if board[i] == '':
            board[i] = ai
            score = alphabeta(board, 0, alpha, beta, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
            alpha = max(alpha, best_score)

    return {'move': move, 'nodes': nodes['count'], 'time_ms': (time.perf_counter() - start) * 1000}
