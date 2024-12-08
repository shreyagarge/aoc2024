import re

def main():
    with open("input_shreya") as f:
        corrupted_memory = f.read()
        pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"

        matches = re.findall(pattern, corrupted_memory)

        total_sum = 0
        for x, y in matches:
            total_sum += int(x) * int(y)

        print(total_sum)

if __name__ == "__main__":
    main()


