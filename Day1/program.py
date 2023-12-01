import re
lut = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def part1():
    with open('input.txt') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            split = [*line]
            digits = list(filter(lambda char: char.isdigit(), split))
            numb = f'{digits[0]}{digits[digits.__len__()-1]}'
            sum += int(numb)
        print(sum)

def part2():
    with open('input.txt') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            regexFind = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))', line)
            mappedFind = list(map(lambda reg: lut.get(reg, reg), regexFind))
            numb = f'{mappedFind[0]}{mappedFind[mappedFind.__len__()-1]}'
            sum += int(numb)
        print(sum)

part2()