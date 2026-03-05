from collections import deque

EXAMPLE_MAP_1 = """
###########
#S..#.....#
#.#.#.###.#
#.#...#...#
#.#####.#G#
#.........#
###########
"""

EXAMPLE_MAP_2 = """
###########
#S#.......#
#.#.#####.#
#.#.....#.#
#.#####.#.#
#.....#..G#
###########
"""


def parse_grid(text: str) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    grid = [list(line) for line in lines]

    start = None
    goal = None

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                if start is not None:
                    raise ValueError("Grid must contain exactly one start 'S'.")
                start = (r, c)
            elif ch == "G":
                if goal is not None:
                    raise ValueError("Grid must contain exactly one goal 'G'.")
                goal = (r, c)

    if start is None or goal is None:
        raise ValueError("Grid must contain exactly one 'S' and one 'G'.")

    return grid, start, goal


def neighbors(grid, node) -> list[tuple[int, int]]:
    r, c = node
    height = len(grid)
    width = len(grid[0]) if height else 0

    result: list[tuple[int, int]] = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] != "#":
            result.append((nr, nc))

    return result


def reconstruct_path(parent, start, goal) -> list[tuple[int, int]] | None:
    if start == goal:
        return [start]
    if goal not in parent:
        return None

    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur]
        path.append(cur)

    path.reverse()
    return path


def bfs_path(grid, start, goal) -> tuple[list[tuple[int, int]] | None, set[tuple[int, int]]]:
    queue = deque([start])
    visited: set[tuple[int, int]] = {start}
    parent: dict[tuple[int, int], tuple[int, int]] = {}

    while queue:
        cur = queue.popleft()
        if cur == goal:
            break

        for nxt in neighbors(grid, cur):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = cur
                queue.append(nxt)

    return reconstruct_path(parent, start, goal), visited


def dfs_path(grid, start, goal) -> tuple[list[tuple[int, int]] | None, set[tuple[int, int]]]:
    stack = [start]
    visited: set[tuple[int, int]] = {start}
    parent: dict[tuple[int, int], tuple[int, int]] = {}

    while stack:
        cur = stack.pop()
        if cur == goal:
            break

        for nxt in neighbors(grid, cur):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = cur
                stack.append(nxt)

    return reconstruct_path(parent, start, goal), visited


def render(grid, path=None, visited=None) -> str:
    path_set = set(path) if path else set()
    visited_set = set(visited) if visited else set()

    out = []
    for r, row in enumerate(grid):
        line_chars = []
        for c, ch in enumerate(row):
            pos = (r, c)
            if ch in {"S", "G"}:
                line_chars.append(ch)
            elif pos in path_set:
                line_chars.append("*")
            elif pos in visited_set and ch != "#":
                line_chars.append("·")
            else:
                line_chars.append(ch)
        out.append("".join(line_chars))

    return "\n".join(out)


def run_map(map_name: str, map_text: str) -> None:
    grid, start, goal = parse_grid(map_text)

    print("=" * 50)
    print(f"Map: {map_name}")
    print("=" * 50)

    for algo_name, algo in [("BFS", bfs_path), ("DFS", dfs_path)]:
        path, visited = algo(grid, start, goal)
        print(f"\n--- {algo_name} ---")
        if path is None:
            print("Path found: No")
            print("Path length: N/A")
        else:
            print("Path found: Yes")
            print(f"Path length: {len(path)}")
        print(f"Visited nodes: {len(visited)}")
        print(render(grid, path=path, visited=visited))



def main() -> None:
    run_map("EXAMPLE_MAP_1", EXAMPLE_MAP_1)
    print()
    run_map("EXAMPLE_MAP_2", EXAMPLE_MAP_2)


if __name__ == "__main__":
    main()
