import re

# https://docs.python.org/3/howto/regex.html
p = re.compile(r'mul\((\d{1,3},\d{1,3})\)')

def calculate_result(input):
    result = 0
    matches = p.findall(input)
    for match in matches:
        factors = list(map(int, match.split(",")))
        result += factors[0] * factors[1]
    return result

if __name__ == '__main__':
    f = open("./src/day3/input.txt", "r")
    input = f.read()
    print(calculate_result(input))