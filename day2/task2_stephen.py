import collections, itertools


def main(path_input):
    with open(path_input) as f:
        raw_reports = f.read().splitlines()

    reports = [[int(v) for v in raw_report.split()] for raw_report in raw_reports]

    print(collections.Counter(is_safe_with_tolerance( report) for report in reports))


def is_safe_with_tolerance(report):
    print(report)
    if is_safe(report):
        print("Safe")
        return True
    else:
        for i in range(len(report)):
            before = report[:i]
            after = report[i+1:]
            print(before, after)
            if is_safe(before + after):
                print(f"Safe without index {i}")
                return True
        print("Unsafe")
        return False


def is_safe(report):
    diffs = [a-b for a,b in itertools.pairwise(report)]
    return all(1 <= diff <= 3 for diff in diffs) or all(1 <= -diff <= 3 for diff in diffs)


if __name__ == "__main__":
    main("input_stephen")