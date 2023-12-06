# This is working for part 1


import re

# Iterate through list of coordinates and return true if any are valid special characters
def check_adjacent_coords(adjacent_coords):
    for adjacent_coord in adjacent_coords:
        #print(f"Checking adjacent coordinate in schematic: {adjacent_coord}")
        symbol = schematic[adjacent_coord['row']][adjacent_coord['col']]
        #print(f"Value is: {symbol}")
        #if re.match(r'[^a-zA-Z0-9_]', symbol) is not None:
        if re.match(r'[^\w.]', symbol) is not None:
            #print("SPECIAL CHARACTER FOUND!")
            return(True)
    return(False)

text_file = open("input.txt")
#text_file = open("test.txt")
#text_file = open("test2.txt")
data = text_file.read()
text_file.close()

# Go over input file first time to build list of part numbers
part_numbers = []
row = 1
for line in data.splitlines():
    
    print(f"Original line: {line}")

    max_col = len(line)

    char_list = [char for char in line]

    print(char_list)

    pending_part_number = False
    start_col = 1
    part_number_value = ""
    col = 1
    for character in char_list:

        print(f"Figuring out character: {character} at position {col}")

        # Handling the beginning of a part number
        if character.isdigit() == True and pending_part_number == False:
            print("Beginning of part number")
            pending_part_number = True
            start_col = col
            part_number_value = character
            col+=1
            continue

        # Handling subsequent digit of a part number
        if character.isdigit() == True and pending_part_number == True:
            print("Subsequent digit in part number")
            part_number_value+=character
            col+=1
            continue

        # Handling first character after a part number
        if character.isdigit() == False and pending_part_number == True:
            print("First character after part number")
            pending_part_number = False
            end_col = col-1
            part_number_loc = {'row': row, 'start_col': start_col, 'end_col': end_col, 'value': part_number_value, 'validity': "unknown"}
            part_numbers.append(part_number_loc)
            part_number_value = "0"
            col+=1
            continue

        # Handling other non part number characters
        if character.isdigit() == False and pending_part_number == False:
            print("Another non-part number")
            col+=1
            continue

    # If we got to the end of the line and there was a pending_part_number (along right edge of input)
    if pending_part_number == True:
        print("Found end of part number along right edge")
        pending_part_number = False
        end_col = col-1
        part_number_loc = {'row': row, 'start_col': start_col, 'end_col': end_col, 'value': part_number_value, 'validity': "unknown"}
        part_numbers.append(part_number_loc)
        part_number_value = "0"
        col+=1

    row+=1
    print("")
print("")

# Go over input file a second time to build 2D array for later validity lookups
schematic = []
# Pad the array with a row of 0s to be consistent with part number list convention
# Peek ahead into the data to find the length of the lines
pad_line = ['0' for _ in range(len(data.splitlines()[0]))]
pad_line.append('0')
schematic.append(pad_line)
for line in data.splitlines():
    #print("Inside the loop")
    #print(line)
    schematic_row = []
    schematic_row.append("0")
    # Pad the line with a 0 to be consistent with part number list convention
    for character in line:
        schematic_row.append(character)
    schematic.append(schematic_row)

'''
print("Finished making 2d array")
for schematic_row in schematic:
    print(schematic_row)
print("")
print(f"coordinate (1,2) in schematic is: {schematic[1][2]}")
'''

# Enumerate all adjacent coordinates for all potentially valid part numbers, check their validity
last_row = row-1
#adjacent_coords = []        # Define as [{row:row, col:col}, ...]
sum_of_valid_part_numbers = 0
for part_number in part_numbers:
    print(part_number)
    all_part_number_cols = list(range(part_number['start_col'], part_number['end_col']+1))
    adjacent_coords = []        # Define as [{row:row, col:col}, ...]
    
    # Special cases:
        # Top left corner               X
        # Top right corner              X
        # Bottom left corner            X
        # Bottom right corner           X
        # Top row (non corner)          X
        # Along the left (non corner)   X
        # Along the right (non corner)  X
        # Bottom row (non corner)       X

    # Top left corner
    if part_number['row'] == 1 and part_number['start_col'] == 1:
        print("Top left corner")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})    # Right
        for col in all_part_number_cols:                                                        # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['end_col']+1})  # Diagonal D
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Top right corner
    if part_number['row'] == 1 and part_number['end_col'] == max_col:
        print("Top right corner")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
        for col in all_part_number_cols:                                                        # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['start_col']-1}) # Diagonal C
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Bottom left corner
    if part_number['row'] == last_row and part_number['start_col'] == 1:
        print("Bottom left corner")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})    # Right
        for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['end_col']+1})   # Diagonal B
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Bottom right corner
    if part_number['row'] == last_row and part_number['end_col'] == max_col:
        print("Bottom right corner")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
        for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['start_col']-1}) # Diagonal A
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Top row (non corner)
    if part_number['row'] == 1:
        print("Part number is on the top row")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
        adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})    # Right
        for col in all_part_number_cols:                                                        # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['start_col']-1}) # Diagonal C
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['end_col']+1})  # Diagonal D
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Bottom row (non corner)
    if part_number['row'] == last_row:
        print("Part number is on the last row")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
        adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})    # Right
        for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['start_col']-1}) # Diagonal A
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['end_col']+1})   # Diagonal B
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Along the left (non corner)
    if part_number['start_col'] == 1:
        print("Part number is along the left")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})    # Right
        for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
        for col in all_part_number_cols:                                                        # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['end_col']+1})   # Diagonal B
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['end_col']+1})  # Diagonal D
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Along the right (non corner)
    if part_number['end_col'] == max_col:
        print("Part number is along the right")
        adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
        for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
        for col in all_part_number_cols:                                                        # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
        adjacent_coords.append({"row": part_number['row']-1, "col": part_number['start_col']-1}) # Diagonal A
        adjacent_coords.append({"row": part_number['row']+1, "col": part_number['start_col']-1}) # Diagonal C
        valid_part_number = check_adjacent_coords(adjacent_coords)
        print(f"valid part number?: {valid_part_number}")
        if check_adjacent_coords(adjacent_coords) == True:
            sum_of_valid_part_numbers+=int(part_number['value'])
        continue

    # Catch-all (not along any edge/corner)
    print("Catch-all case")
    adjacent_coords.append({"row": part_number['row'], "col": part_number['start_col']-1})   # Left
    adjacent_coords.append({"row": part_number['row'], "col": part_number['end_col']+1})     # Right
    for col in all_part_number_cols:                                                         # Above
            adjacent_coord = {"row": part_number['row']-1, "col": col}
            adjacent_coords.append(adjacent_coord)
    for col in all_part_number_cols:                                                         # Below
            adjacent_coord = {"row": part_number['row']+1, "col": col}
            adjacent_coords.append(adjacent_coord)
    adjacent_coords.append({"row": part_number['row']-1, "col": part_number['start_col']-1}) # Diagonal A
    adjacent_coords.append({"row": part_number['row']-1, "col": part_number['end_col']+1})   # Diagonal B
    adjacent_coords.append({"row": part_number['row']+1, "col": part_number['start_col']-1}) # Diagonal C
    adjacent_coords.append({"row": part_number['row']+1, "col": part_number['end_col']+1})   # Diagonal D
    valid_part_number = check_adjacent_coords(adjacent_coords)
    print(f"valid part number?: {valid_part_number}")
    if check_adjacent_coords(adjacent_coords) == True:
        sum_of_valid_part_numbers+=int(part_number['value'])

print("")
print(f"After all that, the sum of the valid part number values is: {sum_of_valid_part_numbers}")
'''
print("")
print("Adjacent coordinates")
for adjacent_coord in adjacent_coords:
    print(adjacent_coord)
'''

