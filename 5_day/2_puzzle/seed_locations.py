import re
from collections import defaultdict
from bisect import bisect_right

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
            seeds = [[int(x), int(y)] for x, y in zip(section_text.split()[::2], section_text.split()[1::2])]
        else:
            for line in section_text.splitlines():
                line = line.strip()
                if line:
                    v0, v1, v2 = [int(x) for x in line.split()]
                    parameter_maps[i].append([v1, v1 + v2 - 1, v0 - v1])
            parameter_maps[i].sort()

            # Additional processing step
            processed_parameter_map = []
            previous = float('-inf')
            for element in parameter_maps[i]:
                v1, v2, delta = element
                if v1 != previous + 1:
                    processed_parameter_map.append([previous + 1, v1 - 1, 0])
                processed_parameter_map.append([v1, v2, delta])
                previous = v2
            processed_parameter_map.append([previous + 1, float('inf'), 0])
            parameter_maps[i] = processed_parameter_map

    return seeds, parameter_maps

def process_seeds(seeds, parameter_map):
    accumulator = float('inf')
    search = [[s[0], s[0] + s[1] - 1, 0] for s in seeds]

    while search:
        first, second, third = search.pop()

        if third == 7:
            accumulator = min(accumulator, first)
        else:
            index = bisect_right([p[0] for p in parameter_map[third + 1]], first) - 1
            source_start, source_end, transformation = parameter_map[third + 1][index]
            search.append([first + transformation, min(second, source_end) + transformation, third + 1])

            first = source_end + 1
            while second >= source_end:
                index += 1
                source_start, source_end, transformation = parameter_map[third + 1][index]
                search.append([max(first, source_start) + transformation, min(second, source_end) + transformation, third + 1])
                first = source_end + 1

    return accumulator


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        file_text = file.read()
    seeds, parameter_maps = parse_input(file_text)
    print(process_seeds(seeds, parameter_maps))
