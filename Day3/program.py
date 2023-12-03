from functools import reduce
board = []

def part2():
    sum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        construct2DArray(lines)
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if x >= board[y].__len__():
                    break
                if board[y][x] == "*":
                    check, succArr = checkSurrounding(y,x, lambda boardChar: boardChar.isnumeric())
                    if check:
                        numbers = []
                        checkedIndexes = []
                        for succ in succArr:
                            print(succ, checkedIndexes)
                            if not succ in checkedIndexes:
                                numb, indexes = getNumber(succ[0],succ[1])
                                print('found', numb)
                                numbers.append(numb)
                                checkedIndexes.extend(indexes)
                        if numbers.__len__() == 2:
                            sum += reduce(lambda x,y: x * y, numbers)
        print(sum)

def part1():
    sum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        construct2DArray(lines)
        for y, row in enumerate(board):
            offset = 0
            for x, col in enumerate(row):
                x = x + offset
                if x >= board[y].__len__():
                    break
                if board[y][x].isnumeric():
                    for xOffset in range(0, board[y].__len__()-x):
                        if board[y][x+xOffset].isnumeric():
                            check,arr = checkSurrounding(y, x+xOffset, lambda boardChar: not boardChar.isnumeric() and not boardChar == ".")
                            if check:
                                numb, indexes = getNumber(y,x)
                                sum += numb
                                offset += str(numb).__len__()-1
                                break
                        else:
                            offset += xOffset
                            break
        print(sum)


def construct2DArray(lines):
    for line in lines:
        b_line = [*line.strip()]
        board.append(b_line)

# y = row, x = col
def checkSurrounding(y,x, func):
    found = False
    foundArr = []
    for yOffset in range(-1,2):
        for xOffset in range(-1,2):
            if(y+yOffset >= 0 and y+yOffset < board.__len__() and x+xOffset >= 0 and x+xOffset < board.__len__()):
                boardChar = board[y+yOffset][x+xOffset]
                if func(boardChar):
                    found = True
                    foundArr.append((y+yOffset, x+xOffset))
    return found, foundArr

def getNumber(y,x):
    indexes = []
    for xOffset in range(board[y].__len__()-x):
        if not board[y][x-xOffset].isnumeric() or x-xOffset < 0:
            x = x-xOffset+1
            break
    numb = ""
    for xOffset in range(board[y].__len__()-x):
        char = board[y][x+xOffset]
        if char.isnumeric():
            indexes.append((y,x+xOffset))
            numb += char
        else:
            break
    return int(numb), indexes

part2()