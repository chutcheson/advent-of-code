import re
from collections import defaultdict
from bisect import bisect_left

def parse_input(file_text):
    regex_patterns = [
        r'seeds:(.*?)seed-to-soil map:',
        r'seed-to-soil map:(.*?)soil-to-fertilizer map:',
        r'soil-to-fertilizer map:(.*?)fertilizer-to-water map:',
        r'fertilizer-to-water map:(.*?)water-to-light map:',
        r'water-to-light map:(.*?)light-to-temperature map:',
        r'light-to-temperature map:(.*?)temperature-to-humidity map:',
        r'temperature-to-humidity map:(.*?)humidity-to-location map:',
        r'humidity-to-location map:(.*)'
    ]

    seeds = None

    parameter_maps = defaultdict(list)

    for i, pattern in enumerate(regex_patterns):
        section_text = re.search(pattern, file_text, re.DOTALL).group(1).strip() if re.search(pattern, file_text, re.DOTALL) else ''
        if i == 0:  # Special handling for seeds
            seeds = [int(x) for x in section_text.split()] if section_text else []
        else:
            for line in section_text.splitlines():
                line = line.strip()
                if line:
                    v0, v1, v2 = [int(x) for x in line.split()]
                    parameter_maps[i].append([v1, v2, v0])
            parameter_maps[i].sort()

    return seeds, parameter_maps

def find_path(seeds, parameter_map):
    accumulator = float('inf')

    def binary_search(arr, x):
        i = bisect_left(arr, [x, float('inf'), float('inf')])
        if i:
            return arr[i-1] if arr[i-1][0] <= x else None
        return None

    for seed in seeds:
        path = [seed]
        for range_index in range(1, 8):
            result = binary_search(parameter_map[range_index], path[-1])
            if result is None:
                path.append(path[-1])
            else:
                r0, r1, r2 = result
                if r0 <= path[-1] <= r0 + r1 - 1:
                    path.append(path[-1] - r0 + r2)
                else:
                    path.append(path[-1])
        accumulator = min(accumulator, path[-1])

    return accumulator


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        file_text = file.read()
    seeds, parameter_maps = parse_input(file_text)
    print(find_path(seeds, parameter_maps))
