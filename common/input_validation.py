"""
Contains input validation functions
"""


def get_numeric(prompt_text, range_start, range_end):
    input_num = -1
    
    while input_num == -1:
        attempted_input = input(prompt_text)
        if attempted_input.isdigit():
            input_num = int(attempted_input)
            if not range_start <= input_num <= range_end:
                input_num = -1
                print(f'Input out of range ({range_start}-{range_end})')#
        else:
            print('Input specified must be number')
    
    return input_num