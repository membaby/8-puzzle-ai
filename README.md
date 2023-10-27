# 8-Puzzle Solver with Informed and Uninformed Search Algorithms

## Table of Contents
- [Overview](#overview)
- [Algorithms](#algorithms)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributors](#Contributors)

## Overview
This project implements an agent to solve the 8-puzzle game using both informed (A*) and uninformed (BFS, DFS) search algorithms. The 8-puzzle game consists of a board with 8 distinct movable tiles and an empty space represented by the number 0. The goal is to transition the initial state to the configuration with all tiles arranged in ascending order (0,1,2,3,4,5,6,7,8).


## Algorithms
The project implements the following search algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search
  - Manhattan Heuristic
  - Euclinean Heuristic

## Getting Started
To get started with this project, follow the instructions below.

### Prerequisites
- Python
- PyQt6 (for the GUI)

### Installation
1. Clone the repository to your local machine.
     ```
     git clone https://github.com/your-username/8-puzzle-solver.git
2.  Install the required dependencies, including PyQt6.
     ```
     pip install PyQt6
### Usage        
1. Run the program with Python.
    ```
    python app.py  
2. Use the GUI to input the initial state of the 8-puzzle.
3. Select the search algorithm (BFS, DFS, A*).
4. Click the "Solve" button to find the solution.
5. The program will display the statistics and solution path.

## Contributors
- [Ehab Yasser](https://github.com/EhabYasser25)
- [Mahmoud Embaby](https://github.com/membaby)
- [Rowaina Abdelnaser](https://github.com/rowaina2025)
- [Sama Zayed](https://github.com/samatarekzayed)

