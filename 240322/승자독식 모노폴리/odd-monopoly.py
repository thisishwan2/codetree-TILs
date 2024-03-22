from collections import deque


def move(arr, x, y, k, player_num, direction):
    arr[x][y] = [player_num, k + 1]
    q.append([player_num, direction, x, y])


def conflict(arr, x, y, k, player_num, direction, black_list):
    if arr[x][y][0] > player_num:  # 새로 온 플레이어 번호가 더 낮은 경우 기존 플레이어를 추방
        black_list.append(arr[x][y][0])
        arr[x][y] = [player_num, k + 1]
        q.append([player_num, direction, x, y])
    else:
        black_list.append(player_num)


def minus(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                player_num = arr[i][j][0]
                registartion = arr[i][j][1]
                arr[i][j] = [player_num, registartion - 1]


dir = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}

n, m, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 초기 player 방향
init_direction = list(map(int, input().split()))

player_direction = {}
for i in range(1, m + 1):  # 플레이어마다
    tmp = {}
    for j in range(1, 5):  # 4가지 방향에 대한 우선순위 존재
        tmp[j] = list(map(int, input().split()))
    player_direction[i] = tmp

# 초기 플레이어에 대한 정보를 담을 큐 생성 및 배열에 필요한 정보를 추가
q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            player_num = arr[i][j]
            direction = init_direction[player_num - 1]

            q.append([player_num, direction, i, j])
            arr[i][j] = [player_num, k]

ans = 0
black_list = []
while ans < 1000:

    if len(black_list) == m - 1 and 1 not in black_list:
        print(ans)
        exit()

    for i in range(len(q)):
        player_num, direction, x, y = q.popleft()

        if player_num in black_list:
            continue

        player_direction_dic = player_direction.get(player_num)
        player_direction_list = player_direction_dic.get(direction)

        not_empty_arr = 0
        for j in player_direction_list:
            dx, dy = dir.get(j)
            nx = x + dx
            ny = y + dy
            not_empty_arr += 1

            if 0 <= nx < n and 0 <= ny < n:
                # 인접한 빈칸 존재하는 경우
                if arr[nx][ny] == 0:
                    # 이동
                    move(arr, nx, ny, k, player_num, j)
                    break
                # 인접한 빈칸은 아닌경우, 다른 유저가 이번 턴에 먼저 온경우
                elif arr[nx][ny][1] == k+1:
                    conflict(arr, nx, ny, k, player_num, j, black_list)
                    break

        # 그 외의 경우 본인의 이전 칸으로 돌아간다.
        if not_empty_arr == 4:
            for i in range(1, 5):
                dx, dy = dir.get(i)
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny][0] == player_num and arr[nx][ny][1] == k - 1:
                        move(arr, nx, ny, k, player_num, i)
                        continue
    minus(arr)
    ans += 1

print(-1)