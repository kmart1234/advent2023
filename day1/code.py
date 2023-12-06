import re


def check_spelled_numbers(line):
    possible_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    found_numbers = []

    for number in possible_numbers:
        #print(f"Checking for {number} in line")
        position = line.find(number)
        if position == -1:
            continue
        else:
            found_number = {'starting_position' : position, 'value' : number}
            found_numbers.append(found_number)

    #Sort list based on position (it's appended in order of numeric value, not position)
    found_numbers = sorted(found_numbers, key=lambda x: x['starting_position'])
    print("Found the following spelled numbers in this line (after sorting):")
    for number in found_numbers:
        print(number)

    return(found_numbers)


def replace_single_number(line, number):

    print(f"replace_single_number called with line {line}, and number {number}")

    if number == "one":
        line = line.replace("one", "1")
    elif number == "two":
        line = line.replace("two", "2")
    elif number == "three":
        line = line.replace("three", "3")
    elif number == "four":
        line = line.replace("four", "4")
    elif number == "five":
        line = line.replace("five", "5")
    elif number == "six":
        line = line.replace("six", "6")
    elif number == "seven":
        line = line.replace("seven", "7")
    elif number == "eight":
        line = line.replace("eight", "8")
    elif number == "nine":
        line = line.replace("nine", "9")

    print(f"Returning updated line: {line}")
    return(line)


def fix_line(line):

    found_numbers = check_spelled_numbers(line)
    print(f"Initial check for spelled numbers returned {len(found_numbers)}")

    if len(found_numbers) == 1:
        line = replace_single_number(line, found_numbers[0]['value'])
    elif len(found_numbers) > 1:
        line = replace_single_number(line, found_numbers[0]['value'])       # replace first spelled number
        line = replace_single_number(line, found_numbers[-1]['value'])      # replace last spelled number

    return(line)
    
''' 
    # Replace all spelled numbers, left to right
    while len(found_numbers) > 0:

        line = replace_single_number(line, found_numbers[0]['value'])
        print(f"After replacing first spelled number in list, the line is: {line}")

        found_numbers = check_spelled_numbers(line)

    return(line)
'''



text_file = open("input.txt")
#text_file = open("test.txt")
data = text_file.read()
text_file.close()

running_total = 0

for line in data.splitlines():
    print(f"Original line: {line}")

    fixed_line = fix_line(line)                 # Convert spelled numbers to numbers
    print(f"Fixed line is: {fixed_line}")

    numbers = re.sub(r'\D', '', fixed_line)     # Remove all letters
    print(f"Only numbers: {numbers}")

    first_number = numbers[:1]
    print(f"The first number is: {first_number}")
    
    if len(numbers) == 1:
        last_number = first_number
    else:
        last_number = numbers[-1:]
    
    print(f"The last number is: {last_number}")

    two_digit = int(first_number + last_number)
    print(f"The two digit number is then: {two_digit}")

    running_total+=two_digit
    print(f"The running total is: {running_total}")

    print("")
    print("")

print(f"After completing the file, the running total was: {running_total}")

