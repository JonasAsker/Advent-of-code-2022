import copy

def makeGrid():
    grid = []
    with open('input20228.txt') as file:
        for line in file.readlines():
            line = [int(i) for i in line.strip('\n')]
            grid.append(line)
    gridT = list(map(list, zip(*grid)))
    return grid, gridT


def getTallestRow(row, rowIndex, tallest, prevMarker):
    if type(prevMarker) == int:
        if prevMarker > (len(row) // 2) + 1: # checking from the left
            maxHeight = max(row[:prevMarker])
            maxHeightIndex = row.index(maxHeight)
        else: # checking from the right
            maxHeight = max(row[prevMarker:])
            maxHeightIndex = (len(row) - 1 - 
                                row[::-1].index(maxHeight))
        if ((max(prevMarker, maxHeightIndex) == len(row) - 1)
            and min(prevMarker, maxHeightIndex) == 0):
            return tallest
        row[min(prevMarker, maxHeightIndex) : max(prevMarker, maxHeightIndex) + 1] = \
                                            [0] * (abs(maxHeightIndex - prevMarker) + 1)
    else:
        maxHeight = max(row)
        maxHeightIndex = row.index(maxHeight)
        row[maxHeightIndex] = 0 
    tallest.add((rowIndex, maxHeightIndex))
    prevMarker = maxHeightIndex
    tallest = getTallestRow(row, rowIndex, tallest, prevMarker)
    return tallest


def treeEvaluator(tree, row):
    directions = [1, -1]
    score = [0,0]
    for i in directions:
        j = 1
        while (tree + (j * i)) >= 0 and (tree + (j * i)) < len(row):
            score[directions.index(i)] += 1
            if row[tree + j * i] >= row[tree]:
                break
            j += 1
    return score[0] * score[1]


def getBestTreeHouse(inner, grid, gridT):
    totScore = 0
    for tree in inner:
        scoreHorz = treeEvaluator(tree[1], grid[tree[0]])
        scoreVert = treeEvaluator(tree[0], gridT[tree[1]])
        tempScore = scoreHorz * scoreVert
        totScore = max(totScore, tempScore)
    return totScore


def getTallestGrid(grid, gridT):
    gridCC = copy.deepcopy(grid)
    gridTCC = copy.deepcopy(gridT)
    tallest = set()
    tallestInRow = set()
    for i in range(1, len(gridCC) - 1):
        tallestInRow = getTallestRow(gridCC[i], i, set(), False)
        tallest.update(tallestInRow)
    for i in range(1, len(gridCC) - 1):
        tallestInRow = getTallestRow(gridTCC[i], i, set(), False)
        tallestInRow = set([(i[1], i[0]) for i in tallestInRow])
        tallest.update(tallestInRow)
    return tallest
        

def main():
    grid, gridT = makeGrid()
    tallest = getTallestGrid(grid, gridT)
    inner = list(filter(lambda x: (len(grid) - 1) not in x and 0 not in x, tallest))
    print(getBestTreeHouse(inner, grid, gridT))


main()