import re

regex = re.compile('mul\((\d{1,3},\d{1,3})\)')

def calculate_result(input):
    return 0

if __name__ == '__main__':
    f = open("./src/day3/input.txt", "r")
    input = f.read()
    print(calculate_result(input))