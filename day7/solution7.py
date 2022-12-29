from dataclasses import dataclass

def buildTree():
    data = D({'/':D({})})
    directoryStack = []
    with open('input20227.txt') as file:
        for line in file.readlines():
            line = line.split()
            if line[0] == '$':
                if line[1] == 'cd' and line[2] != '..':
                    directoryStack.append(line[2])
                elif line[1] == 'cd' and line[2] == '..':
                    directoryStack.pop(-1)
                elif line[1] == 'ls':
                    currentDirectory = setCurrDir(data, directoryStack)
            else:
                if line[0] == 'dir':
                    currentDirectory.cont[line[1]] = D({})
                else:
                    currentDirectory.cont[line[1]] = int(line[0])
    return data


def calcDirSize1(data, dirStack, smallDirs):
    curDir = setCurrDir(data, dirStack)
    size = 0
    for k in curDir.cont:
        if type(curDir.cont[k]) == int:
            size += curDir.cont[k]
        else:
            dirStack.append(k)
            nextDir = calcDirSize1(data, dirStack, smallDirs)
            dirStack.pop(-1)
            size += nextDir[0]
            smallDirs = nextDir[1]
    if size <= 100000:
        smallDirs.append(size)
    return size, smallDirs
        

def calcDirSize2(data, dirStack, bigDirs, limit):
    curDir = setCurrDir(data, dirStack)
    size = 0
    for k in curDir.cont:
        if type(curDir.cont[k]) == int:
            size += curDir.cont[k]
        else:
            dirStack.append(k)
            nextDir = calcDirSize2(data, dirStack, bigDirs, limit)
            dirStack.pop(-1)
            size += nextDir[0]
            bigDirs = nextDir[1]
    if size >= limit:
        bigDirs.append(size)
    return size, bigDirs


@dataclass # This is unnecessary, should have only used dictionaries.
class D:
    # D for directory
    cont: dict


def setCurrDir(data, dirStack):
    currDir = data
    for d in dirStack:
        currDir = currDir.cont[d]
    return currDir


def main():
    data = buildTree()
    #print(data)
    #print(calcDirSize2(data, ['/'], [], 0))
    totalSize = calcDirSize2(data, ['/'], [], 0)[0]
    minimumSize = 30000000 - (70000000 - totalSize)
    size, bigDirs = calcDirSize2(data, ['/'], [], minimumSize)
    print(min(bigDirs))

main()