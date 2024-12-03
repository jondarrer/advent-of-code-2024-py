def calculate_result(input):
    number_of_safe_reports = 0

    for item in input:
        parts = item.split(' ')
        report = map(int, parts)
        if (is_report_safe(report)):
            number_of_safe_reports += 1

    return number_of_safe_reports

def is_report_safe(report):
    previous_level = None
    was_increasing = None

    for level in report:
        if (previous_level != None):
            diff = abs(previous_level - level)
            previous_level - level
            # Any two adjacent levels differ by at least one and at most three
            if (diff < 1 or diff > 3):
                return False
            # The levels are either all increasing or all decreasing
            if (was_increasing == None):
                if (previous_level - level < 0):
                    was_increasing = False
                else:
                    was_increasing = True
            elif (was_increasing):
                if (previous_level - level < 0):
                    return False
            else:
                if (previous_level - level > 0):
                    return False
        previous_level = level

    return True

if __name__ == '__main__':
    f = open("./src/day2/input.txt", "r")
    input = f.read().split("\n")
    print(calculate_result(input))