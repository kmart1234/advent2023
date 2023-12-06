# Part 2 in progress


import re

# Pass in coordinate of arbitrary number symbol, look forward and backward to return a complete part number
def complete_part_number(row, col):
    print(f"Complete_part_number called with row:{row} and col:{col}")
    full_part_number = ""

    # Look backward until hitting a non-number symbol or edge to find leftmost position
    pending_part_number = True
    symbol = schematic[row][col]
    col_pointer = col

    while symbol.isdigit() == True and pending_part_number == True:
        col_pointer-=1 
        symbol = schematic[row][col_pointer]
        #print(f"Moving to the left, the symbol is {symbol}")

    left_boundary = col_pointer+1
    #print(f"Found left boundary of part number: column {left_boundary}")

    # Look forward until hitting a non-number symbol or edge to right rightmost position
    pending_part_number = True
    symbol = schematic[row][col]
    col_pointer = col

    #while symbol.isdigit() == True and pending_part_number == True:
    while symbol.isdigit() == True and pending_part_number == True and col_pointer < len(schematic[0])-1:
        col_pointer+=1 
        symbol = schematic[row][col_pointer]
        #print(f"Moving to the right, the symbol is {symbol}")

    right_boundary = col_pointer-1
    #print(f"Found right boundary of part number: column {right_boundary}")

    # Now we know the left and right boundaries of the part number, plus the column, so we can construct the full part number
    for col in range(left_boundary, right_boundary+1):
        full_part_number+=str(schematic[row][col])

    print(f"Full part number is: {full_part_number}")
    return(full_part_number)


# Iterate through list of coordinates and return ratio if it's a valid gear, or 0 if it's not
def check_adjacent_coords(adjacent_coords):

    part_numbers = []        # Make a list to hold valid part numbers

    for adjacent_coord in adjacent_coords:
        print(f"Checking adjacent coordinate in schematic: {adjacent_coord}")
        symbol = schematic[adjacent_coord['row']][adjacent_coord['col']]
        print(f"Value is: {symbol}")
        if re.match(r'[0-9]', symbol) is not None:
            print("Numeric character found!")
            # Look ahead/behind to get full numbers 
            part_numbers.append(complete_part_number(adjacent_coord['row'],adjacent_coord['col']))
    
    #print(f"After checking all adjacent coordinates, we have a set of part numbers:")
    part_number_set = set(part_numbers)
    #print(part_number_set)
    if len(part_number_set) == 2:      # Valid gear
        # return product of gears
        product = 1
        for item in part_number_set:
            #print(item)
            product = product*int(item)
        return(product)
    else:
        return 0


# Determine adjacent coordinates of a given coordinate, return list of coordinates
def determine_adjacency(row, col):
    adjacent_coords = []        # Define as [{row:row, col:col}, ...]

    # I looked at my input and don't see any gear indicators along any edge, so this is simpler
    adjacent_coords.append({"row": row-1, "col": col-1})
    adjacent_coords.append({"row": row-1, "col": col})
    adjacent_coords.append({"row": row-1, "col": col+1})
    adjacent_coords.append({"row": row,   "col": col-1})
    adjacent_coords.append({"row": row,   "col": col+1})
    adjacent_coords.append({"row": row+1, "col": col-1})
    adjacent_coords.append({"row": row+1, "col": col})
    adjacent_coords.append({"row": row+1, "col": col+1})
            
    return(adjacent_coords)


text_file = open("input.txt")
#text_file = open("test.txt")
#text_file = open("test2.txt")
data = text_file.read()
text_file.close()


# Build matrix for lookups
schematic = []
num_rows = 0
for line in data.splitlines():
    #print(line)
    num_cols = 0
    schematic_row = []
    for character in line:
        schematic_row.append(character)
        num_cols+=1
    schematic.append(schematic_row)
    num_rows+=1

# Iterate through matrix looking for gear indicators ("*")
cur_row = 0
total_ratio = 0

for schematic_row in schematic:             # Traverse each row
    #print(schematic_row)
    cur_col = 0
    for character in schematic_row:         # Traverse each column
        if character == "*":
            print(f"Found gear indicator at position: {cur_row}, {cur_col}")
            adjacent_coordinates = determine_adjacency(cur_row, cur_col)       # determine adjacent coordinates (neighbors)

            # Check all neighbors to see if they're numbers (two neighbors that are numbers means it's a valid gear), and get product (ratio) if there are two
            ratio = check_adjacent_coords(adjacent_coordinates)
            print(f"This gear indicator had a ratio of {ratio}")
            total_ratio+=ratio
            print(f"total ratio is: {total_ratio}")

        cur_col+=1
    print("")
    cur_row+=1

print(f"total ratio is: {total_ratio}")
print("")





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