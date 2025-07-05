

def convert_naive(s, numRows):
    """
    Naive solution to the zigzag conversion problem.
    Time complexity: O(n^2), where n is the length of the string.
    Space complexity: O(n^2), for storing the whole grid.
    :param s: Given string.
    :param numRows: The number of rows in the grid.
    :return: Converted string.
    """

    # Edge case: If only 1 row or string is too short, return as-is.
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize a grid (2D list) filled with empty strings
    # Rows = numRows, Columns = len(s) (worst case: full zigzag
    grid = [['' for _ in range(len(s))] for _ in range(numRows)]

    # Start at the top-left cell (row 0, column 0)
    row, col = 0, 0
    going_down = False  # Direction flag (False = moving up diagonally)

    for char in s:
        # Place the current character in the grid
        grid[row][col] = char

        # If at the top or bottom row, toggle direction
        if row == 0 or row == numRows - 1:
            going_down = not going_down

        # Move to the next position based on direction
        if going_down:
            row += 1    # Move down
        else:
            row -= 1    # Move up diagonally
            col += 1    # Move right

    # Read the grid row by row to construct the result
    result = []
    for r in range(numRows):        # For each row
        for c in range(len(s)):     # For each column
            if grid[r][c] != '':    # If a character exists here
                result.append(grid[r][c])

    return ''.join(result)  # Combine into final string


def main():
    # Test 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    expected1 = "PAHNAPLSIIGYIR"
    actual1 = convert_naive(s1, numRows1)
    print("Zigzag conversion of", s1, "->", actual1)
    assert actual1 == expected1

    # Test 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    expected2 = "PINALSIGYAHRPI"
    actual2 = convert_naive(s2, numRows2)
    print("Zigzag conversion of", s2, "->", actual2)
    assert actual2 == expected2

    # Test 3
    s3 = "A"
    numRows3 = 1
    expected3 = "A"
    actual3 = convert_naive(s3, numRows3)
    print("Zigzag conversion of", s3, "->", actual3)
    assert actual3 == expected3


if __name__ == '__main__':
    main()