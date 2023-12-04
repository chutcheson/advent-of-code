import re

def process_file_content(file_text):
    points = 0
    lines = file_text.splitlines()
    for line in lines:
        line = line.strip()
        parts = re.split(r': |\|', line)
        portion1 = parts[0].strip()
        portion2 = set(parts[1].strip().split())
        portion3 = set(parts[2].strip().split())
        intersection = portion2.intersection(portion3)
        if len(intersection) > 0:
            points += 2 ** (len(intersection) - 1)
    return points

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        file_content = file.read()
    result = process_file_content(file_content)
    print(result)

