import collections, itertools


def main():
    with open("input_stephen") as f:
        raw_reports = f.read().splitlines()

    reports = [[int(v) for v in raw_report.split()] for raw_report in raw_reports]

    print(collections.Counter(is_report_safe(report) for report in reports))


def is_report_safe(report):
    diffs = [a-b for a,b in itertools.pairwise(report)]
    return all(1 <= diff <= 3 for diff in diffs) or all (1 <= -diff <= 3 for diff in diffs)



if __name__ == "__main__":
    main()