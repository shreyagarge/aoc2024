import re

def main():
    with open("input_shreya") as f:
        corrupted_memory = f.read()
        do_mul(corrupted_memory)
        do_mul_with_filter(corrupted_memory)


def do_mul(corrupted_memory):
    pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
    matches = re.findall(pattern, corrupted_memory)
    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)
    print(total_sum)


def do_mul_with_filter(corrupted_memory):
    dont_indexes = [match.start() for match in re.finditer(r"don't\(\)", corrupted_memory)]
    do_indexes = [match.start() for match in re.finditer(r"do\(\)", corrupted_memory)]

    dodontmap = {}
    for value in do_indexes:
        dodontmap[value] = "do"

    for value in dont_indexes:
        dodontmap[value] = "dont"

    squashed_map = {}
    previous_value = None

    for key in sorted(dodontmap.keys()):
        value = dodontmap[key]
        if value != previous_value:
            squashed_map[key] = value
        previous_value = value

    print(squashed_map)

    indexes = sorted(squashed_map.keys())

    ranges_to_remove = []
    for i in range(len(indexes) - 1):
        start = indexes[i]
        end = indexes[i + 1]

        if squashed_map[start] == 'dont' and squashed_map[end] == 'do':
            ranges_to_remove.append((start, end))

    filtered_memory = ""
    current_position = 0
    for start, end in ranges_to_remove:
        filtered_memory += corrupted_memory[current_position:start]
        current_position = end  # Skip to the end of the "do"

    filtered_memory += corrupted_memory[current_position:]
    print(do_mul(filtered_memory))


if __name__ == "__main__":
    main()


