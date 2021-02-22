#!/usr/bin/env python3

def onBoard(x, y):
    return x>= 0 and x<8 and y>=0 and y<8

def checkPawn(px, py, c):
    if c.isupper():
        if onBoard(px-1, py-1) and board[px-1][py-1] == c.isupper():
            return True
        if onBoard(px-1, py+1) and board[px-1][py+1] == c.isupper():
            return True
    else:
        if onBoard(px+1, py-1) and board[px+1][py-1] == c:
            return True
        if onBoard(px+1, py+1) and board[px+1][py+1] == c:
            return True
    return False

def checkRook(rx, ry, c):
    k=0
    while onBoard(rx+k, ry):
        if board[rx+k][ry] == c:
            return True
        k += 1

    k=0
    while onBoard(rx+k, ry):
        if board[rx+k][ry] == c:
            return True
        k -= 1

    k = 0
    while onBoard(rx, ry+k):
        if board[rx][ry+k] == c:
            return True
        k += 1

    k = 0
    while onBoard(rx, ry+k):
        if board[rx][ry+k] == c:
            return True
        k -= 1
    return False

def checkKnight(nx, ny, c):
    x_possible = [2, 2, -2, -2, 1, 1, -1, -1]
    y_possible = [1, -1, 1, -1, 2, -2, 2, -2]

    for i in range(8):
        x = nx + x_possible[i]
        y = ny + y_possible[i]

        if (onBoard(x, y) and board[x][y] == c):
            return True
    return False

def checkQueen(qx, qy, c):
    if c.isupper():
        cr, cb = "R", "B"
    else:
        cr, cb = "r", "b"
    return checkRook(qx, qy, cr) or checkBishop(qx, qy, cb)

def checkKing(kx, ky, c):
    x_possible = [-1, -1, -1, 0, 0, 1, 1, 1]
    y_possible = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(8):
        x = kx + x_possible[i]
        y = ky + y_possible[i]

        if (onBoard(x, y) and board[x][y] == c):
            return True
    return False

def checkBishop(bx, by, c):
    k = 0
    while onBoard(bx+k, by+k):
        if board[bx+k][by+k] == c:
            return True
        k += 1

    k = 0
    while onBoard(bx+k, by-k):
        if board[bx+k][by-k] == c:
            return True
        k += 1

    k = 0
    while onBoard(bx-k, by+k):
        if board[bx-k][by+k] == c:
            return True
        k += 1

    k = 0
    while onBoard(bx-k, by-k):
        if board[bx-k][by-k] == c:
            return True
        k += 1
    return False

def getCoords(p):
    if p[0] == 'a':
        x = 0
    elif p[0] == 'b':
        x = 1
    elif p[0] == 'c':
        x = 2
    elif p[0] == 'd':
        x = 3
    elif p[0] == 'e':
        x = 4
    elif p[0] == 'f':
        x = 5
    elif p[0] == 'g':
        x = 6
    elif p[0] == 'h':
        x = 7
    return x, int(p[1])-1

def buildBoard(positons_list):
    chess_board = [[ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ],
                   [ '-', '-', '-', '-', '-', '-', '-', '-' ]]
    kings = {}
    board = chess_board
    for i in positons_list:
        piece = i.split(',')[1] if i.split(',')[0] == 'w' else i.split(',')[1].upper()
        piece_raw_coords = i.split(',')[2]
        piece_x, piece_y = getCoords(piece_raw_coords)
        if piece.lower() == "k":
            kings[piece] = (piece_x, piece_y)
        board[piece_x][piece_y] = piece
    return kings, board

def IsKingInCheck(kings):
    return (
    (checkQueen(kings['k'][0], kings['k'][1], "Q") or checkKnight(kings['k'][0], kings['k'][1], "N") or checkKing(kings['k'][0], kings['k'][1], "K") or checkPawn(kings['k'][0], kings['k'][1], "P")) or (checkQueen(kings['K'][0], kings['K'][1], "q") or checkKnight(kings['K'][0], kings['K'][1], "n") or checkKing(kings['K'][0], kings['K'][1], "k") or checkPawn(kings['K'][0], kings['K'][1], "p"))
)

def ParseMatches(chess_matches):
    return [c.split('+') for c in chess_matches.split(' ')]

result = []
chess_matches =  ParseMatches(raw_input())
for chess_match in chess_matches:
    kings, board = buildBoard(chess_match)

    result.append(IsKingInCheck(kings))

print(result)
