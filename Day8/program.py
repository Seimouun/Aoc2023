import math
nodes = {}
dirs = []
def setup():
    global dirs
    with open('input.txt') as file:
        lines = [line.replace('\n','') for line in file.readlines()]
        dirs = [*lines[0].strip()]
        for line in lines[2:]:
            s = line.split(' = ')
            loc = s[0]
            nodes[loc] = s[1].replace('(','').replace(')','').split(', ')

def part1():
    setup()
    curr_loc = 'AAA'
    step = 0
    while not curr_loc == 'ZZZ':
        if dirs[step % len(dirs)] == 'R':
            curr_loc = nodes[curr_loc][1]
        elif dirs[step % len(dirs)] == 'L':
            curr_loc = nodes[curr_loc][0]
        step += 1
    print(step)

def part2():
    setup()
    loc_nodes = [node for node in nodes.keys() if node.endswith('A')]
    ends = []
    for loc in loc_nodes:
        curr_loc = loc
        step = 0
        while not curr_loc.endswith('Z'):
            if dirs[step % len(dirs)] == 'R':
                curr_loc = nodes[curr_loc][1]
            elif dirs[step % len(dirs)] == 'L':
                curr_loc = nodes[curr_loc][0]
            step += 1
        ends.append(step)
    print(math.lcm(*ends))

part2()