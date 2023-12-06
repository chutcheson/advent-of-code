import math
from bisect import bisect_left, bisect_right

def process_file_text(file_text):
    # Split the text into lines
    lines = file_text.split('\n')

    # Process the first line
    first_line = lines[0].strip()
    time = int("".join(first_line.split()[1:]))

    # Process the second line
    second_line = lines[1].strip()
    distance = int("".join(second_line.split()[1:]))

    return time, distance

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

def calculate_accumulator(time, distance):

    mid_time = time // 2
    increasing_func = lambda w: (time - w) * w
    decreasing_func = lambda w: (time - w) * w

    low = binary_search_increasing(increasing_func, distance + 1, 0, mid_time)
    high = binary_search_decreasing(decreasing_func, distance, mid_time, time)

    return (high - low + 1)

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        file_text = file.read()

    time, distance = process_file_text(file_text)
    print(calculate_accumulator(time, distance))

