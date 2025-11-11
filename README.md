# Pirate Sailor Game

A text-based grid game where you control a merchant ship (M) and must navigate through a dangerous sea filled with rocks (*) while being pursued by pirates (P). Your goal is to survive and avoid the pirates, or hope they crash into rocks!

## Prerequisites

- Python 3.x
- NumPy library

## Installation

1. Make sure you have Python 3 installed on your system.

2. Install the required dependency (NumPy):
   ```bash
   pip install numpy
   ```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd Pirate_Sailor_Game
   ```

2. Run the game using one of these methods:

   **Option 1: Run as a module (Recommended)**
   ```bash
   python -m Pirate_Sailor_Game
   ```

   **Option 2: Run directly**
   ```bash
   python Pirate_Sailor_Game/__main__.py
   ```

## How to Play

1. **Start the game**: When you run the program, you'll be prompted to choose a difficulty level from 1 to 10.
   - Higher difficulty (closer to 10) = fewer rocks = easier to navigate but pirates are still dangerous
   - Lower difficulty (closer to 1) = more rocks = harder to navigate but more chance pirates hit rocks

2. **Game Grid**: A 10x10 grid will be displayed showing:
   - `.` = Empty sea (safe water)
   - `M` = Your merchant ship (your position)
   - `P` = Pirate ship (enemy position)
   - `*` = Rocks (dangerous - avoid these!)
   - `X` = Your ship's wreck (if you die)
   - `W` = Pirate ship wreck (if pirates hit rocks)
   - `-` = Previous position marker

3. **Movement**: On each turn, you'll be prompted to choose a direction:
   - `N` = North (up)
   - `E` = East (right)
   - `S` = South (down)
   - `W` = West (left)

4. **Game Flow**:
   - You move first in your chosen direction
   - Then the pirates move automatically toward your position
   - The grid is updated and displayed after each turn

5. **Win/Lose Conditions**:
   - **You Lose** if:
     - You move into a rock (`*`) - "You have been killed by the rocks!"
     - You move into the pirates (`P`) - "Pirates have killed you!"
     - The pirates catch you (move adjacent to you) - "You have been caught by the pirates!"
   - **You Win** if:
     - The pirates move into a rock (`*`) - "You Won the Pirates sunk"

## Game Mechanics

- **Grid Size**: Fixed at 10x10
- **Movement**: Your ship cannot move off the edges of the grid (bounded movement)
- **Pirate AI**: Pirates automatically move toward your position each turn
- **Rock Placement**: Rocks are randomly placed based on difficulty (15 - difficulty level)
- **Ship Placement**: Both your ship and the pirate ship are randomly placed at the start, ensuring they don't overlap with rocks

## Tips

- Plan your moves carefully to avoid rocks
- Use rocks strategically - they can help you win if the pirates hit them
- Watch the pirate's movement pattern - they always move toward you
- Higher difficulty means fewer obstacles but requires more strategy

## Troubleshooting

- **Import Error for numpy**: Make sure you've installed numpy using `pip install numpy`
- **Invalid direction error**: Only use N, E, S, or W (case-insensitive)
- **Difficulty input error**: Enter a number between 1 and 10

Enjoy the game and good luck escaping the pirates!

