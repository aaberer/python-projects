# subroutines if any, go here
import sys
import ast
# fill in your code


def longest_path(ribbon):

    if ribbon is None or len(ribbon) == 0:
        return None
    if len(ribbon[0]) == 0:
        return None

    rows, cols = len(ribbon), len(ribbon[0])
    norm = {}

    def depth_first(x, y):
        if (x, y) in norm:
            return norm[(x, y)]
        max_length = 0  # init
        best_previous = None
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # u,d,l,r

        for delta_x, delta_y in directions:
            new_x, new_y = x + delta_x, y + delta_y
            if 0 <= new_x < rows:
                if new_y < 0:
                    new_y = cols - 1
                elif new_y >= cols:
                    new_y = 0
                if ribbon[new_x][new_y] > ribbon[x][y]:
                    length, _ = depth_first(new_x, new_y)
                    if length > max_length:
                        max_length = length
                        best_previous = (new_x, new_y)
        norm[(x, y)] = (max_length + 1, best_previous)
        return norm[(x, y)]

    overall_max_length = 0
    starting_cell = None

    for row in range(rows):
        for col in range(cols):
            length, _ = depth_first(row, col)
            if length > overall_max_length:
                overall_max_length = length
                starting_cell = (row, col)

    if overall_max_length < 2:  # too small
        return ()

    path = []
    current_cell = starting_cell
    while current_cell is not None:  # build
        path.append(current_cell)
        current_cell = norm[current_cell][1]
    return tuple(path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ribbon should be a nested tuple.")
        sys.exit(1)

    ribbon_input = sys.argv[1]
    ribbon = ast.literal_eval(ribbon_input)
    result = longest_path(ribbon)
    print(result)
