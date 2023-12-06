import math
from bisect import bisect_left, bisect_right

def process_file_text(file_text):
    # Split the text into lines
    lines = file_text.split('\n')

    # Process the first line
    first_line = lines[0].strip()
    times = [int(value) for value in first_line.split()[1:]]  # Skipping the 0th value

    # Process the second line
    second_line = lines[1].strip()
    distances = [int(value) for value in second_line.split()[1:]]  # Skipping the 0th value

    # Pair the times and distances in a dictionary
    race = {index: (time, distance) for index, (time, distance) in enumerate(zip(times, distances))}

    return race

def binary_search_increasing(func, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if func(mid) < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def binary_search_decreasing(func, x, lo, hi):
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if func(mid) > x:
            lo = mid
        else:
            hi = mid - 1
    return lo

def calculate_accumulator(race_dict):
    accumulator = 1

    for key, (time, distance) in race_dict.items():
        mid_time = time // 2
        increasing_func = lambda w: (time - w) * w
        decreasing_func = lambda w: (time - w) * w

        low = binary_search_increasing(increasing_func, distance + 1, 0, mid_time)
        high = binary_search_decreasing(decreasing_func, distance, mid_time, time)

        accumulator *= (high - low + 1)

    return accumulator

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        file_text = file.read()

    race_results = process_file_text(file_text)
    print(calculate_accumulator(race_results))

