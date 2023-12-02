def find_values(line):
    vals = {}

    for char in enumerate(line):
        if char[1].isdigit():
            vals[char[0]] = char[1]

    left = int(vals[min(vals)])
    right = int(vals[max(vals)])

    return left, right


if __name__ == "__main__":
    total_sum = 0
    with open("puzzle.txt", "r") as puzzle:
        for line in puzzle:
            left, right = find_values(line)
            line_total = left * 10 + right
            total_sum += line_total

    print(total_sum)
