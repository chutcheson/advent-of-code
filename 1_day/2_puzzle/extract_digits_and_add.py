digit_trie = {
    "o": {
        "n": {
            "e": {
                "": "1"
            }
        }
    },
    "t": {
        "w": {
            "o": {
                "": "2"
            }
        },
        "h": {
            "r": {
                "e": {
                    "e": {
                        "": "3"
                    }
                }
            }
        }
    },
    "f": {
        "o": {
            "u": {
                "r": {
                    "": "4"
                }
            }
        },
        "i": {
            "v": {
                "e": {
                    "": "5"
                }
            }
        }
    },
    "s": {
        "i": {
            "x": {
                "": "6"
            }
        },
        "e": {
            "v": {
                "e": {
                    "n": {
                        "": "7"
                    }
                }
            }
        }
    },
    "e": {
        "i": {
            "g": {
                "h": {
                    "t": {
                        "": "8"
                    }
                }
            }
        }
    },
    "n": {
        "i": {
            "n": {
                "e": {
                    "": "9"
                }
            }
        }
    },
    "1": {
        "": "1"
    },
    "2": {
        "": "2"
    },
    "3": {
        "": "3"
    },
    "4": {
        "": "4"
    },
    "5": {
        "": "5"
    },
    "6": {
        "": "6"
    },
    "7": {
        "": "7"
    },
    "8": {
        "": "8"
    },
    "9": {
        "": "9"
    }
}

def extract_digits_and_add(lines):
    """
    Extracts the first and last digits from the given lines, concatenates them and returns their sum.
    Some digits may be represented as words.
    """
    concatenated_first_and_last_total = 0

    for line in lines:
        line_digits = []

        forward_found = False
        forward_line_index = 0
        head = digit_trie

        while forward_line_index < len(line):
            lookahead_index = forward_line_index
            while lookahead_index < len(line) and line[lookahead_index] in head:
                head = head[line[lookahead_index]]
                if "" in head:
                    line_digits.append(head[""])
                    forward_found = True
                    break
                else:
                    lookahead_index += 1
            if not forward_found:
                forward_line_index += 1
                head = digit_trie
            else:
                break

        backward_found = False
        backward_line_index = len(line) - 1
        head = digit_trie

        while backward_line_index >= 0:
            lookahead_index = backward_line_index
            while lookahead_index < len(line) and line[lookahead_index] in head:
                head = head[line[lookahead_index]]
                if "" in head:
                    line_digits.append(head[""])
                    backward_found = True
                    break
                else:
                    lookahead_index += 1
            if not backward_found:
                backward_line_index -= 1
                head = digit_trie
            else:
                break

        concatenated_first_and_last_total += int(line_digits[0] + line_digits[-1])

    return concatenated_first_and_last_total

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(extract_digits_and_add(lines))



