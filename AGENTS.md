# Project Agent Rules and Implementation Notes

This file documents working rules for this repository and should be treated as a reference in future interactions.

## Allowed file changes

- Modify only existing files unless explicitly asked otherwise.
- Current allowed files for this project task:
  - `pathfinding.py`
  - `README.md`
  - `AGENTS.md`

## Pathfinding implementation rules

- Keep function signatures exactly as written in `pathfinding.py`.
- DFS must be **iterative** using a Python `list` as a stack (no recursion).
- BFS must use `collections.deque` as a queue.
- Use:
  - `visited: set[tuple[int, int]]`
  - `parent: dict[tuple[int, int], tuple[int, int]]` mapping child -> parent
- Mark nodes visited when they are enqueued/pushed, not when popped.
- Keep changes minimal and ensure `main()` runs without crashing.

## Required functions in `pathfinding.py`

1. `parse_grid(text: str) -> tuple[list[list[str]], tuple[int,int], tuple[int,int]]`
   - Parse multiline map string into a 2D char grid.
   - Locate exactly one `S` and one `G`.
2. `neighbors(grid, node) -> list[tuple[int,int]]`
   - 4-direction movement only: up/down/left/right.
   - Must stay in bounds and avoid `#` walls.
3. `reconstruct_path(parent, start, goal) -> list[tuple[int,int]] | None`
   - Build path using parent pointers from goal back to start.
4. `bfs_path(grid, start, goal) -> tuple[list[tuple[int,int]] | None, set[tuple[int,int]]]`
   - Queue-based BFS.
5. `dfs_path(grid, start, goal) -> tuple[list[tuple[int,int]] | None, set[tuple[int,int]]]`
   - Stack-based iterative DFS.
6. `render(grid, path=None, visited=None) -> str`
   - Overlay path (`*`) and visited nodes (`·` or `+`) while preserving `S` and `G`.

## Program output requirements

When running:

```bash
python pathfinding.py
```

- Execute BFS and DFS on at least two built-in maps.
- For each algorithm/map combination print:
  - Path found or not
  - Path length (when found)
  - Number of visited nodes
  - Rendered grid
- Use clear separators for readability.
- Make BFS/DFS behavior differences obvious (BFS shortest path vs DFS path depending on traversal order).

## Troubleshooting guidance

- If output appears wrong, verify:
  - `S` and `G` are present exactly once in map parsing.
  - `visited` is updated on enqueue/push, not on pop.
  - DFS uses a list stack and no recursion.
  - BFS uses `deque.popleft()`.
  - Parent pointers are assigned before adding frontier nodes.
- If no path is found unexpectedly:
  - Confirm `neighbors` excludes walls and out-of-bounds coordinates.
  - Confirm `reconstruct_path` returns `None` when goal was never reached.
- If overlays look incorrect:
  - Preserve `S` and `G` characters during render.
  - Apply path overlay before visited overlay so path remains visible.
