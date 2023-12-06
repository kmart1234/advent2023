import re


def check_spelled_numbers(line):
    spelled_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    spelled_numbers_present = False

    for number in spelled_numbers:
        #print(f"Checking for {number} in {line}")
        if number in line:
            spelled_numbers_present = True
        else:
            continue

    return(spelled_numbers_present)


def replace_spelled_numbers(line):
    fixed_ones = line.replace("one", "1")
    fixed_twos = fixed_ones.replace("two", "2")
    fixed_threes = fixed_twos.replace("three", "3")
    fixed_fours = fixed_threes.replace("four", "4")
    fixed_fives = fixed_fours.replace("five", "5")
    fixed_sixes = fixed_fives.replace("six", "6")
    fixed_sevens = fixed_sixes.replace("seven", "7")
    fixed_eights = fixed_sevens.replace("eight", "8")
    fixed_nines = fixed_eights.replace("nine", "9")
    return(fixed_nines)


def fix_line(line):
    #print(f"Original line: {line}")
    fixed_line = line
    while check_spelled_numbers(fixed_line) == True:
        fixed_line = replace_spelled_numbers(line)
    
    return(fixed_line)


text_file = open("test.txt")
data = text_file.read()
text_file.close()

running_total = 0

for line in data.splitlines():
    print(f"Original line: {line}")

    fixed_line = fix_line(line)
    print(f"Fixed line is: {fixed_line}")

    numbers = re.sub(r'\D', '', fixed_line)
    #print(f"Only numbers: {numbers}")
    
    first_number = numbers[:1]
    #print(f"The first number is: {first_number}")
    
    if len(numbers) == 1:
        last_number = first_number
    else:
        last_number = numbers[-1:]

    #print(f"The last number is: {last_number}")

    two_digit = int(first_number + last_number)
    #print(f"The two digit number is then: {two_digit}")

    running_total+=two_digit

    print("")

print(f"After completing the file, the running total was: {running_total}")

