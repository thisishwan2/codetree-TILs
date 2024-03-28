def dice_change(dice, direction):
    if direction == 1:
        up = dice[0][1]
        floor = dice[1][1]
        down = dice[2][1]
        celing = dice[1][3]

        dice[0][1] = celing
        dice[1][1] = up
        dice[2][1] = floor
        dice[1][3] = down

    elif direction == 2:
        up = dice[0][1]
        floor = dice[1][1]
        down = dice[2][1]
        celing = dice[1][3]

        dice[0][1] = floor
        dice[1][1] = down
        dice[2][1] = celing
        dice[1][3] = up

    elif direction == 3:
        tmp = dice[1].pop()
        dice[1].insert(0, tmp)

    else:
        tmp = dice[1].pop(0)
        dice[1].append(tmp)


def bfs(board, nx, ny):
    q = deque()
    q.append([nx, ny])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[nx][ny] = 1
    num = board[nx][ny]
    score = num
    while q:
        x, y = q.popleft()
        for i in range(1, 5):
            nx = x + dir.get(i)[0]
            ny = y + dir.get(i)[1]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == num and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    score += num
    return score


from collections import deque

n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

x, y = 0, 0
direction = 4
dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

dice = [[0, 5, 0, 0], [4, 6, 3, 1], [0, 2, 0, 0]]
dice_floor_x = 1
dice_floor_y = 1

total = 0
for i in range(m):

    nx = x + dir.get(direction)[0]
    ny = y + dir.get(direction)[1]

    # 격자 안인지를 고려하기, 밖으로 나가려하면 반대로 튕겨나감
    if 0 > nx:
        direction = 2
        nx = x + dir.get(direction)[0]
    elif nx >= n:
        direction = 1
        nx = x + dir.get(direction)[0]

    if 0 > ny:
        direction = 4
        ny = y + dir.get(direction)[1]
    elif ny >= n:
        direction = 3
        ny = y + dir.get(direction)[1]

    # 주사위를 굴림
    dice_change(dice, direction)

    # 점수 입력
    total += bfs(board, nx, ny)

    # 바닥의 칸보다 큰 경우
    if dice[dice_floor_x][dice_floor_y] > board[nx][ny]:
        if direction == 1:
            direction = 4
        elif direction == 2:
            direction = 3
        elif direction == 3:
            direction = 1
        else:
            direction = 2
    elif dice[dice_floor_x][dice_floor_y] < board[nx][ny]:
        if direction == 1:
            direction = 3
        elif direction == 2:
            direction = 4
        elif direction == 3:
            direction = 2
        else:
            direction = 1
    else:
        pass
    x = nx
    y = ny
print(total)