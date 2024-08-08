# import copy


# def move(posion, dx, dy, move_cnt):
#     new_posion = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if posion[i][j] == 1:
#                 nx = i + dx * move_cnt
#                 ny = j + dy * move_cnt

#                 if nx < 0:
#                     nx = n + nx
#                 elif nx >= n:
#                     nx = nx - n

#                 if ny < 0:
#                     ny = n + ny
#                 elif ny >= n:
#                     ny = ny - n

#                 new_posion[nx][ny] = 1
#     return new_posion


# def posion_input(leavero, posion):
#     for i in range(n):
#         for j in range(n):
#             if posion[i][j] == 1:
#                 leavero[i][j] += 1


# def height_up(leavero, posion):
#     dx = [-1, -1, 1, 1]
#     dy = [-1, 1, -1, 1]
#     res = copy.deepcopy(leavero)

#     for i in range(n):
#         for j in range(n):
#             cnt = 0
#             if posion[i][j] == 1:
#                 for k in range(4):
#                     nx = i + dx[k]
#                     ny = j + dy[k]

#                     if 0 <= nx < n and 0 <= ny < n:
#                         if leavero[nx][ny] >= 1:
#                             cnt += 1
#                 res[i][j] += cnt
#     return res


# def cut(leavero, posion):
#     new_posion = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if posion[i][j] != 1:
#                 if leavero[i][j] >= 2:
#                     leavero[i][j] -= 2
#                     new_posion[i][j] = 1
#     return new_posion


# dir = {1: (0, 1), 2: (-1, 1), 3: (-1, 0), 4: (-1, -1), 5: (0, -1), 6: (1, -1), 7: (1, 0), 8: (1, 1)}

# # 초기 특수 영양제는 n x n 격자의 좌하단의 4개의 칸에 주어집니다.
# # 영양제 이동은 즉 격자 바깥으로 나가면 마치 지구가 둥근것처럼 반대편으로 돌아옵니다. => 예제에서 4,2 => 1,0 으로 가는 경우
# # 높이가 0인 리브로수는 새싹만 존재하는 땅을 의미합니다.
# n, m = map(int, input().split())

# leavero = []

# for i in range(n):
#     leavero.append(list(map(int, input().split())))

# move_rule = []  # 이동 방향, 이동 칸수
# for i in range(m):
#     move_rule.append(list(map(int, input().split())))

# # 영양제 위치 지정
# posion = [[0 for _ in range(n)] for _ in range(n)]
# posion[n - 2][0] = 1
# posion[n - 1][0] = 1
# posion[n - 2][1] = 1
# posion[n - 1][1] = 1

# for i in move_rule:
#     direction = i[0]
#     move_cnt = i[1]
#     dx, dy = dir.get(direction)

#     # 영양제 이동
#     posion = move(posion, dx, dy, move_cnt)

#     # 영양제 투약
#     posion_input(leavero, posion)

#     # 대각선 인접한 1이상의 리브로수의 개수만큼 높이 증가
#     leavero = height_up(leavero, posion)

#     # 영양제 맞은땅 제외 높이 2 이상인 리브로수의 높이를 2만큼 자르고 해당 위치에 영양제 위치시킨다.
#     posion = cut(leavero, posion)

# total = 0
# for i in range(n):
#     for j in range(n):
#         total += leavero[i][j]
# print(total)

# 나무 타이쿤

def energy_move(d,p):
    new_energy=[]
    for x,y in energy:
        nx=x+dir[d][0]*p
        ny=y+dir[d][1]*p

        if 0<=nx<n and 0<=ny<n:
            new_energy.append([nx,ny])
        else:
            if nx<0:
                nx=n+nx
            elif nx>=n:
                nx=nx-n

            if ny < 0:
                ny = n + ny
            elif ny >= n:
                ny = ny-n
            new_energy.append([nx, ny])

    return new_energy

def energy_injection():
    for x,y in energy:
        leaverose[x][y] +=1

def check_near_lenght():
    for x,y in energy:
        cnt=0
        for i in range(2,9,2):
            nx=x+dir[i][0]
            ny=y+dir[i][1]

            if 0<=nx<n and 0<=ny<n:
                if leaverose[nx][ny]>=1:
                    cnt+=1

        leaverose[x][y]+=cnt

def cut():
    new_energy=[]
    for i in range(n):
        for j in range(n):
            if [i,j] not in energy and leaverose[i][j]>=2:
                leaverose[i][j]-=2
                new_energy.append([i,j])
    return new_energy


# 이동 좌표
dir = {1:[0,1], 2:[-1,1], 3:[-1,0], 4:[-1,-1], 5:[0,-1], 6:[1,-1], 7:[1,0], 8:[1,1]}

n,m = map(int, input().split()) # n: 격자의 크기, m: 리브로수를 키우는 총 년
leaverose = []
for i in range(n):
    leaverose.append(list(map(int, input().split())))

# 특수 영양제 좌표(초기에는 좌측 하단 4개)
energy=[[n-2,0],[n-1,0],[n-2,1],[n-1,1]]

for _ in range(m):
    d,p = map(int, input().split())

    # 영양제 이동
    energy = energy_move(d,p)

    # 이동시킨 땅에 영양제 투입
    energy_injection()

    # 인접한 대각선의 높이를 확인하여 증가
    check_near_lenght()

    # 특수 영양제 투입 리브로브 제외 높이가 2이상인 리브로브는 높이 2를 잘라내고, 특수 영양제의 위치로 둔다.
    energy = cut()

# 남아있는 높이 총합을 계산
answer = 0
for i in range(n):
    answer+=sum(leaverose[i])

print(answer)