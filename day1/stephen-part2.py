import collections


def main():
    with open("input_stephen") as f:
        raw = f.read().splitlines()

    left, right = zip(*[(int(a), int(b)) for a, b in (line.split() for line in raw)])

    left_counts = collections.Counter(left)
    right_counts = collections.Counter(right)

    print(sum(n * left_counts[n] * right_counts[n] for n in left_counts))


if __name__ == "__main__":
    main()