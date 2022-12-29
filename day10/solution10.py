def addToSigStr(cycleNo, xReg, sigStr):
    cycles = [20 * i for i in range(1, 12, 2)]
    if cycleNo in cycles:
        sigStr.append(xReg * cycleNo)
    return sigStr


def crt(cycle, xReg):
    sprite = [xReg + i for i in [-1, 0, 1]]
    offset = 40 * (cycle // 40) + 1
    if cycle - offset in sprite:
        return '#'
    else:
        return '.'


def main():
    cycle = 1
    xRegister = 1
    signalStrenghts = []
    output = []
    with open('input202210.txt') as file:
        for line in file.readlines():
            line = line.split()
            if line[0] == 'noop':
                signalStrenghts = addToSigStr(cycle, 
                xRegister, signalStrenghts)
                output.append(crt(cycle, xRegister))
                cycle += 1
            else:
                for i in range(2):
                    if cycle == 220:
                        print(line[1])
                    signalStrenghts = addToSigStr(cycle, 
                    xRegister, signalStrenghts)
                    output.append(crt(cycle, xRegister))
                    cycle += 1
                    if i == 1:
                        xRegister += int(line[1])
    for i in range(0, 240, 40):
        print(*output[i: i + 40])


main()


