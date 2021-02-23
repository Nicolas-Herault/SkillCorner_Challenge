"""
    Simple implementation of our print_lines function
"""
import argparse

from print_lines.utils.get_new_data import get_new_data

parser = argparse.ArgumentParser()

parser.add_argument('--log_file', '-l', type=str, required=True,
                    help='log file from whick to retrieve lines')


if __name__ == '__main__':

    ARGS = vars(parser.parse_args())

    # Open and read our log file
    with open(ARGS["log_file"], 'r') as file:
        lines = file.readlines()

    # Loop on our log lines
    for i, line in enumerate(lines):
        # Print the line number and processed NEW_DATA for each line
        print(f"Line n°{i} : ", get_new_data(i, line))
