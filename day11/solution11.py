import re
from math import floor
import copy

def monkeyOperation(item, instructions):
    operand = instructions[1]
    if operand == 'old':
        return item * item
    else:
        instr = str(instructions[0] + instructions[1])
        return eval(str(item) + instr)


def monkeyTest(worryLevel, divisor):
    if not (worryLevel % divisor):
        return 't'
    else:
        return 'f'


def stuffSlinging(monkeys, lcm):
    for i in range(10000):
        for monkey in monkeys.values():
            currentItems = copy.copy(monkey['items'])
            for item in currentItems:
                monkey['items'].pop(0)
                newWorry = monkeyOperation(item, monkey['oper'])
                newWorry = newWorry % lcm # the result of the modulus is 
                monkey['inspections'] += 1 # equal in mod sense to newWorry
                divisorTest = monkeyTest(newWorry, monkey['test'])
                nextMonkey = str(monkey[divisorTest])
                monkeys[nextMonkey]['items'].append(newWorry)            
    inspections = [i['inspections'] for i in monkeys.values()]
    itms = [i['items'] for i in monkeys.values()]
    return inspections, itms


def main():
    monkeys = {}
    currentMonkey = 0
    lcm = 1
    with open('input202211.txt') as file:
        for line in file.readlines():
            lineList = line.split()
            nums = re.findall(r'\d+', line)
            if not lineList:
                continue
            if lineList[0] == 'Monkey':
                currentMonkey = nums[0]
                monkeys[currentMonkey] = {'inspections':0}
            elif lineList[0] == 'Starting':
                items = [int(i) for i in nums]
                monkeys[currentMonkey]['items'] = items
            elif lineList[0] == 'Operation:':
                monkeys[currentMonkey]['oper'] = lineList[-2:]
            elif lineList[0] == 'Test:':
                monkeys[currentMonkey]['test'] = int(nums[0])
                lcm *=  int(nums[0])
            elif lineList[1] == 'true:':
                monkeys[currentMonkey]['t'] = int(nums[0])
            elif lineList[1] == 'false:':
                monkeys[currentMonkey]['f'] = int(nums[0])
    insps, items = stuffSlinging(monkeys, lcm)
    insps.sort()
    monkeyBusiness = insps[-1] * insps[-2]
    print(monkeyBusiness)


main()