def main():
    with open("input_shreya") as f:
        reports = f.read().splitlines()
        print(reports)

    count, count_with_tolerance = safe_report_count(reports)
    print(count, count_with_tolerance)


def safe_report_count(reports):
    safe_count = 0
    safe_with_tolerance_count = 0
    for report in reports:
        line = report.split()
        report = [int(i) for i in line]
        if is_safe(report):
            safe_count += 1
        elif is_safe_with_tolerance(report):
            safe_with_tolerance_count += 1

    return safe_count, safe_count + safe_with_tolerance_count


def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return (all(x > 0 for x in differences) or all(x < 0 for x in differences)) and (
        all(1 <= abs(x) <= 3 for x in differences))


def is_safe_with_tolerance(report):
    if is_increasing(report):
        for i in range(1, len(report)):
            if report[i] < report[i - 1] or abs(report[i] - report[i - 1]) > 3 or report[i] - report[i - 1] == 0:
                return is_safe(report[:i] + report[i + 1:]) or is_safe(report[:i - 1] + report[i:])
    else:
        for i in range(1, len(report)):
            if report[i] > report[i - 1] or abs(report[i] - report[i - 1]) > 3 or report[i] - report[i - 1] == 0:
                return is_safe(report[:i] + report[i + 1:]) or is_safe(report[:i - 1] + report[i:])


def is_increasing(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return sum(x > 0 for x in differences) > sum(x < 0 for x in differences)
    # return report[0] + report[1] < report[len(report) - 2] + report[len(report) - 1]


if __name__ == "__main__":
    main()
