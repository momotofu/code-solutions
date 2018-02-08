def discovered_checks(possible_pieces, king_position, pawn_position):
    for i in range(8):
        pos = (0,i)
        moves = {}
        if board[0][0][i] == 'Q':
            moves = possible_pieces[0]
        elif board[0][0][i] == 'B':
            moves = possible_pieces[2]
        else:
            continue
        for key, value in moves.items():
            move = (pos[0] + value[0], pos[1] + value[1])
            if move == pawn_position:
                while 0 <= move[0] < 8 and 0 <= move[1] < 8:
                    if board[move[0]][0][move[1]] != '#' and move != king_position:
                        break
                    if move == king_position:
                        return 1
                    else:
                        move = (move[0] + value[0], move[1] + value[1])
    return 0

def waysToGiveACheck(board):
    # define different pieces
    # Queen, Rook, or Bishop, or Knight
    # find pawns 8th position
    # find position of king
    # iterate through positions and incrament if match is found

    queen = {'left': (0,-1), 'right': (0, 1), 'bottom': (1, 0), 'left-diagonal': (1, -1), 'right-diagonal': (1, 1)}
    rook = {'left': (0,-1), 'right': (0, 1), 'bottom': (1, 0)}
    bishop = {'left-diagonal': (1, -1), 'right-diagonal': (1, 1)}
    knight = {'in-left': (1, -2), 'out-left': (2, -1), 'in-right': (1, 2), 'out-right': (2, 1)}

    number_of_checks = 0
    possible_pieces = [queen, rook, bishop, knight]
    pawn_position = (0,0)
    king_position = (0,0)

    for i in range(8):
        for j in range(8):
            if i == 1 and board[i][0][j] == 'P':
                pawn_position = (0, j)
                board[i][0] = board[i][0][:j] + '#' + board[i][0][j + 1:]
            if board[i][0][j] == 'k':
                king_position = (i, j)

    # write logic
    if board[pawn_position[0]][0][pawn_position[1]] != '#':
        return 0
    # check for discovered checks
    number_of_checks += discovered_checks(possible_pieces, king_position, pawn_position = (1, pawn_position[1]))

    # king is on 7th row and there is something other than a knight on that row
    for i in range(8):
        square = board[1][0][i]
        if i > pawn_position[1] > king_position[1]:
            if square == 'Q' or square == 'R':
                number_of_checks += 1
                break
        elif i < pawn_position[1] < king_position[1]:
            if square == 'Q' or square == 'R':
                number_of_checks += 1
                break
    for piece in possible_pieces:
        for key, value in piece.items():
            move = (pawn_position[0] + value[0], pawn_position[1] + value[1])
            # Check if knight
            if key[:2] == 'in' or key[:3] == 'out':
                # check if move is within the board
                if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                    if board[move[0]][0][move[1]] == 'k':
                        number_of_checks += 1
                        continue
            else:
                # move until outside of board or hit king
                while 0 <= move[0] < 8 and 0 <= move[1] < 8:
                    if board[move[0]][0][move[1]] != '#' and move != king_position: # board[move[0]][0][move[1]] != 'k':
                        break
                    if move == king_position:
                        number_of_checks += 1
                        break
                    else:
                        move = (move[0] + value[0], move[1] + value[1])
    return number_of_checks
