text_file = open("input.txt")
#text_file = open("test.txt")
data = text_file.read()
text_file.close()

total_points = 0

for line in data.splitlines():
    #print(line)
    num_winners, game_points = 0, 1

    game = line.split(": ")[1]
    print(game)

    winning_numbers = game.split(" | ")[0].split()
    print(f"Winning numbers: {winning_numbers}")

    my_numbers = game.split(" | ")[1].split()
    print(f"My numbers: {my_numbers}")

    for number in my_numbers:
        #print(f"Checking to see if {number} is a winning number")
        if number in winning_numbers:
            #print("My number is a winning number")
            num_winners+=1
            game_points*=2
            #print(f"There have been {num_winners} winning numbers this game")

    if num_winners == 0:
        #print(f"There were no winners this game")
        game_points = 0
    else:
        #print(f"There were {num_winners} winners this game")
        game_points/=2

    print(f"There should be {int(game_points)} points awarded this game.")        
    print("")

    total_points+=int(game_points)

print(f"There should be {total_points} total points")
    