def count_winners(winning_numbers, my_numbers):
    num_matches = 0
    
    for number in my_numbers:
        #print(f"Checking to see if {number} is a winning number")
        if number in winning_numbers:
            #print("My number is a winning number")
            num_matches+=1
            #print(f"There have been {num_matches} winning numbers this game")

    #print(f"There were {num_matches} matches in this game.")        
    return(num_matches)


text_file = open("input.txt")
#text_file = open("test.txt")
data = text_file.read()
text_file.close()

all_cards = []
game_num = 1

# Make a card for each line in the input file and add to a list
for line in data.splitlines():
    #print(line)

    game = line.split(": ")[1]
    winning_numbers = game.split(" | ")[0].split()
    my_numbers = game.split(" | ")[1].split()

    card = {"game_num": game_num, "winning_numbers": winning_numbers, "my_numbers": my_numbers, "copies": 1}
    all_cards.append(card)

    game_num+=1

# Evaluate number of matches, and adjust number of copies of cards
for card in all_cards:
    print(card)
    winners = count_winners(card['winning_numbers'], card['my_numbers'])
    if winners == 0:
        print("Card had no winners, don't need to increment copies of any cards")
    else:
        print(f"Card had {winners} winners, so add one to copies attribute of next {winners} cards")

        cards_to_increment = range(card['game_num']+1, card['game_num']+winners+1)
        #print(f"... which is {cards_to_increment}")

        for inc in cards_to_increment:
            print(f"Incrementing copies of card number {inc}")
            all_cards[inc-1]['copies']+=(1*card['copies'])
    
    print("")

# Final loop to count up total copies
total_copies = 0
for card in all_cards:
    total_copies+=card['copies']

print(f"Total copies: {total_copies}")



    