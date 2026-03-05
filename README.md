# DFS/BFS Grid Pathfinding (Python)

This project demonstrates **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** on a 2D grid.

- **BFS** explores level by level and finds the shortest path in an unweighted grid.
- **DFS** explores deeply along one route before backtracking, so it may return a longer path depending on neighbor order.

## Run

```bash
python pathfinding.py
```

The program runs both BFS and DFS on built-in example maps and prints:

- Whether a path was found
- Path length (if found)
- Number of visited nodes
- Rendered grid with overlays

## Grid legend

- `#` wall
- `.` walkable floor
- `S` start
- `G` goal
- `*` final path
- `·` visited node (not on final path)

## Example output format

```text
==================================================
Map: EXAMPLE_MAP_1
==================================================

--- BFS ---
Path found: Yes
Path length: 13
Visited nodes: 24
###########
#S**#.....#
#.#*#.###.#
#.#***#...#
#.#####*#G#
#......***#
###########

--- DFS ---
Path found: Yes
Path length: 17
Visited nodes: 21
...
```
