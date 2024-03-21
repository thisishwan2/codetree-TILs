from collections import deque

def minus(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                player_num, registration = arr[i][j]
                if registration - 1 == 0:
                    arr[i][j] = 0
                else:
                    arr[i][j] = [player_num, registration - 1]

def move_and_conflict(arr, q, direction_dic, k):
    next_positions = {}  # 다음 턴에 각 플레이어가 이동할 위치를 저장
    for _ in range(len(q)):
        x, y, player_num, direction = q.popleft()
        priorities = direction_dic[player_num][direction]
        moved = False
        for p in priorities:
            nx, ny = x + dx[p], y + dy[p]
            if 0 <= nx < n and 0 <= ny < n and (arr[nx][ny] == 0 or arr[nx][ny][1] == k):
                next_positions[(nx, ny)] = min(next_positions.get((nx, ny), player_num), player_num)
                moved = True
                break
        if not moved:  # If no move was made, stay in place
            next_positions[(x, y)] = player_num

    # Clear the board and update with new positions
    for i in range(n):
        for j in range(n):
            arr[i][j] = 0
    for position, player_num in next_positions.items():
        x, y = position
        arr[x][y] = [player_num, k]
        q.append([x, y, player_num, direction_dic[player_num][direction][0]])  # Update direction based on priority

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
init_direction = list(map(int, input().split()))

q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            player_num = arr[i][j]
            arr[i][j] = [player_num, k]
            q.append([i, j, player_num, init_direction[player_num - 1]])

direction_dic = {}
for i in range(1, m + 1):
    direction_dic[i] = {}
    for j in range(1, 5):
        direction_dic[i][j] = list(map(int, input().split()))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

turns = 0
while turns < 1000:
    turns += 1
    minus(arr)  # Decrease the contract turn count at the start of each turn
    move_and_conflict(arr, q, direction_dic, k)
    if len(q) == 1 and q[0][2] == 1:  # If only player 1 remains
        print(turns)
        break
else:
    print(-1)