from collections import deque

def choose_attacker():
    damage = 1e9
    ax = 0
    ay = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: continue
            # 공격력이 작으면
            if arr[i][j] < damage:
                damage = arr[i][j]
                ax = i
                ay = j
            # 공격력이 낮은 포탑이 2개 이상이면    
            elif arr[i][j] == damage:
                if attack_time[i][j] > attack_time[ax][ay]:  # 공격시간이 더 최근이면
                    ax = i
                    ay = j
                elif attack_time[i][j] == attack_time[ax][ay]:  # 공격 시간도 동일하면
                    if i + j > ax + ay:
                        ax = i
                        ay = j
                    elif i + j == ax + ay:
                        if j > ay:
                            ax = i
                            ay = j

    return ax, ay


def choose_target():
    damage = -1
    tx = 0
    ty = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: continue
            if (i,j) == (ax,ay): continue
            if arr[i][j] > damage:
                damage = arr[i][j]
                tx = i
                ty = j
            elif arr[i][j] == damage:
                if attack_time[i][j] < attack_time[tx][ty]:  # 공격한지 오래됐다면
                    tx = i
                    ty = j
                elif attack_time[i][j] == attack_time[tx][ty]:  # 공격 시간도 동일하다면
                    if i + j < tx + ty:  # 행열 합이 더 작다면
                        tx = i
                        ty = j
                    elif i + j == tx + ty:
                        if j < ty:
                            tx = i
                            ty = j
    return tx, ty


def laser():
    q = deque()
    q.append([ax, ay, []])  # x,y,지나온 경로
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[ax][ay] = 1

    while q:
        x, y, route = q.popleft()
        for i in range(4):
            # 가장자리에서 건너편으로 넘어가는 경우를 고려
            nx = (x + dx[i]) % n
            ny = (y + dy[i]) % m

            if 0 <= nx < n and 0 <= ny < m:
                # 부서진 포탑이 아니고, 방문하지 않았으면
                if arr[nx][ny] != 0 and visited[nx][ny] == 0:

                    # 타겟에 도달한 경우
                    if (nx, ny) == (tx, ty):
                        arr[nx][ny] -= damage
                        for rx, ry in route:
                            arr[rx][ry] -= half_damage
                            attack[rx][ry] = True  # 공격에 관여함
                        return True
                    else:
                        visited[nx][ny] = 1
                        tmp = route[:]
                        tmp.append([nx, ny])
                        q.append([nx, ny, tmp])
                        # q.append([nx,ny,route.append([nx,ny])]) 이렇게 하면 route.apppend 하고 None을 반환해서 안됨
    return False  # 레이저 공격이 불가능한 경우


def bomb():
    arr[tx][ty] -= damage  # 타겟에는 공격력 만큼 피해
    bomb_dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    bomb_dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 주변 8개 방향에 포탑에 피해
    for i in range(8):
        nx = (tx + bomb_dx[i]) % n
        ny = (ty + bomb_dy[i]) % m

        # 공격자가 주변 8개 범위에 있으면 공격을 받지 않는다.
        if (nx, ny) == (ax, ay): continue

        arr[nx][ny] -= half_damage
        attack[nx][ny] = True


def check_destory():
    for i in range(n):
        for j in range(m):
            if arr[i][j] < 0:
                arr[i][j] = 0


def refactor_tower():
    tower_cnt = 0
    tower_list = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] ==0: continue
            tower_cnt+=1
            if attack[i][j]: continue
            tower_list.append((i,j))

    # 타워가 하나만 남으면, 최대값을 출력하고 종료(이부분을 체크 안하면 하나만 남았지만, 계속 진행되어서 이상한 답이 나옴)
    if tower_cnt == 1:
        print(get_max())
        exit(0)
    for i,j in tower_list:
        arr[i][j] += 1

def get_max():
    maxi = 0
    for i in range(n):
        maxi = max(maxi, max(arr[i]))
    return maxi

n, m, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

attack_time = [[0 for _ in range(m)] for _ in range(n)]  # 공격한 시간을 기록
time = 1

for i in range(k):

    # 공격과 관련있는지를 파악하기 위해 사용(4번 포탑 정비시 필요)
    attack = [[False for _ in range(m)] for _ in range(n)]

    # 1번
    ax, ay = choose_attacker()
    arr[ax][ay] += n + m  # 공격자 포탑 공격력 증가
    damage = arr[ax][ay]
    half_damage = arr[ax][ay] // 2
    attack[ax][ay] = True  # 공격에 관여함을 표시
    attack_time[ax][ay] = time  # 공격한 시점 표시
    time += 1

    # 2번
    # 타겟 위치 확인
    tx, ty = choose_target()
    attack[tx][ty] = True
    # 레이저 공격이 안되는 경우
    if not laser():
        bomb()

    # 3번
    check_destory()

    # 4번
    refactor_tower()


print(get_max())