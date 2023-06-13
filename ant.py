def calculate_sum(n):
    digit_sum = 0
    while n:
        digit_sum += n % 10
        n //= 10
    return digit_sum

def is_accessible(x, y):
    return calculate_sum(x) + calculate_sum(y) <= 25

def count_accessible_cells(start_x, start_y):
    queue = [(start_x, start_y)]
    visited = set()
    count = 0

    while queue:
        x, y = queue.pop(0)
        if (x, y) not in visited and is_accessible(x, y):
            visited.add((x, y))
            count += 1

            # Add neighboring cells to the queue
            queue.append((x, y + 1))  # Up
            queue.append((x, y - 1))  # Down
            queue.append((x - 1, y))  # Left
            queue.append((x + 1, y))  # Right

    return count

start_x = 1000
start_y = 1000
accessible_cells = count_accessible_cells(start_x, start_y)
print(f"The ant can visit {accessible_cells} cells.")
