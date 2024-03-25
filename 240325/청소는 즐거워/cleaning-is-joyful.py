def dust_left(arr, x, y):
    cal = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01,0], [0, 0, 0.02, 0, 0]]

    now = arr[x][y]  # 본 배열의 먼지 값
    a_x, a_y = 2, 1  # a의 위치 인덱스
    cal_res = [[0 for _ in range(5)] for _ in range(5)]

    total = 0  # 계산된 먼지 총합

    for i in range(5):
        for j in range(5):
            if cal[i][j] != 0:
                calcu = int(cal[i][j] * now)
                cal_res[i][j] = calcu
                total += calcu

    cal_res[a_x][a_y] = arr[x][y] - total

    # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
    x_plus = x - 2
    y_plus = y - 2

    # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
    for i in range(5):
        for j in range(5):
            if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
                arr[i + x_plus][j + y_plus] += cal_res[i][j]

    arr[x][y] = 0
    # print(arr)
    return arr

def dust_right(arr, x, y):
    cal = [[0, 0, 0.02, 0, 0], [0, 0.01, 0.07, 0.1, 0], [0, 0, 0, 0, 0.05], [0, 0.01, 0.07, 0.1,0], [0, 0, 0.02, 0, 0]]

    now = arr[x][y]  # 본 배열의 먼지 값
    a_x, a_y = 2, 3  # a의 위치 인덱스
    cal_res = [[0 for _ in range(5)] for _ in range(5)]

    total = 0  # 계산된 먼지 총합

    for i in range(5):
        for j in range(5):
            if cal[i][j] != 0:
                calcu = int(cal[i][j] * now)
                cal_res[i][j] = calcu
                total += calcu

    cal_res[a_x][a_y] = arr[x][y] - total

    # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
    x_plus = x - 2
    y_plus = y - 2

    # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
    for i in range(5):
        for j in range(5):
            if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
                arr[i + x_plus][j + y_plus] += cal_res[i][j]

    arr[x][y] = 0
    # print(arr)
    return arr

def dust_up(arr, x, y):
    cal = [[0,0,0.05,0,0], [0,0.1,0,0.1,0], [0.02,0.07,0,0.07,0.02], [0,0.01,0,0.01,0], [0,0,0,0,0]]

    now = arr[x][y]  # 본 배열의 먼지 값
    a_x, a_y = 1, 2  # a의 위치 인덱스
    cal_res = [[0 for _ in range(5)] for _ in range(5)]

    total = 0  # 계산된 먼지 총합

    for i in range(5):
        for j in range(5):
            if cal[i][j] != 0:
                calcu = int(cal[i][j] * now)
                cal_res[i][j] = calcu
                total += calcu

    cal_res[a_x][a_y] = arr[x][y] - total

    # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
    x_plus = x - 2
    y_plus = y - 2

    # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
    for i in range(5):
        for j in range(5):
            if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
                arr[i + x_plus][j + y_plus] += cal_res[i][j]

    arr[x][y] = 0
    # print(arr)
    return arr

def dust_down(arr, x, y):
    cal = [[0,0,0,0,0], [0,0.01,0,0.01,0], [0.02,0.07,0,0.07,0.02], [0,0.1,0,0.1,0], [0,0,0.05,0,0]]

    now = arr[x][y]  # 본 배열의 먼지 값
    a_x, a_y = 3, 2  # a의 위치 인덱스
    cal_res = [[0 for _ in range(5)] for _ in range(5)]

    total = 0  # 계산된 먼지 총합

    for i in range(5):
        for j in range(5):
            if cal[i][j] != 0:
                calcu = int(cal[i][j] * now)
                cal_res[i][j] = calcu
                total += calcu

    cal_res[a_x][a_y] = arr[x][y] - total

    # 원래 배열에서의 위치와 현재 중앙으로 옮긴 위치까지 평행이동의 값
    x_plus = x - 2
    y_plus = y - 2

    # 이제 원래 배열에서 위의 계산 결과를 가지고 먼지를 더해줘야함
    for i in range(5):
        for j in range(5):
            if 0 <= i + x_plus < n and 0 <= j + y_plus < n:
                arr[i + x_plus][j + y_plus] += cal_res[i][j]

    arr[x][y] = 0
    # print(arr)
    return arr


def check_dir(dir, direction, x, y, visited):
    new_dir = 0
    if direction == 1:
        new_dir = 3
    elif direction == 2:
        new_dir = 4
    elif direction == 3:
        new_dir = 2
    else:
        new_dir = 1

    nx = x + dir.get(new_dir)[0]
    ny = y + dir.get(new_dir)[1]

    if visited[nx][ny] == 0:
        return new_dir
    else:
        return direction


dir = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 전체 먼지수 구하기
total_dust = 0
for i in range(n):
    for j in range(n):
        total_dust += arr[i][j]

# 전체 탐색 횟수
time = n * 2 - 1

x = n // 2
y = n // 2
direction = 3
visited = [[0 for _ in range(n)] for _ in range(n)]
visited[x][y] = 1

for i in range(n * n - 1):
    direc = dir.get(direction)
    nx = x + direc[0]
    ny = y + direc[1]
    visited[nx][ny] = 1

    x=nx
    y=ny

    # 먼지 계산
    if direction == 1: # 윗 방향
        dust_up(arr,x,y)
    elif direction == 2: # 아래
        dust_down(arr,x,y)
    elif direction == 3: #좌측
        dust_left(arr,x,y)
    else: # 우측
        dust_right(arr,x,y)



    # 방향을 왼쪽을 90도 회전시킨 방문 배열에 이미 방문한 적이 있으면, 그냥 지금 방향 그대로 진행
    direction = check_dir(dir, direction, x, y, visited)

# for문 다돌고 나서, 배열 전체를 한번 다시 탐색을 해서 남아있는 먼지를 구하고, 전체 먼지에서 빼면 격자 밖으로 나간 먼지를 구할 수 잇음
dust = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            dust += arr[i][j]

print(total_dust - dust)