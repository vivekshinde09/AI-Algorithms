# 8-Puzzle Solver Using A* Algorithm

This project implements the 8-Puzzle problem using the A* search algorithm in Python.

## Features

* User can enter a custom puzzle
* Displays the current puzzle
* Solves the puzzle using A* algorithm
* Uses Misplaced Tiles heuristic
* Uses `heapq` as a priority queue
* Tracks visited states
* Reconstructs and displays the solution path
* Displays the total number of moves

## Goal State

```text
1 2 3
4 5 6
7 8 0
```

Use `0` to represent the blank space.

## Algorithm

A* uses the following formula:

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` is the cost from the initial state
* `h(n)` is the heuristic cost
* `f(n)` is the total cost

The project uses the Misplaced Tiles heuristic.

## Menu

```text
1. For Giving puzzle info
2. Display
3. For 8 puzzle solution
4. For Exit
```

## Requirements

* Python 3.10 or later
* No external libraries required

The project uses Python's built-in `heapq` module.

## Run

```bash
python eight_puzzle.py
```

## Project Structure

```text
8-puzzle-a-star/
    eight_puzzle.py
    README.md
```

## Future Improvements

* Manhattan Distance heuristic
* Solvability checking
* GUI using Tkinter
* Comparison with BFS and DFS

## Author

Vivek Shinde
