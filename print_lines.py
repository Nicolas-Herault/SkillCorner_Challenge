"""
    Simple implementation of our print_lines function
"""
import argparse

import json


parser = argparse.ArgumentParser()

parser.add_argument('--log_file', '-l', type=str, required=True,
                    help='log file from whick to retrieve lines')

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

    return new_data


if __name__ == '__main__':

    ARGS = vars(parser.parse_args())

    # Open and read our log file
    with open(ARGS["log_file"], 'r') as file:
        lines = file.readlines()

    # Loop on our log lines
    for i, line in enumerate(lines):
        # Print the line number and processed NEW_DATA for each line
        print(f"Line n°{i} : ", get_new_data(i, line))
