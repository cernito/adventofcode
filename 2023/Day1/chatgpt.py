import re

# Define the mapping from word to digit
digit_map = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

# Create a regex pattern that matches either digits or digit words
pattern = re.compile(r'\b(zero|one|two|three|four|five|six|seven|eight|nine|\d)\b')

def get_first_last_digit(line):
    matches = pattern.findall(line)
    if not matches:
        return None, None
    first_digit = matches[0]
    last_digit = matches[-1]
    # Convert digit words to digits
    first_digit = digit_map.get(first_digit, first_digit)
    last_digit = digit_map.get(last_digit, last_digit)
    return int(first_digit), int(last_digit)

def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        first_digit, last_digit = get_first_last_digit(line)
        if first_digit is not None and last_digit is not None:
            total_sum += first_digit * 10 + last_digit
    return total_sum

# Example usage
lines = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

result = calculate_sum(lines)
print(result)  # This should print the correct sum based on the input
