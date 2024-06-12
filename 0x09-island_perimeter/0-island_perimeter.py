#!/usr/bin/python3

"""
Function to find perimeter of an island
"""

def island_perimeter(grid):
    """
    Input: List of Lists
    Returns: Perimeter of the island
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0]) if grid else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions (up, left, right, down)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1  # Up
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1  # Left
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1  # Right
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1  # Down

    return perimeter

# Test case
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
