def matcher(posx, posy, word, board):
    maxx = len(board[0])
    maxy = len(board)

    if posx not in range(0,maxx):
        return False
    elif posy not in range(0,maxy):
        return False
    elif not word:
        return True

    elif board[posy][posx] == word[0]:
        board[posy][posx] = ""
        res = [matcher(posx + 1,posy, word[1:], board),
               matcher(posx,posy + 1, word[1:], board),
               matcher(posx - 1,posy, word[1:], board),
               matcher(posx,posy - 1, word[1:], board)]

        if True in res:
            return True
        else:
            return False

    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(matcher(0,0, word, board))

