import copy

mat=[
    'S%.....%.......',
    '.%...%.........',
    '...%.%...%%%%%%',
    '...%...%..%....',
    '...%..%.....%.E'
]
grid=[]
for row in mat:
    grid.append(list(row))
def heuristics(x1, x2, y1, y2):
    return abs(x2-x1)+abs(y2-y1)
def g():
    return 1
def aStar(start_x, start_y, target_x, target_y, grid):
    m,n=len(grid),len(grid[0])
    queue = []
    answer_routes = None

    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

    queue.append([start_x, start_y, [], 0])
    while len(queue) > 0:
        x, y, r, score = queue.pop(0)
        routes = copy.deepcopy(r)
        routes.append([x, y])

        if x == target_x and y == target_y:
            if answer_routes == None:
                answer_routes = routes
                break

        possible_moves = []
        for dx,dy in directions:
            next_x = x + dx
            next_y= y + dy
            if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n:
                continue

            if grid[next_x][next_y] == "E" or grid[next_x][next_y] == ".":
                grid[next_x][next_y] = '='
                possible_moves.append([next_x, next_y, score + heuristics(target_x,next_x,target_y,next_y) + g()])

        possible_moves.sort(key = lambda x: x[2])
        for move in possible_moves:
            queue.append([move[0], move[1], routes, score])

    return answer_routes

routes = aStar(0,0,4,14,grid)
for x in routes: print(x)
