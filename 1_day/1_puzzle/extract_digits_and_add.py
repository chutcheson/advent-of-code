import string

def extract_digits_and_add(lines):
    """Extracts the first and last digits from the given lines, concatenates them and returns their sum."""

    res = 0

    for line in lines:
        digits = []
        for char in line:
            if char in string.digits:
                digits.append(char)
        res += int(digits[0] + digits[-1])

    return res

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(extract_digits_and_add(lines))



