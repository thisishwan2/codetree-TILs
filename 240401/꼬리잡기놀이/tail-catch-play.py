from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def turn(arr):
    new_arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nx = j
            ny = n - i - 1

            new_arr[nx][ny] = arr[i][j]

    return new_arr


def throw(idx):
    for i, val in enumerate(arr[idx]):
        if val != 4 and val != 0:

            visited = [[0 for _ in range(n)] for _ in range(n)]
            q = deque()
            q.append([idx, i, 1])
            visited[idx][i] = 1

            dic = {}

            while q:
                x, y, cnt = q.popleft()

                if arr[x][y] == 1:

                   dic[1]=[x,y,cnt]

                elif arr[x][y] == 3:
                    dic[3]=[x,y,cnt]

                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]

                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny] == 0 and arr[nx][ny] != 4 and arr[nx][ny] != 0:
                            q.append([nx, ny, cnt + 1])
                            visited[nx][ny] = 1

            x_1,y_1,cnt_1 = dic.get(1)
            x_3,y_3,cnt_3 = dic.get(3)

            arr[x_1][y_1]=3
            arr[x_3][y_3]=1

            return cnt*cnt

def move(arr):
    team = []
    new_arr = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                team.append(dfs(arr, i, j, team))

    for i in team:
        for idx, j in enumerate(i):
            people = j[0]
            x = j[1][0]
            y = j[1][1]

            if idx == len(i) - 1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if new_arr[nx][ny] != 4 and new_arr[nx][ny] != 0:
                            arr[nx][ny] = people
                            arr[x][y] = 4
            else:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 4:
                            arr[nx][ny] = people
                            arr[x][y] = 4
    return arr


def dfs(arr, x, y, team):
    tmp = []
    tmp.append([1, [x, y]])

    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and arr[nx][ny] != 4 and arr[nx][ny] != 0:
                    q.append([nx, ny])
                    tmp.append([arr[nx][ny], [nx, ny]])
                    visited[nx][ny] = 1

    return tmp


n, m, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 행 열수 만큼 round 공 던짐
score = 0
for i in range(k):

    # 각 팀은 머리사람을 따라서 한칸 이동한다.
    arr = move(arr)

    # 각 라운드 마다 정해진 선을 따라 공을 던진다.
    turn = i

    # 만약 n*4를 넘기면 다시 1로 초기화
    if turn // n == 4 and turn % n == 0:
        turn = 0

    if n - 1 >= turn >= 0:  # 좌측
        score += throw(turn)
    elif 2 * n - 1 >= turn > n:  # 하단
        arr = turn(arr)
        score += throw(turn % n)
        arr = turn(arr)
        arr = turn(arr)
        arr = turn(arr)

    elif 3 * n - 1 >= turn > 2 * n:  # 우측
        arr = turn(arr)
        arr = turn(arr)
        score += throw(turn % n)
        arr = turn(arr)
        arr = turn(arr)
    elif 4 * n - 1 >= turn > 3 * n:  # 상단
        arr = turn(arr)
        arr = turn(arr)
        arr = turn(arr)
        score += throw(turn % n)
        arr = turn(arr)


print(score)