with open("puzzle.txt", "r") as puzzle:
    game_sum = 0
    for line in puzzle:
        first_split = line.split(":")
        set_split = first_split[1].split(";")

        min_green = 1
        min_blue = 1
        min_red = 1

        for set in set_split:
            game_set = set.split(",")
            for pull in game_set:
                pull = ''.join(pull.split())
                if "green" in pull:
                    end = pull.find("green")
                    green = int(pull[0:end])
                    if green > min_green:
                        min_green = green

                if "red" in pull:
                    end = pull.find("red")
                    red = int(pull[0:end])
                    if red > min_red:
                        min_red = red

                if "blue" in pull:
                    end = pull.find("blue")
                    blue = int(pull[0:end])
                    if blue > min_blue:
                        min_blue = blue

        power_set = min_green * min_blue * min_red
        game_sum += power_set
    print(game_sum)