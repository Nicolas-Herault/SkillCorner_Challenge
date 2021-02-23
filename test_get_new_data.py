"""
    Test file for testing the behaviour of our utils function
"""
import pytest

from print_lines.utils.get_new_data import get_new_data


DATA_FILE = "./print_lines/data/data.log"


@pytest.mark.parametrize(
    "line_number, expected_line",
    [
        # Expected case : 5 Multiple
        (5, "Multiple de 5"),
        # Expected case: Start with parenthesis and odd line number
        (1, '{"player": {"first_name": "Sergio", "last_name": "Ramos", "Age": 34}, "team": "Real Madrid"}'),
        # Expected case: Ending with a point
        (6, '{"player": {"first_name": "Luis", "last_name": "Suárez", "Age": 34}, "team": "Atlético Madrid"}.'),
        # Expected case: With a $
        (8, "Process_9000_suc$esfully_run"),
        # Expected case: No specific case, nothing to show
        (3, "Rien à afficher")
    ]
)
def test_get_new_data(line_number: int, expected_line: str) -> None:
    """
    Test the behavior of the print lines function

    Args:
        line_number: the line number ot get from the data file
        expected_line: the path to retrieve the expected output
    """
    with open(DATA_FILE, 'r') as file:
        lines = file.readlines()

    created_line = get_new_data(line_number, lines[line_number])
    print(created_line)
    assert expected_line == created_line, f"Expected line {expected_line} doesn't match \
                                           the created one {created_line}"
