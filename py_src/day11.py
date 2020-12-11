import itertools

from copy import deepcopy

test_input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

real_input = """<input data>"""

def parse_input(inpt):
    return [list(str) for str in inpt.split("\n")]

def get_adjacent_seats(x, y, layout, width, height):
    horizontal_span = xrange(-1, 2)
    vertical_span = xrange(-1, 2)
    deltas = list(itertools.product(horizontal_span, vertical_span))
    deltas.remove((0,0))
    return filter(lambda (x,y): (0 <= x < width) and (0 <= y < height),
                  [(x+delx, y+dely) for (delx, dely) in deltas])

def get_line_of_sight_seats(x, y, layout, width, height):
    def get_next_coordinate(x, y, x_step, y_step):
        while True:
            x = x + x_step
            y = y + y_step
            if x >= 0 and y >= 0 and x < width and y < height:
                if layout[x][y] != '.':
                    return x,y
            else:
                break
        return None
    
    horizontal_span = xrange(-1, 2)
    vertical_span = xrange(-1, 2)
    deltas = list(itertools.product(horizontal_span, vertical_span))
    deltas.remove((0,0))
    return filter(bool, [get_next_coordinate(x, y, delx, dely) for (delx, dely) in deltas])

def update_seat_layout(original_layout, next_seat_fn, threshold):
    height = len(original_layout)
    width = len(original_layout[0])
    new_layout = deepcopy(original_layout)
    for x,y in itertools.product(xrange(height), xrange(width)):
        occupied_seats = filter(
            lambda s: s == '#',
            [original_layout[adjx][adjy]
             for (adjx,adjy)
             in next_seat_fn(x, y, original_layout, height, width)])
        if original_layout[x][y] == 'L':
            if len(occupied_seats) == 0:
                new_layout[x][y] = '#'
        elif original_layout[x][y] == '#':
            if len(occupied_seats) >= threshold:
                new_layout[x][y] = 'L'
    num_occupied_seats = sum(
        1 for (x,y) in itertools.product(xrange(height), xrange(width)) if new_layout[x][y] == '#')
    return new_layout, num_occupied_seats

def print_layout(inpt):
    for row in inpt:
        print row
    
def runner(inpt, next_seat_fn, threshold=4):
    layout = parse_input(inpt)
    occupied_train = []
    while True:
        layout, num_occ = update_seat_layout(layout, next_seat_fn, threshold)
        occupied_train.append(num_occ)
        if len(occupied_train) > 5:
            if len(set(occupied_train[-5:])) == 1:
                return occupied_train[-1]

def part1(inpt):
    return runner(inpt, get_adjacent_seats)

def part2(inpt):
    return runner(inpt, get_line_of_sight_seats, threshold=5)
            
print part1(test_input)
print part2(real_input)
