def stringToList(data):
    out = []
    i = 0
    num = ''
    while i < len(data):
        char = data[i]
        if char == ',':
            i += 1
            if num:
                out.append(int(num))
                num = ''
            continue
        elif char == '[':
            i += 1
            innerList, j = stringToList(data[i:])
            out.append(innerList)
            i += j
        elif char == ']':
            i += 1
            if num:
                out.append(int(num))
                num = ''
            return out, i
        else:
            i += 1
            num += char
            #out.append(int(char))
    return out


def getData():
    data = []
    with open('input202213.txt') as file:
        for line in file.readlines():
            line = line.strip("\n")
            if line:
                data.append(
                    stringToList(line)[0]
                    )
    return data


def comparer(lhs, rhs):
    #print(lhs, rhs)
    for j in range(len(lhs)):
        try:
            if type(lhs[j]) == int and type(rhs[j]) == int:
                #print(lhs[j], rhs[j])
                if lhs[j] == rhs[j]:
                    continue
                elif lhs[j] < rhs[j]:
                    return True
                else:
                    return False
            else: # at least one of them is not an int
                #print("list found, ", lhs, rhs)
                if type(lhs[j]) == int:
                    lhs[j] = [lhs[j]]
                if type(rhs[j]) == int:
                    rhs[j] = [rhs[j]]
                inner = comparer(lhs[j], rhs[j])
                if inner != 'even':
                    return inner
        except IndexError:
            #print('test')
            return False
    if len(rhs) > len(lhs):
        return True
    elif len(rhs) == len(lhs):
        return "even"


    #i = 0
    #while True:
    #    lhsElem = lhs[i]
    #    rhsElem = rhs[i]
    #    if type(lhsElem) == int and type(rhsElem) == list:
    #        lhsElem = list(lhsElem)
    #        continue
    #    if type(lhsElem) == int and type(rhsElem) == int:
    #        if lhsElem == rhsElem:
    #            i += 1
    #            continue
    #        elif lhsElem < rhsElem:
    #            return True
    #        else:
    #            return False

def task1(signal):
    indiciesRaw = []
    indicies = []
    for i in range(0, len(signal), 2):
        lhs = signal[i]
        rhs = signal[i+1]
        if comparer(lhs, rhs):
            indiciesRaw.append(i)
            indicies.append(int((i/2) + 1))
    return indicies, indiciesRaw

        
def main():
    dataPackets = getData()
    #print(dataPackets)
    answer, raw = task1(dataPackets)
    print(answer, sum(answer), len(answer))
    #for i in raw:
    #    print(dataPackets[i], dataPackets[i+1])

main()