number_dict = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
        }


def find_left(line):
    vals = {}
    for num in number_dict:
        if line.find(num) > -1:
            vals[line.find(num)] = number_dict[num]

    for char in enumerate(line):
        if char[1].isdigit():
            vals[char[0]] = char[1]

    value = vals[min(vals)]

    return value

def find_right(line):
    vals = {}
    for num in number_dict:
        if line.find(num[::-1]) > -1:
            vals[line.find(num[::-1])] = number_dict[num]

    for char in enumerate(line):
        if char[1].isdigit():
            vals[char[0]] = char[1]

    value = vals[min(vals)]

    return value    


if __name__ == "__main__":
    total_sum = 0
    with open("puzzle.txt", "r") as puzzle:
        for line in puzzle:
            line_total = (int(find_left(line)) * 10) + int(find_right(line[::-1]))
            total_sum += line_total

    print(total_sum)