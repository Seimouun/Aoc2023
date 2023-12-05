seed_map = {}

def part1():
    with open('input.txt') as file:
        lines = file.readlines()
        seeds_to_plant = list(map(lambda x: int(x), lines[0].split(" ")[1:]))

        from_to_split = None
        from_map = {}

        for i, line in enumerate(lines[1:]):
            if not line.isspace():
                line=line.rstrip()
                from_to_split_temp = line.replace(' map:', '').split('-to-')
                if len(from_to_split_temp) > 1:
                    if len(from_map.keys()) > 0:
                        seed_map[from_to_split[0]] = from_map
                    from_map = {}
                    from_to_split = from_to_split_temp
                else:
                    numbs = list(map(lambda x: int(x),line.split(' ')))
                    from_obj = {
                        'range': numbs[2],
                        from_to_split[1]: numbs[0]
                    }
                    from_map[numbs[1]] = from_obj
                    if(i == len(lines[1:])-1):
                        seed_map[from_to_split[0]] = from_map
    print(min(getNextValue('seed', seed, seed, 0) for seed in seeds_to_plant))

def part2():
    with open('input.txt') as file:
        lines = file.readlines()
        seeds_to_plant = list(map(lambda x: int(x), lines[0].split(" ")[1:]))

        from_to_split = None
        from_map = {}

        for i, line in enumerate(lines[1:]):
            if not line.isspace():
                line=line.rstrip()
                from_to_split_temp = line.replace(' map:', '').split('-to-')
                if len(from_to_split_temp) > 1:
                    if len(from_map.keys()) > 0:
                        seed_map[from_to_split[0]] = from_map
                    from_map = {}
                    from_to_split = from_to_split_temp
                else:
                    numbs = list(map(lambda x: int(x),line.split(' ')))
                    t_range = (numbs[1], numbs[1] + numbs[2]-1)
                    from_obj = {
                        from_to_split[1]: (numbs[0], numbs[0] + numbs[2]-1)
                    }
                    from_map[t_range] = from_obj
                    if(i == len(lines[1:])-1):
                        seed_map[from_to_split[0]] = from_map
    ans = []
    for seed_range in [(seeds_to_plant[i], seeds_to_plant[i] + seeds_to_plant[i + 1]-1) for i in range(0, len(seeds_to_plant)-1, 2)]:
        ans.extend(getValueRange(seed_range, 'seed', 0))
    print(min(ans))

        
def getNextValue(category, id, seedId, step):
    for mapped_seed in seed_map[category]:
        maxSeed = seed_map[category][mapped_seed]['range'] + mapped_seed
        nextCategory = list(seed_map[category][mapped_seed].keys())[1]
        if mapped_seed <= id < maxSeed:
            mappedId = seed_map[category][mapped_seed][nextCategory] + id - mapped_seed
            if not nextCategory in seed_map.keys():
                return mappedId
            return getNextValue(nextCategory, mappedId, seedId, step+1)
    if not nextCategory in seed_map.keys():
        return id
    return getNextValue(nextCategory, id, seedId, step+1)

def getValueRange(initial_range, category, step):
    end_values = []
    start = initial_range[0]
    if not category in seed_map.keys():
        end_values.append(start)
        return end_values
    sub_ranges = seed_map[category]
    sorted_sub_ranges = dict(sorted(sub_ranges.items(), key=lambda item: item[0]))
    #print(f'{" "*step*2}sub_range:',sorted_sub_ranges)
    for i, range in enumerate(sorted_sub_ranges):
        sub_start = range[0]
        sub_end = range[1]
        sub_next_category = list(sorted_sub_ranges[range].keys())[0]
        sub_next_mapped = sorted_sub_ranges[range][sub_next_category]
        if(start > sub_end or initial_range[1] < sub_start):
            continue
        if start < sub_start:
            end_values.extend(getValueRange((start, sub_start), sub_next_category, step+1) or [])
            start = sub_start
            
        t_start = sub_next_mapped[0] + start - sub_start
        t_end = sub_next_mapped[1] + min(sub_end, initial_range[1]) - sub_end
        end_values.extend(getValueRange((t_start, t_end), sub_next_category, step+1) or [])
        start = sub_end+1
    if start < initial_range[1]:
        end_values.extend(getValueRange((start, initial_range[1]), sub_next_category, step+1) or [])
    return end_values


part1()