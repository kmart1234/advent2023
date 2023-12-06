import re

text_file = open("input.txt")
#text_file = open("test.txt")
data = text_file.read()
text_file.close()

running_total = 0

game_number = 1
for line in data.splitlines():
    print(f"Original line: {line}")
    print(f"Game number {game_number}")
    game_possible = True

    max_red, max_green, max_blue = 0, 0, 0

    shows = line.split(": ")[1]
    shows = shows.replace(" ", "")

    show_number = 1
    for show in shows.split(";"):
        print(f"{show_number}th show in game {game_number} contained: {show}")
        show_number+=1
        for cube in show.split(","):
            #print(cube)
            color = re.sub(r'\d+', '', cube)
            count = re.sub(r'\D+', '', cube)
            #print(f"Elf showed {count} {color} cubes")

            if color == "red" and int(count) > int(max_red):
                max_red = count

            if color == "green" and int(count) > int(max_green):
                max_green = count

            if color == "blue" and int(count) > int(max_blue):
                max_blue = count

            show_power = int(max_red) * int(max_green) * int(max_blue)
            print(f"Power of show {show_number} is {show_power}")

    running_total+=show_power

    print(f"Running total is {running_total}")
    game_number+=1
    print("")

