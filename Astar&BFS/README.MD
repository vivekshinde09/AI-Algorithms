# AI Search Algorithms in Python

This project implements two important Artificial Intelligence search algorithms using Python:

* **A* Search**
* **Best First Search**

The program uses a weighted graph and heuristic values to find a path from a starting node to a goal node.

## Algorithms

### 1. A* Search

A* uses the formula:

```text
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = actual cost from the start node to the current node
* `h(n)` = estimated cost from the current node to the goal
* `f(n)` = total estimated cost

A* considers both the actual distance and heuristic distance while selecting the next node.

### 2. Best First Search

Best First Search uses:

```text
f(n) = h(n)
```

It selects the node with the smallest heuristic value.

Unlike A*, it does not consider the actual path cost `g(n)`, so it is not guaranteed to find the optimal path.

## Features

* Weighted graph representation
* Heuristic values for each node
* Priority queue using Python `heapq`
* Menu-driven program
* A* Search
* Best First Search
* Graph display
* User can select start and goal nodes

## Example Graph

```text
A → B (2), C (4)
B → D (3), E (5)
C → F (4)
D → G (2)
E → G (3)
F → G (2)
```

## Requirements

* Python 3.x
* No external libraries required

## How to Run

```bash
python main.py
```

Then select an option from the menu.

## Menu

```text
1. Display Graph
2. A* Search
3. Best First Search
4. Exit
```

## Concepts Used

* Artificial Intelligence
* Graph Search
* Heuristic Search
* A* Algorithm
* Best First Search
* Priority Queue
* `heapq`
* Python Classes and Objects
