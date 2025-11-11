"""
This file contains the functions that setup the game: creating a grid, placing
rocks and ships. You will need to finish these functions.

Do not change the function definitions, only the function bodies. You may add
additional functions if you wish.
"""

# enter any imports you feel are relevant here
import random


def create_grid(size):
    """
    This function creates a square grid where each side is as long as 'size'.
    The grid should be held in a two-dimensional list: that is, a
    list-of-lists. Each item in the outer list will be another list of the same
    size. The outer list holds the rows, the inner list holds each cell in a
    row. At the end of the function, this grid should be returned.

    NOTE: DO NOT USE LIST COMPREHENSION, USE A NESTED LOOP. List comprehension
    is useful, but for this assignment, please use a nested loop. For more
    information on nested loops, see 'Loops and lists 2' under week 3 course
    notes.

    :param size: the size of a side of the square grid
    :type size: int
    :return: a two-dimensional list representing the game grid
    :rtype: list
    """

    # put your code to create the grid here
    grid = []
    for _i in range(size):

        sea_tiles = "."
        sea_list = []
        for _ in range(size):
            sea_list.append(sea_tiles)

        grid.append(sea_list)
    return grid


def add_rocks(grid, difficulty):
    """
    This functions adds rocks(*) to the grid, then returns the updated grid.
    The number of rocks should be: 15 minus the difficulty level. For
    example, at difficulty 10 there would only be 5 rocks. The rocks should be
    randomly placed.
    :param grid: A 2D list that represents the game board
    :type grid: list
    :param difficulty: The game difficulty
    :type difficulty: int
    :return: The updated 2D game board
    :rtype: list
    """

    # put your code here:
    rocks_num = 15 - difficulty
    for _i in range(rocks_num):
        while True:

            rock_row = random.randint(0, len(grid)-1)
            rock_column = random.randint(0, len(grid)-1)

            if grid[rock_row][rock_column] == ".":
                grid[rock_row][rock_column] = "*"
                break
    # return the updated grid:
    return grid


def place_player(grid):
    """
    This function places the merchant ship ("M") at a random position in the
    grid, then returns the updated grid and the player position. Remember the
    ship should not be placed on the same square as a rock or the pirates.
    The player position should be returned as two integers in a tuple.
    :param grid: The 2D gameboard
    :type grid: list
    :return: The updated 2D gameboard, and player position.
    :rtype: list, tuple
    """

    # your code for placing the player here
    while True:

        merchant_place_1 = random.randint(0, len(grid) - 1)
        merchant_place_2 = random.randint(0, len(grid) - 1)

        if grid[merchant_place_1][merchant_place_2] == ".":
            player_position = (merchant_place_1, merchant_place_2)
            grid[merchant_place_1][merchant_place_2] = "M"
            break
    # returns two values, the updated grid and the player_position:
    return grid, player_position


def place_enemy(grid):
    """
    This function places the pirate ship ("P") at a random position in the
    grid, then returns the updated grid and the pirate position. Remember the
    ship should not be placed on the same square as a rock or the merchant
    ship. The pirate position should be returned as two integers in a tuple.

    Optional Note: does this function do anything similar to place_player and
    add_rocks? Is there any duplicate code that could be moved out to an
    additional function?

    :param grid: The 2D gameboard
    :type grid: list
    :return: The updated 2D gameboard, and enemy position.
    :rtype: list, tuple
    """

    # your code for placing the enemy here
    while True:

        pirate_place_1 = random.randint(0, len(grid) - 1)
        pirate_place_2 = random.randint(0, len(grid) - 1)

        if grid[pirate_place_1][pirate_place_2] == ".":
            enemy_position = (pirate_place_1, pirate_place_2)
            grid[pirate_place_1][pirate_place_2] = "P"
            break
    # returns two values, the updated grid and the enemy_position:

    return grid, enemy_position


def print_grid(grid):
    """
    Prints the grid. You'll need to call this function several times throughout
    the game. This function doesn't need to return anything, just print out to
    command line.

    NOTE: USE A NESTED LOOP, rather than the 'join' function.

    :param grid: The 2D gameboard
    :type grid: list
    :return: None
    """

    # your code for printing the grid here
    for row in grid:
        print(*row)
