from collections import Counter

def convert_card_value(card):
    """Convert card character to its numeric value."""
    if card in '23456789':
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14

def evaluate_hand(cards):
    """Evaluate the hand and return its score and the numeric values of the cards."""
    values = [convert_card_value(card) for card in cards]
    count = Counter(values)
    counts = list(count.values())

    if 5 in counts:
        return (7, values)
    if 4 in counts:
        return (6, values)
    if 3 in counts and 2 in counts:
        return (5, values)
    if 3 in counts:
        return (4, values)
    if counts.count(2) == 2:
        return (3, values) 
    if 2 in counts:
        return (2, values) 
    return (1, values)

def process_string(input_string):
    """Process the input string into a list of evaluated hands."""
    res = []
    for line in input_string.split("\n"):
        elements = line.split()
        if len(elements) != 2:
            continue 
        hand_score = evaluate_hand(elements[0])
        points = int(elements[1])
        res.append([hand_score, points])
    return res

def calculate_total_score(processed_data):
    """Calculate the total score from the processed data."""
    res = 0
    processed_data.sort()
    for index, (score, points) in enumerate(processed_data, start=1):
        res += points * index
    return res

if __name__ == '__main__':
    with open("input.txt") as f:
        input_string = f.read()
    processed_data = process_string(input_string)
    print(calculate_total_score(processed_data))
