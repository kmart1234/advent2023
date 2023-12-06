import re



text_file = open("input.txt")
data = text_file.read()
text_file.close()

running_total = 0

for line in data.splitlines():
    #print(f"Original line: {line}")

    numbers = re.sub(r'\D', '', line)
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


print(f"After completing the file, the running total was: {running_total}")

# Answer is 54081