import re

def process_file_text(file_text):
    lines = file_text.splitlines()
    acc = [1] * len(lines)
    
    for line_index in reversed(range(len(lines))):
        line = lines[line_index].strip()
        portions = re.split(r': |\|', line)
        portion2 = set(portions[1].strip().split())
        portion3 = set(portions[2].strip().split())
        
        intersection = portion2.intersection(portion3)
        if len(intersection) > 0:
            for i in range(line_index + 1, line_index + len(intersection) + 1):
                if i < len(acc):  # Ensure the index does not go out of bounds
                    acc[line_index] += acc[i]
                    
    return sum(acc)

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        file_content = file.read()
    result = process_file_text(file_content)
    print(result)

