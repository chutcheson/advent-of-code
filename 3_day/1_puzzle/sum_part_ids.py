def first_function(lines):
    col1 = set()
    col2 = []

    for line_number, line in enumerate(lines):
        line = line.strip()

        i = 0
        while i < len(line):
            char = line[i]
            
            if char == ".":
                pass
            elif char.isdigit():
                start = i
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                value = int(line[start:i + 1])
                locations = [(line_number, j) for j in range(start, i + 1)]
                col2.append([value, locations])
            else:
                col1.add((line_number, i))
            i += 1

    return col1, col2

def second_function(col1, col2):
    col = 0

    for value, locations in col2:
        for loc in locations:
            x, y = loc
            adjacent = [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
            if any(adj_loc in col1 for adj_loc in adjacent):
                col += value
                break

    return col

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
    col1, col2 = first_function(lines)
    col = second_function(col1, col2)
    print(col)
