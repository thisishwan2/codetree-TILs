from collections import deque

def move_runner():
    move_list = []
    for i in runner_dic.keys():
        x, y = runner_dic[i][0], runner_dic[i][1]

        if abs(seeker_x - x) + abs(seeker_y - y) <= 3:
            move_list.append(i)

    for i in move_list:
        x, y, d = runner_dic[i]

        for j in range(2):
            nx = x + dir_dic[d][0]
            ny = y + dir_dic[d][1]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    break
                else:
                    runner_dic[i] = [nx, ny, d]
                    break
            else:
                d = d + 2
                if d > 4:
                    d = d - 4


def move_forward(next):
    global seeker_x, seeker_y, total_score, turn
    flag = False
    for i in range(n):
        if flag:
            break

        for j in range(n):
            if seeker_move_arr[i][j]==next:
                seeker_x = i
                seeker_y = j
                d = seeker_forward[i][j]
                flag=True
                break


    direction = dir_dic[d]
    check_x = seeker_x
    check_y = seeker_y


    catch_runner_cnt=0
    remove_lst = []
    for i in range(3):
        nx = check_x + direction[0]*i
        ny = check_y + direction[1]*i

        # 나무가 아님
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
            for j in runner_dic.keys():
                r_x = runner_dic[j][0]
                r_y = runner_dic[j][1]

                if (nx,ny) == (r_x, r_y):
                    remove_lst.append(j)
                    catch_runner_cnt+=1
    for i in remove_lst:
        runner_dic.pop(i)
    total_score+=turn*catch_runner_cnt

def move_backward(next):
    global seeker_x, seeker_y, total_score, turn
    flag = False
    for i in range(n):
        if flag:
            break

        for j in range(n):
            if seeker_move_arr[i][j]==next:
                seeker_x = i
                seeker_y = j
                d = seeker_backward[i][j]
                flag = True
                break

    direction = dir_dic[d]
    check_x = seeker_x
    check_y = seeker_y


    catch_runner_cnt=0
    remove_lst=[]
    for i in range(3):
        nx = check_x + direction[0]*i
        ny = check_y + direction[1]*i

        # 나무가 아님
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
            for j in runner_dic.keys():
                r_x = runner_dic[j][0]
                r_y = runner_dic[j][1]

                if (nx,ny) == (r_x, r_y):
                    remove_lst.append(j)
                    catch_runner_cnt+=1

    for i in remove_lst:
        runner_dic.pop(i)
    total_score+=turn*catch_runner_cnt

def forward():
    x = n//2
    y = n//2
    q=deque()
    q.append([x,y]) # x,y,d


    while q:
        x,y= q.popleft()
        for i in range(1,5):
            nx = x + dir_dic[i][0]
            ny = y + dir_dic[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                if seeker_move_arr[nx][ny]==seeker_move_arr[x][y]+1:

                    for i in dir_dic.keys():
                        if dir_dic[i] == [nx-x, ny-y]:
                            seeker_forward[x][y]=i
                    q.append([nx,ny])


def backward():
    x = 0
    y = 0
    q = deque()
    q.append([x, y])  # x,y,d

    while q:
        x, y = q.popleft()
        for i in range(1, 5):
            nx = x + dir_dic[i][0]
            ny = y + dir_dic[i][1]

            if 0 <= nx < n and 0 <= ny < n:
                if seeker_move_arr[nx][ny] == seeker_move_arr[x][y] - 1:

                    for i in dir_dic.keys():
                        if dir_dic[i] == [nx - x, ny - y]:
                            seeker_backward[x][y] = i
                    q.append([nx, ny])





def find_seeker_move():
    global seeker_x, seeker_y, seeker_dir

    x = seeker_x
    y = seeker_y
    d = seeker_dir

    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1

    for i in range(2, n * n + 1):
        nx = x + dir_dic[d][0]
        ny = y + dir_dic[d][1]

        if visited[nx][ny] == 0:
            x = nx
            y = ny
            d = d + 1

            if d > 4:
                d = d - 4

            seeker_move_arr[nx][ny] = i
            visited[nx][ny]=1

        # 다음칸이 이미 간곳
        else:
            d = d - 1

            if d == 0:
                d = 4

            nx = x + dir_dic[d][0]
            ny = y + dir_dic[d][1]

            if visited[nx][ny] == 0:
                x = nx
                y = ny
                d = d + 1

                if d > 4:
                    d = d - 4

                seeker_move_arr[nx][ny] = i
                visited[nx][ny] = 1


n, m, h, k = map(int, input().split())

dir_dic = {1: [0, 1], 2: [1, 0], 3: [0, -1], 4: [-1, 0]}  # 우,하,좌,상

seeker_x = n // 2
seeker_y = n // 2
seeker_dir = 4

arr = [[0 for _ in range(n)] for _ in range(n)]
runner_dic = {}

# 도망자 x,y,d
for i in range(1, m + 1):
    x, y, d = map(int, input().split())
    runner_dic[i] = [x - 1, y - 1, d]
# 나무 x,y
for _ in range(h):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 2


# 술래 이동 순서 배열 생성
seeker_move_arr = [[0 for _ in range(n)] for _ in range(n)]
seeker_move_arr[seeker_x][seeker_y] = 1
find_seeker_move()

# 순방향 배열 생성
seeker_forward = [[0 for _ in range(n)] for _ in range(n)]
forward()
seeker_forward[0][0]=2
# 역방향 배열 생성
seeker_backward = [[0 for _ in range(n)] for _ in range(n)]
backward()
seeker_backward[n//2][n//2]=4

# 이동할 순서 리스트 만들기
seeker_move_seq = []
tmp1 = [i for i in range(2, n*n+1)]
tmp2 = [i for i in range(n*n-1,-1,-1)]
while 1:
    if len(seeker_move_seq)>=k:
        seeker_move_seq = seeker_move_seq[:k]
        break
    else:
        seeker_move_seq = seeker_move_seq + tmp1 + tmp2

seeker_move_seq.insert(0,1)

total_score=0
turn=1
for i in range(1, len(seeker_move_seq)):
    for j in range(2):

        # 도망자 턴
        if j == 0:
            # 술래와 거리가 3인지를 확인하고, 움직임
            move_runner()

        # 술래 턴
        elif j==1:

            # 순방향
            if seeker_move_seq[i-1] < seeker_move_seq[i]:
                move_forward(seeker_move_seq[i])
            # 역방향
            elif seeker_move_seq[i-1] > seeker_move_seq[i]:
                move_backward(seeker_move_seq[i])
    turn+=1

print(total_score)