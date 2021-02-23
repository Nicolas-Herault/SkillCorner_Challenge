"""
    Simple implementation of our print_lines function
"""
import json


def get_new_data(line_number: int, input_line: str) -> str:
    """
    Process the NEW_DATA line.

    Args:
        line_number, the number of the mine to process
        input_line, the line to process

    Return:
        the processed NEW_DATA line
    """
    if not line_number % 5:
        new_data = "Multiple de 5"
    elif '$' in input_line:
        new_data = input_line.replace(' ', '_')
    elif input_line[-2] == '.':
        new_data = input_line
    elif input_line[0] == '{':
        our_dict = json.loads(input_line)
        if not line_number % 2:
            our_dict['pair'] = True
        new_data = json.dumps(our_dict)
    else:
        new_data = "Rien à afficher"

    return new_data.replace('\n', '').replace('\r', '')
