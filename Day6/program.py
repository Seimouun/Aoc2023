from functools import reduce
import math

def part1():
    with open('input.txt') as file:
        ans = []
        lines = file.readlines()
        n_lines = [list(map(lambda numb: int(numb), line.split()[1:])) for line in lines]
        times, distance = (n_lines[0], n_lines[1])
        for time_index, time in enumerate(times):
            start_index, end_index = (-1, -1)
            for time_held in range(time):
                dist = time_held * (time - time_held)
                if dist > distance[time_index] and start_index < 0:
                    start_index = time_held
                elif dist < distance[time_index] and start_index >= 0:
                    end_index = time_held
                    break
            ans.append(end_index - start_index)
        print(reduce(lambda x, y: x * y, ans))

def part2():
    with open('input.txt') as file:
        ans = []
        lines = file.readlines()
        n_lines = [int(''.join(line.split()[1:])) for line in lines]
        time, distance = (n_lines[0], n_lines[1])
        print(checkRange(0, time, distance, 0, time, False)-checkRange(0, time, distance, 0, time, True))
        

def checkRange(s_numb, e_numb, max_dist, s_max, e_max, small):
    numb = -1
    diff = e_numb - s_numb
    if diff == 1:
        return s_numb
    half_numb = math.floor((e_numb - s_numb) / 2) + s_numb
    dist = half_numb * ((e_max - s_max) - half_numb)
    if small:
        if dist > max_dist and s_numb < half_numb:
            numb = checkRange(s_numb, half_numb, max_dist, s_max, e_max, small)
        elif dist < max_dist and e_numb > half_numb:
            numb = checkRange(half_numb, e_numb, max_dist, s_max, e_max, small)
    else:
        if dist < max_dist and s_numb < half_numb:
            numb = checkRange(s_numb, half_numb, max_dist, s_max, e_max, small)
        elif dist > max_dist and e_numb > half_numb:
            numb = checkRange(half_numb, e_numb, max_dist, s_max, e_max, small)
    return numb
part2()