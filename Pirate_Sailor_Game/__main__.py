"""
This file contains the function calls to execute the game.
This should be the only place you have code outside of functions, and the more
code within functions the better. You should call the functions defined in the
other modules (setup_game, player_actions, enemy_actions). You are free to
define additional functions and modules if needed, but these should be in
addition to existing functions, rather than replacements.

Note: to call functions from other modules, you need to
include the module name; e.g. setup_game.create_grid()
"""

import setup_game
import player_actions
import enemy_actions
# add any other imports you feel are relevant here

if __name__ == "__main__":
    # this is where the code should go that runs the game.
    # you can leave the following line in or take it out, up to you:
    print("PIRATES!")

    # Before you start, read the pro-forma(pdf) carefully; you should develop a
    # flow-chart or pseudocode to determine in which order you need to call the
    # functions from the other modules.
    while True:
        try:
            difficulty = int(input("Pick difficulty from 1-10: "))
            if 0 < difficulty < 11:
                break
        except ValueError:
            print("Didn't pick a number, please choose a number")

    size = 10
    grid = setup_game.create_grid(size)
    grid, player_position = setup_game.place_player(grid)
    grid, enemy_position = setup_game.place_enemy(grid)
    grid = setup_game.add_rocks(grid, difficulty)
    setup_game.print_grid(grid)

    while True:
        direction = player_actions.get_user_direction()
        new_player_position = player_actions.get_new_player_position(player_position, direction, grid)

        if grid[new_player_position[0]][new_player_position[1]] == "*":
            print("You have been killed by the rocks!")
            player_position = player_actions.kill_player(grid, player_position, new_player_position)
            setup_game.print_grid(grid)
            break
        elif grid[new_player_position[0]][new_player_position[1]] == "P":
            print("Pirates have killed you!")
            player_position = player_actions.kill_player(grid, player_position, new_player_position)
            break
        else:
            player_position = player_actions.move_player(grid, player_position, new_player_position)
            new_enemy_position = enemy_actions.get_new_enemy_position(enemy_position, player_position)

            if grid[new_enemy_position[0]][new_enemy_position[1]] == "*":
                print("You Won the Pirates sunk")
                enemy_position = enemy_actions.kill_enemy(grid, enemy_position, new_enemy_position)
                setup_game.print_grid(grid)
                break
            enemy_position = enemy_actions.move_enemy(grid, enemy_position, new_enemy_position)
            caught = enemy_actions.has_caught_player(enemy_position, player_position)
            if caught:
                print("You have been caught by the pirates!")
                setup_game.print_grid(grid)
                break
            else:
                enemy_position = enemy_actions.move_enemy(grid, enemy_position, new_enemy_position)
                setup_game.print_grid(grid)
