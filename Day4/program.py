import re
from functools import reduce

def part1():
    sum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        for line in lines:
            m = re.findall(r'(?<=[|:])[\s\d]*', line)
            m = list(map(lambda x: re.findall(r'\d+', x.lstrip().rstrip()), m))
            winners = list(filter(lambda x: x in list(m[1]), list(m[0])))
            score = pow(2, winners.__len__()-1)
            sum += score if score >= 1 else 0
        print(sum)

def part2():
    sum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        copies = {}
        for i, line in enumerate(lines):
            m = re.findall(r'(?<=[|:])[\s\d]*', line)
            m = list(map(lambda x: re.findall(r'\d+', x.lstrip().rstrip()), m))
            winners = list(filter(lambda x: x in list(m[1]), list(m[0])))
            copies_of_card = copies.get(i, 0)+1
            for x in range(1,len(winners)+1):
                copies[x+i] = copies.get(x+i, 0) + copies_of_card
            sum += copies_of_card
        
        print(sum)

part2()