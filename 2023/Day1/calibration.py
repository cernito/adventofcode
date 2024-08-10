# Day 1 | Advent of Code

# Using regular expresions for the Part Two.

# --- Part One and Two ---
import re

digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
          6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}


pattern = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|\d)\b')


def find_calibration_digits(string):
    """
    Part One

    Finds the first and the last digit in the given string.
    """
    first_digit = None
    last_digit = None

    first_digit_idx = len(string)
    last_digit_idx = -1

    # Search first digit from the start of string
    idx = 0
    for char in string:
        if char.isdigit():
            first_digit = char
            first_digit_idx = idx
            break
        idx += 1

    # Search the last digit
    # (meaning search the first digit from the reversed string)
    idx = 0
    for char in reversed(string):
        if char.isdigit():
            last_digit = char
            last_digit_idx = len(string) - idx - 1
            break
        idx += 1

    return [first_digit, first_digit_idx], [last_digit, last_digit_idx]


def find_calibration_words(line):
    """
    Part Two

    Finds first and last digits spelled out with letters.
    """
    first_digit = None
    last_digit = None

    first_word_idx = len(line)
    last_word_idx = -1

    for i in range(1, 10):
        match = re.search(f"{digits[i]}", line)
        if match:

            # First word
            if match.start() < first_word_idx:
                first_word_idx = match.start()
                first_digit = str(i)

            # Last word
            for match in re.finditer(f"{digits[i]}", line):
                pass

            if match.start() > last_word_idx:
                last_word_idx = match.start()
                last_digit = str(i)

    return [first_digit, first_word_idx], [last_digit, last_word_idx]


def compute_calibration_vals():
    """
    Find calibration values on all lines in file.
    """
    calibration_values = []
    with open("input.txt", "r") as file:

        for line in file:

            # Part One
            [first_digit, first_digit_idx], [last_digit, last_digit_idx] = find_calibration_digits(line)

            # Part Two
            [first_word, first_word_idx], [last_word, last_word_idx] = find_calibration_words(line)

            first = first_digit if first_digit_idx < first_word_idx else first_word
            last = last_digit if last_digit_idx > last_word_idx else last_word

            calib_val = first + last
            calibration_values.append(calib_val)

    return calibration_values


def sum_vals(values):
    """
    Sums up all the calibration values.
    """
    total_sum = 0
    for val in values:
        total_sum += int(val)
    return total_sum


def main():
    calibration_values = compute_calibration_vals()
    result = sum_vals(calibration_values)
    print(result)


main()
