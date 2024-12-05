def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check for "MAS" in a given direction
    def check_mas(x, y, dx, dy):
        try:
            return (
                grid[x][y] == 'M' and
                grid[x + dx][y + dy] == 'A' and
                grid[x + 2 * dx][y + 2 * dy] == 'S'
            )
        except IndexError:
            return False

    # Check all positions for "X-MAS"
    for i in range(rows):
        for j in range(cols):
            # Check for all four configurations of "X-MAS"
            if (
                check_mas(i, j, 1, -1) and check_mas(i, j, 1, 1) or  # Top-left to bottom-right X
                check_mas(i, j, -1, -1) and check_mas(i, j, -1, 1)   # Bottom-left to top-right X
            ):
                count += 1

    return count


# Input grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

# Convert grid into a list of lists
grid = [list(row) for row in grid]

# Count X-MAS occurrences
result = count_xmas(grid)
print(f"The number of X-MAS patterns is: {result}")
