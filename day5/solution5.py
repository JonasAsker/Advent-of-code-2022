import re


def part1(instructions, crates):
    for move in instructions:
        craneLoad = crates[move[1]][:move[0] + 1][::-1]
        crates[move[1]] = crates[move[1]][move[0] + 1:]
        crates[move[2]] = [*craneLoad, *crates[move[2]]]
    topLayer = [i[0] for i in crates]
    return topLayer


def part2(instructions, crates):
    for move in instructions:
        craneLoad = crates[move[1]][:move[0] + 1]
        crates[move[1]] = crates[move[1]][move[0] + 1:]
        crates[move[2]] = [*craneLoad, *crates[move[2]]]
    topLayer = [i[0] for i in crates]
    return topLayer


def main():
    crates = []
    instructions = []
    with open('input20225.txt') as file:
        for line in file.readlines():
            if '[' in line:
                line = line.replace('    ', ' - ').split()
                crates.append(line)
            elif line != '\n' and 'm' in line:
                instruction = re.findall(r'\d+', line)
                instruction = [int(i) - 1 for i in instruction]
                instructions.append(instruction)
    cratesTranspose = list(map(list, zip(*crates)))
    cratesTranspose = [list(filter(lambda x :x != '-', i)) 
                            for i in cratesTranspose]
    crates = cratesTranspose
    print(part2(instructions, crates))
    
main()