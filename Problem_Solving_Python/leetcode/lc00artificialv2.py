import copy

# pacman_x, pacman_y = list(map(int, input().split()))
# food_x, food_y = list(map(int, input().split()))
# n, m = list(map(int, input().split()))
mat=[ 'P--%%%--------------------%%%%%%%%%%%',
    '%---------------------------%-----%-%',
    '%-%%%%%%%-%-----------------%%%%%-%-%',
    '%-------%-------%-%-----%-----%-%---%',
    '%%%%%-%%%%%-%%%-%-%-%-%%%-----------.'
]
grid=[]
for row in mat:
    grid.append(list(row))
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
        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if next_x < 0 or next_x >= m or next_y < 0 and next_y >= n:
                continue

            if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
                grid[next_x][next_y] = '='
                possible_moves.append([next_x, next_y, score + abs(target_x - next_x) + abs(target_y - next_y)])

        possible_moves.sort(key = lambda x: x[2])
        for move in possible_moves:
            queue.append([move[0], move[1], routes, score])

    print(str(len(answer_routes) - 1))
    for point in answer_routes:
        print(str(point[0]) + " " + str(point[1]))
aStar(0,0,4,36,grid)
