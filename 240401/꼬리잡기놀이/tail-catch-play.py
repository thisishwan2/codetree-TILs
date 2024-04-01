from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def turn_90(arr):
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
                            if (arr[x][y]==3 and arr[nx][ny]==1):
                                continue
                            if (arr[x][y]==1 and arr[nx][ny]==3):
                                continue
                            q.append([nx, ny, cnt + 1])
                            visited[nx][ny] = 1

            x_1,y_1,cnt_1 = dic.get(1)
            x_3,y_3,cnt_3 = dic.get(3)

            arr[x_1][y_1]=3
            arr[x_3][y_3]=1

            return cnt_1*cnt_1

    return 0


# 진짜 DFS 로 수정해야함
def move(arr):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]==3 and visited[i][j]==0:
                arr = bfs_move(i,j,visited, arr)

    # print(*arr, sep='\n')
    # print("===========")
    return arr


def bfs_move(x,y,visited, arr):
    new_arr = copy.deepcopy(arr)

    q=deque()
    q.append((x,y))


    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny<n and visited[nx][ny]==0:
                if arr[x][y] == 3 and arr[nx][ny] == 2: # 현재 꼬리고 다음은 2인경우
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    new_arr[nx][ny]=arr[x][y]
                    new_arr[x][y]=4
                    break
                elif arr[x][y]==2 and arr[nx][ny]==2:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    new_arr[nx][ny] = arr[x][y]
                    break
                elif arr[x][y]==2 and arr[nx][ny]==1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    new_arr[nx][ny] = arr[x][y]
                    break

                elif (arr[x][y]==1 and arr[nx][ny]==4) or (arr[x][y]==1 and arr[nx][ny]==3):
                    visited[nx][ny] = 1
                    new_arr[nx][ny] = arr[x][y]
                    break
    return new_arr


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
        arr = turn_90(arr)
        score += throw(turn % n)
        arr = turn_90(arr)
        arr = turn_90(arr)
        arr = turn_90(arr)

    elif 3 * n - 1 >= turn > 2 * n:  # 우측
        arr = turn_90(arr)
        arr = turn_90(arr)
        score += throw(turn % n)
        arr = turn_90(arr)
        arr = turn_90(arr)
    elif 4 * n - 1 >= turn > 3 * n:  # 상단
        arr = turn_90(arr)
        arr = turn_90(arr)
        arr = turn_90(arr)
        score += throw(turn % n)
        arr = turn_90(arr)


print(score)