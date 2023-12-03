from functools import reduce
lut = {
    'red': 12,
    'green': 13,
    'blue': 14
}
def part1():
    idsSum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        for line in lines:
            initSplit = line.split(':')
            gameId = int(initSplit[0].split(' ')[1])
            possible = True
            for cubes in initSplit[1].split(';'):
                cubesSplit = cubes.split(',')
                for cube in cubesSplit:
                    cubeSplit = cube.lstrip().split(' ')
                    cubeColor = cubeSplit[1].strip()
                    cubesAmount = int(cubeSplit[0])
                    if cubesAmount > lut[cubeColor]:
                        possible = False
            if possible:
                idsSum += gameId
        print(idsSum)

def part2():
    gamesSum = 0
    with open('input.txt') as file:
        lines = file.readlines()
        for line in lines:
            initSplit = line.split(':')
            maxRGB = {}
            for cubes in initSplit[1].split(';'):
                cubesSplit = cubes.split(',')
                for cube in cubesSplit:
                    cubeSplit = cube.lstrip().split(' ')
                    cubeColor = cubeSplit[1].strip()
                    cubesAmount = int(cubeSplit[0])
                    maxRGB[cubeColor] = max(maxRGB.get(cubeColor, -1), cubesAmount)
            reduction = reduce(lambda x,y: x * y, list(maxRGB.values()))
            gamesSum += reduction
        print(gamesSum)

part2()