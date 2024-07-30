# def dust_left(arr, x, y):
#     cal = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01,0], [0, 0, 0.02, 0, 0]]

#     now = arr[x][y]  # 본 배열의 먼지 값
#     a_x, a_y = 2, 1  # a의 위치 인덱스
#     cal_res = [[0 for _ in range(5)] for _ in range(5)]

#     total = 0  # 계산된 먼지 총합

#     for i in range(5):
#         for j in range(5):
#             if cal[i][j] != 0:
#                 calcu = int(cal[i][j] * now)
#                 cal_res[i][j] = calcu
#                 total += calcu

#     cal_res[a_x][a_y] = arr[x][y] - total

#     # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
#     x_plus = x - 2
#     y_plus = y - 2

#     # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
#     for i in range(5):
#         for j in range(5):
#             if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
#                 arr[i + x_plus][j + y_plus] += cal_res[i][j]

#     arr[x][y] = 0
#     # print(arr)
#     return arr

# def dust_right(arr, x, y):
#     cal = [[0, 0, 0.02, 0, 0], [0, 0.01, 0.07, 0.1, 0], [0, 0, 0, 0, 0.05], [0, 0.01, 0.07, 0.1,0], [0, 0, 0.02, 0, 0]]

#     now = arr[x][y]  # 본 배열의 먼지 값
#     a_x, a_y = 2, 3  # a의 위치 인덱스
#     cal_res = [[0 for _ in range(5)] for _ in range(5)]

#     total = 0  # 계산된 먼지 총합

#     for i in range(5):
#         for j in range(5):
#             if cal[i][j] != 0:
#                 calcu = int(cal[i][j] * now)
#                 cal_res[i][j] = calcu
#                 total += calcu

#     cal_res[a_x][a_y] = arr[x][y] - total

#     # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
#     x_plus = x - 2
#     y_plus = y - 2

#     # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
#     for i in range(5):
#         for j in range(5):
#             if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
#                 arr[i + x_plus][j + y_plus] += cal_res[i][j]

#     arr[x][y] = 0
#     # print(arr)
#     return arr

# def dust_up(arr, x, y):
#     cal = [[0,0,0.05,0,0], [0,0.1,0,0.1,0], [0.02,0.07,0,0.07,0.02], [0,0.01,0,0.01,0], [0,0,0,0,0]]

#     now = arr[x][y]  # 본 배열의 먼지 값
#     a_x, a_y = 1, 2  # a의 위치 인덱스
#     cal_res = [[0 for _ in range(5)] for _ in range(5)]

#     total = 0  # 계산된 먼지 총합

#     for i in range(5):
#         for j in range(5):
#             if cal[i][j] != 0:
#                 calcu = int(cal[i][j] * now)
#                 cal_res[i][j] = calcu
#                 total += calcu

#     cal_res[a_x][a_y] = arr[x][y] - total

#     # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
#     x_plus = x - 2
#     y_plus = y - 2

#     # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
#     for i in range(5):
#         for j in range(5):
#             if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
#                 arr[i + x_plus][j + y_plus] += cal_res[i][j]

#     arr[x][y] = 0
#     # print(arr)
#     return arr

# def dust_down(arr, x, y):
#     cal = [[0,0,0,0,0], [0,0.01,0,0.01,0], [0.02,0.07,0,0.07,0.02], [0,0.1,0,0.1,0], [0,0,0.05,0,0]]

#     now = arr[x][y]  # 본 배열의 먼지 값
#     a_x, a_y = 3, 2  # a의 위치 인덱스
#     cal_res = [[0 for _ in range(5)] for _ in range(5)]

#     total = 0  # 계산된 먼지 총합

#     for i in range(5):
#         for j in range(5):
#             if cal[i][j] != 0:
#                 calcu = int(cal[i][j] * now)
#                 cal_res[i][j] = calcu
#                 total += calcu

#     cal_res[a_x][a_y] = arr[x][y] - total

#     # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
#     x_plus = x - 2
#     y_plus = y - 2

#     # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
#     for i in range(5):
#         for j in range(5):
#             if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
#                 arr[i + x_plus][j + y_plus] += cal_res[i][j]

#     arr[x][y] = 0
#     # print(arr)
#     return arr


# def check_dir(dir, direction, x, y, visited):
#     new_dir = 0
#     if direction == 1:
#         new_dir = 3
#     elif direction == 2:
#         new_dir = 4
#     elif direction == 3:
#         new_dir = 2
#     else:
#         new_dir = 1

#     nx = x + dir.get(new_dir)[0]
#     ny = y + dir.get(new_dir)[1]

#     if visited[nx][ny] == 0:
#         return new_dir
#     else:
#         return direction


# dir = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}

# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))

# # 전체 먼지수 구하기
# total_dust = 0
# for i in range(n):
#     for j in range(n):
#         total_dust += arr[i][j]

# # 전체 탐색 횟수
# time = n * 2 - 1

# x = n // 2
# y = n // 2
# direction = 3
# visited = [[0 for _ in range(n)] for _ in range(n)]
# visited[x][y] = 1

# for i in range(n * n - 1):
#     direc = dir.get(direction)
#     nx = x + direc[0]
#     ny = y + direc[1]
#     visited[nx][ny] = 1

#     x=nx
#     y=ny

#     # 먼지 계산
#     if direction == 1: # 윗 방향
#         dust_up(arr,x,y)
#     elif direction == 2: # 아래
#         dust_down(arr,x,y)
#     elif direction == 3: #좌측
#         dust_left(arr,x,y)
#     else: # 우측
#         dust_right(arr,x,y)



#     # 방향을 왼쪽을 90도 회전시킨 방문 배열에 이미 방문한 적이 있으면, 그냥 지금 방향 그대로 진행
#     direction = check_dir(dir, direction, x, y, visited)

# # for문 다돌고 나서, 배열 전체를 한번 다시 탐색을 해서 남아있는 먼지를 구하고, 전체 먼지에서 빼면 격자 밖으로 나간 먼지를 구할 수 잇음
# dust = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] != 0:
#             dust += arr[i][j]

# print(total_dust - dust)

# 청소는 즐거워
from collections import deque


def get_direction(now_x, now_y, n_x, n_y):
    # 좌측으로 이동하는 경우
    if now_x == n_x and now_y > n_y:
        return 2
    # 우측으로 이동하는 경우
    elif now_x == n_x and now_y < n_y:
        return 0
    # 아래로 이동하는 경우
    elif now_x < n_x and now_y == n_y:
        return 1
    # 위로 이동하는 경우
    elif now_x > n_x and now_y == n_y:
        return 3

# 오른쪽
def cal_dir_0(x,y):
    dust_cnt = 0

    # a%
    if 0 <= x < n and 0 <= y + 1 < n:
        dust[x][y + 1] += a_per
    else:
        dust_cnt += a_per

    # 5%
    if 0 <= x < n and 0 <= y + 2 < n:
        dust[x][y + 2] += five_per
    else:
        dust_cnt += five_per

    # 10%
    if 0 <= x - 1 < n and 0 <= y + 1 < n:
        dust[x - 1][y + 1] += ten_per
    else:
        dust_cnt += ten_per
    if 0 <= x + 1 < n and 0 <= y + 1 < n:
        dust[x + 1][y + 1] += ten_per
    else:
        dust_cnt += ten_per

    # 7%
    if 0 <= x - 1 < n and 0 <= y < n:
        dust[x - 1][y] += seven_per
    else:
        dust_cnt += seven_per
    if 0 <= x + 1 < n and 0 <= y < n:
        dust[x + 1][y] += seven_per
    else:
        dust_cnt += seven_per

    # 2%
    if 0 <= x - 2 < n and 0 <= y < n:
        dust[x - 2][y] += two_per
    else:
        dust_cnt += two_per
    if 0 <= x + 2 < n and 0 <= y < n:
        dust[x + 2][y] += two_per
    else:
        dust_cnt += two_per

    # 1%
    if 0 <= x - 1 < n and 0 <= y - 1 < n:
        dust[x - 1][y - 1] += one_per
    else:
        dust_cnt += one_per
    if 0 <= x + 1 < n and 0 <= y - 1 < n:
        dust[x + 1][y - 1] += one_per
    else:
        dust_cnt += one_per

    return dust_cnt
# 아래
def cal_dir_1(x,y):
    dust_cnt = 0

    # a%
    if 0 <= x+1 < n and 0 <= y < n:
        dust[x+1][y] += a_per
    else:
        dust_cnt += a_per

    # 5%
    if 0 <= x+2 < n and 0 <= y < n:
        dust[x+2][y] += five_per
    else:
        dust_cnt += five_per

    # 10%
    if 0 <= x +1 < n and 0 <= y - 1 < n:
        dust[x + 1][y - 1] += ten_per
    else:
        dust_cnt += ten_per
    if 0 <= x + 1 < n and 0 <= y + 1 < n:
        dust[x + 1][y + 1] += ten_per
    else:
        dust_cnt += ten_per

    # 7%
    if 0 <= x < n and 0 <= y-1 < n:
        dust[x][y-1] += seven_per
    else:
        dust_cnt += seven_per
    if 0 <= x < n and 0 <= y+1 < n:
        dust[x][y+1] += seven_per
    else:
        dust_cnt += seven_per

    # 2%
    if 0 <= x < n and 0 <= y-2 < n:
        dust[x][y-2] += two_per
    else:
        dust_cnt += two_per
    if 0 <= x < n and 0 <= y+2 < n:
        dust[x][y+2] += two_per
    else:
        dust_cnt += two_per

    # 1%
    if 0 <= x - 1 < n and 0 <= y - 1 < n:
        dust[x - 1][y - 1] += one_per
    else:
        dust_cnt += one_per
    if 0 <= x - 1 < n and 0 <= y + 1 < n:
        dust[x - 1][y + 1] += one_per
    else:
        dust_cnt += one_per

    return dust_cnt
# 왼쪽
def cal_dir_2(x,y):
    dust_cnt=0

    # a%
    if 0<=x<n and 0<=y-1<n:
        dust[x][y-1]+=a_per
    else:
        dust_cnt+=a_per

    # 5%
    if 0 <= x < n and 0 <= y - 2 < n:
        dust[x][y - 2] += five_per
    else:
        dust_cnt += five_per

    # 10%
    if 0<=x-1<n and 0<=y-1<n:
        dust[x-1][y-1] += ten_per
    else:
        dust_cnt += ten_per
    if 0<=x+1<n and 0<=y-1<n:
        dust[x+1][y-1] += ten_per
    else:
        dust_cnt += ten_per

    # 7%
    if 0<=x-1<n and 0<=y<n:
        dust[x-1][y] += seven_per
    else:
        dust_cnt += seven_per
    if 0<=x+1<n and 0<=y<n:
        dust[x+1][y]+= seven_per
    else:
        dust_cnt += seven_per

    # 2%
    if 0 <= x - 2 < n and 0 <= y < n:
        dust[x - 2][y] += two_per
    else:
        dust_cnt += two_per
    if 0 <= x + 2 < n and 0 <= y < n:
        dust[x + 2][y] += two_per
    else:
        dust_cnt += two_per

    # 1%
    if 0 <= x - 1 < n and 0 <= y+1 < n:
        dust[x - 1][y+1] += one_per
    else:
        dust_cnt += one_per
    if 0 <= x + 1 < n and 0 <= y+1 < n:
        dust[x +1][y+1] += one_per
    else:
        dust_cnt += one_per
    return dust_cnt

# 위
def cal_dir_3(x,y):
    dust_cnt = 0

    # a%
    if 0 <= x - 1 < n and 0 <= y < n:
        dust[x - 1][y] += a_per
    else:
        dust_cnt += a_per

    # 5%
    if 0 <= x - 2 < n and 0 <= y < n:
        dust[x - 2][y] += five_per
    else:
        dust_cnt += five_per

    # 10%
    if 0 <= x - 1 < n and 0 <= y - 1 < n:
        dust[x - 1][y - 1] += ten_per
    else:
        dust_cnt += ten_per
    if 0 <= x - 1 < n and 0 <= y + 1 < n:
        dust[x - 1][y + 1] += ten_per
    else:
        dust_cnt += ten_per

    # 7%
    if 0 <= x < n and 0 <= y - 1 < n:
        dust[x][y - 1] += seven_per
    else:
        dust_cnt += seven_per
    if 0 <= x < n and 0 <= y + 1 < n:
        dust[x][y + 1] += seven_per
    else:
        dust_cnt += seven_per

    # 2%
    if 0 <= x < n and 0 <= y - 2 < n:
        dust[x][y - 2] += two_per
    else:
        dust_cnt += two_per
    if 0 <= x < n and 0 <= y + 2 < n:
        dust[x][y + 2] += two_per
    else:
        dust_cnt += two_per

    # 1%
    if 0 <= x + 1 < n and 0 <= y - 1 < n:
        dust[x + 1][y - 1] += one_per
    else:
        dust_cnt += one_per
    if 0 <= x + 1 < n and 0 <= y + 1 < n:
        dust[x + 1][y + 1] += one_per
    else:
        dust_cnt += one_per
    return dust_cnt
n=int(input())

dust = []
for i in range(n):
    dust.append(list(map(int, input().split())))

# 탐색(0,0->중앙까지 나선형으로 탐색 후 리버스)
dir = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}
orders = []
q=deque()
q.append([0,0,0]) # x,y,dir
visited = [[0 for _ in range(n)]for _ in range(n)]
visited[0][0]=1

while q:
    x,y,d=q.popleft()
    orders.append([x,y])

    if (x,y) == (n//2,n//2):
        break

    nx=x+dir[d][0]
    ny=y+dir[d][1]

    if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
        q.append([nx,ny,d])
        visited[nx][ny]=1
    else:
        d=(d+1)%4
        nx=x+dir[d][0]
        ny=y+dir[d][1]
        q.append([nx, ny, d])
        visited[nx][ny] = 1

orders=orders[::-1]
# print(orders)

start_x, start_y = 0,0
out_of_dust=0
for i in range(n*n-1):
    now_x, now_y=orders[i]
    n_x, n_y = orders[i+1]
    # 방향 획득
    direction = get_direction(now_x, now_y, n_x, n_y)

    tmp = dust[n_x][n_y]
    five_per = int(tmp * 0.05)
    ten_per = int(tmp * 0.1)
    two_per = int(tmp * 0.02)
    seven_per = int(tmp * 0.07)
    one_per = int(tmp * 0.01)

    a_per = tmp - five_per-ten_per*2-seven_per*2-two_per*2-one_per*2
    # 방향에 맞는 먼지 이동 함수 호출
    # 우측으로 이동
    if direction==0:
        out_of_dust+=cal_dir_0(n_x,n_y)
    # 아래로 이동
    elif direction == 1:
        out_of_dust+=cal_dir_1(n_x,n_y)
    # 왼쪽으로 이동
    elif direction == 2:
        out_of_dust+=cal_dir_2(n_x, n_y)
    # 위로 이동
    elif direction == 3:
        out_of_dust+=cal_dir_3(n_x,n_y)

    dust[n_x][n_y]=0
print(out_of_dust)