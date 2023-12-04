import re

litterals = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
litteral_pattern = "|".join(litterals.keys())
number_pattern = "|".join(litterals.values())
global_pattern = number_pattern + "|" + litteral_pattern

def get_first_number(source_str: str) -> int:
    source = list(source_str)
    for i in source:
        try:
            int(i)
            return i
        except ValueError:
            continue

def get_first_and_last_of_pattern(pattern: str, source_str: str) -> tuple[re.Match, re.Match] | None:
    matches = re.findall(f"({pattern}).*({pattern})", source_str)
    if not matches:
        match = re.search(pattern, source_str).group()
        return match, match
    return matches[0]


# FIRST STAR
# with open('source_day1.txt') as f:
#     result = 0
#     for line in f:
#         first_number=get_first_number(line)
#         last_number=get_first_number(line[::-1])
#         result += int(first_number + last_number)
#     print(result)

# SECOND STAR
with open('source_day1.txt') as f:
    result = 0
    for line in f:
        first, last = get_first_and_last_of_pattern(global_pattern, line)
        first = litterals[first] if first in litterals.keys() else first
        last = litterals[last] if last in litterals.keys() else last
        result += int(first + last)
    print(result)



