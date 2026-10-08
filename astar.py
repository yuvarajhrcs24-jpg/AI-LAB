import heapq

# Calculate misplaced tiles heuristic
def heuristic(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = \
                new_state[new_pos], new_state[zero_pos]

            neighbors.append(tuple(new_state))

    return neighbors


# A* algorithm
def a_star(start, goal):

    # Priority queue:
    # (f, g, state, path)
    pq = []

    g = 0
    h = heuristic(start, goal)
    f = g + h

    heapq.heappush(pq, (f, g, start, [start]))

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        # Goal reached
        if state == goal:
            return path

        # Generate next states
        for next_state in get_neighbors(state):

            if next_state not in visited:

                new_g = g + 1
                new_h = heuristic(next_state, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, next_state, path + [next_state])
                )

    return None


# Print puzzle
def print_puzzle(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


# ---------------- MAIN PROGRAM ----------------

print("Enter initial state (use 0 for blank):")
start = tuple(map(int, input().split()))

print("Enter goal state (use 0 for blank):")
goal = tuple(map(int, input().split()))

# Check input
if len(start) != 9 or len(goal) != 9:
    print("Error: Enter exactly 9 numbers.")
else:

    solution = a_star(start, goal)

    if solution is None:
        print("\nNo solution found.")

    else:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)
        print("\nSteps:\n")

        for i, state in enumerate(solution):
            print("Step", i)
            print_puzzle(state)