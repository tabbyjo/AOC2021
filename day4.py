def check_columns(board):
    board = list(zip(*board))
    return check_rows(board)

def check_rows(board):
    bingo = len(board[0])
    for row in board:
        count = 0
        for val_ in row:
            if val_ == "X":
                count += 1
        if count == bingo:
            return True
    return False

first = False
board = []
all_boards = []

text_file = open("day4.txt", "r")
lines = text_file.read().split('\n')
for line in lines:
    if "," in line:
        bingo_calls = line
        continue
    elif len(line) == 0:
        if board:
            all_boards.append(board)
        board = []
    else:
        if line[0] == (" "):
            line = line.replace(" ", "0", 1)
        board.append(line.replace("  ", " 0").split(" "))

bingo_calls = bingo_calls.split(",")
while bingo_calls:
    if len(bingo_calls[0]) == 1:
        bingo_calls[0] = "0" + bingo_calls[0]
    for j, board in enumerate(all_boards):
        board_won = False
        for i, line in enumerate(board):
            if bingo_calls[0] in line:
                board[i] = ["X" if x == bingo_calls[0] else x for x in line]
            if check_columns(board) or check_rows(board):
                board = [list(map(lambda x: 0 if x == "X" else int(x), row)) for row in board]
                unmarked_sum = sum(sum(row) for row in board)
                final_score = int(bingo_calls[0]) * unmarked_sum
                if not first:
                    print("FIRST BINGO!! Final Score:")
                    print(final_score)
                    first = True
                all_boards[j] = []
                break         
    del bingo_calls[0]
print("LAST BINGO!! Final Score:")
print(final_score)
