import copy
from collections import deque

def turn_90(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            new_arr[j][3 - i - 1] = arr[i][j]

    return new_arr

def turn_180(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            new_arr[3 - i - 1][3 - j - 1] = arr[i][j]

    return new_arr

def turn_270(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            new_arr[3 - j - 1][i] = arr[i][j]

    return new_arr

# 여기가 뮨제
def count_first_value(arr):
    cnt = 0
    visited = [[0 for _ in range(5)] for _ in range(5)]  # 아직 방문하지 않은 경우 0, 방문했는데 3개이상 연결된 놈은 1, 방문햇는데 아무것도 아닌 놈 -1
    bfs_visited = [[0 for _ in range(5)] for _ in range(5)] # bfs 돌때 방문처리 하기 위한

    # 상우하좌
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for i in range(5):
        for j in range(5):
            connect_three_over = []  # 3개 이상 연결됨을 확인하기 위한 리스트
            if bfs_visited[i][j] == 0:
                q = deque()
                q.append([i, j, arr[i][j]])
                connect_three_over.append([i, j])
                bfs_visited[i][j]=1
                while q:
                    x, y, num = q.popleft()

                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]

                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if bfs_visited[nx][ny] == 0 and arr[nx][ny] == num:
                                q.append([nx, ny, num])
                                connect_three_over.append([nx, ny])
                                bfs_visited[nx][ny]=1

            if len(connect_three_over) >= 3:
                for a, b in connect_three_over:
                    visited[a][b] = 1
            else:
                for a, b in connect_three_over:
                    visited[a][b] = -1

    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                cnt += 1

    return cnt


# 회전 가능한 경우를 찾는다.
def find_3_by_3():
    first_value = 0  # 1차 유물의 획득 가치
    turn = 0  # 회전시킬 각도
    x = 0
    y = 0
    turn_values = [90, 180, 270]

    # i,j는 중심좌표
    for i in range(1, 4):
        for j in range(1, 4):
            for turn_ in turn_values:
                new_board = copy.deepcopy(board)
                new_3_by_3_board = [[0 for _ in range(3)] for _ in range(3)]

                for a in range(3):
                    for b in range(3):
                        new_3_by_3_board[a][b] = board[i - 1 + a][j - 1 + b]

                # turn
                if turn_ == 90:
                    new_3_by_3_board = turn_90(new_3_by_3_board)
                elif turn_ == 180:
                    new_3_by_3_board = turn_180(new_3_by_3_board)
                elif turn_ == 270:
                    new_3_by_3_board = turn_270(new_3_by_3_board)

                # 회전한 부분을 원래 배열에 넣는다.
                for a in range(3):
                    for b in range(3):
                        new_board[i - 1 + a][j - 1 + b] = new_3_by_3_board[a][b]

                # 회전한 배열의 1차 유물 가치 확인
                cnt = count_first_value(new_board)

                if first_value < cnt:
                    first_value = cnt
                    turn = turn_
                    x = i
                    y = j
                elif first_value == cnt and cnt != 0:
                    # 기존의 회전 각도와 비교해서 현재 회전 각도가 더 작다면
                    if turn > turn_:
                        turn = turn_
                        x = i
                        y = j
                    elif turn == turn_:
                        # 열과 행이 가장 작은것을 선택
                        if x > i:
                            x = i
                            y = j
                        elif x==i:
                            if y > j:
                                y = j

    return first_value, turn, x, y


# 3개 이상 연결된 유물을 지우고, 유물의 가치를 반환한다.
def remove_value():
    cnt = 0
    visited = [[0 for _ in range(5)] for _ in range(5)]  # 아직 방문하지 않은 경우 0, 방문했는데 3개이상 연결된 놈은 1, 방문햇는데 아무것도 아닌 놈 -1
    bfs_visited = [[0 for _ in range(5)] for _ in range(5)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(5):
        for j in range(5):
            connect_three_over = []  # 3개 이상 연결됨을 확인하기 위한 리스트
            if bfs_visited[i][j] == 0:
                q = deque()
                q.append([i, j, board[i][j]])
                connect_three_over.append([i, j])
                bfs_visited[i][j]=1
                while q:
                    x, y, num = q.popleft()

                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]

                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if bfs_visited[nx][ny] == 0 and board[nx][ny] == num:
                                q.append([nx, ny, num])
                                connect_three_over.append([nx, ny])
                                bfs_visited[nx][ny]=1

            if len(connect_three_over) >= 3:
                for a, b in connect_three_over:
                    visited[a][b] = 1
            else:
                for a, b in connect_three_over:
                    visited[a][b] = -1

    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                cnt += 1
                board[i][j] = 0

    return cnt


K, M = map(int, input().split())  # 반복횟수, 벽면에 적힌 유물 조각 수

board = []
for i in range(5):
    board.append(list(map(int, input().split())))

numbers = list(map(int, input().split()))

# print(*board, sep='\n')
# print(numbers)

for _ in range(K):
    value = 0

    # 1. 탐사진행
    # 우선 회전 가능한 경우를 찾는다.
    val, turn_degree, x, y = find_3_by_3()  # 1차 획득 가능 수, 회전 각도, 중심 좌표 x,y

    if val == 0:
        break

    # 해당 중심좌표를 기준으로 3*3 만큼 회전한다.
    new_3_by_3_board = [[0 for _ in range(3)] for _ in range(3)]

    for a in range(3):
        for b in range(3):
            new_3_by_3_board[a][b] = board[x - 1 + a][y - 1 + b]

    # turn
    if turn_degree == 90:
        new_3_by_3_board = turn_90(new_3_by_3_board)
    elif turn_degree == 180:
        new_3_by_3_board = turn_180(new_3_by_3_board)
    elif turn_degree == 270:
        new_3_by_3_board = turn_270(new_3_by_3_board)

    # 회전한 부분을 원래 배열에 넣는다.
    for a in range(3):
        for b in range(3):
            board[x - 1 + a][y - 1 + b] = new_3_by_3_board[a][b]

    # 2. 유물 획득 및 연쇄 획득
    while True:
        cnt = remove_value()
        if cnt == 0:
            break

        value += cnt

        # 벽면의 숫자를 board의 0으로 되어있는 부분에 채워넣는다.
        index = 0

        for j in range(5):
            for i in range(4, -1, -1):
                if board[i][j] == 0:
                    board[i][j] = numbers[index]
                    index += 1

        numbers = numbers[index:]

    print(value, end=" ")