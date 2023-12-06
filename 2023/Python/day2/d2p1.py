with open ("puzzle.txt", "r") as puzzle:
    game_sum = 0
    for line in puzzle:
        first_split = line.split(":")
        set_split = first_split[1].split(";")
        game_split = first_split[0].split(" ")
        game_num = game_split[1]
        
        set_tracker = 0
        green = 0
        red = 0
        blue = 0
        for set in set_split:
            game_set = set.split(",")
            for pull in game_set:
                pull = ''.join(pull.split())
                if "green" in pull:
                    end = pull.find("green")
                    green = int(pull[0:end])
                if "red" in pull:
                    end = pull.find("red")
                    red = int(pull[0:end])
                if "blue" in pull:
                    end = pull.find("blue")
                    blue = int(pull[0:end])
            if red <= 12 and green <= 13 and blue <= 14:
                set_tracker += 1
        if set_tracker == len(set_split):
            game_sum += int(game_num)
    print(game_sum)
