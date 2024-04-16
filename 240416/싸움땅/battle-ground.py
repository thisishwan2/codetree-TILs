import heapq

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


def get_next(x,y,d):
    nx=x+dx[d]
    ny=y+dy[d]

    # 다음칸이 격자 밖이면 반대로 움직인다.
    if not in_range(nx,ny):
        d=d+2
        if d>3:
            d=d-4

        nx=x+dx[d]
        ny=y+dy[d]

    return nx,ny,d

def find_player(nx,ny):
    for i in range(m):
        num, x, y, d, s, attack = player[i]
        if (nx,ny)==(x,y):
            return player[i]

    return EMPTY

def update(curr_player):
    player_num = curr_player[0]
    for i in range(m):
        player_num_i , x,y,d,s,attack = player[i]

        if player_num_i==player_num:
            player[i] = curr_player
            break

def get_gun(curr_player):
    num, x, y, d, s, attack = curr_player

    heapq.heappush(gun[x][y], -1*attack)
    attack = -1 * heapq.heappop(gun[x][y])

    curr_player = [num, x, y, d, s, attack]
    update(curr_player)

def loser_move(p): # 싸움에서 진 플레이어는 총을 격자에 내려놀고, 빈칸을 찾아 이동하고, 빈 곳에서 총을 얻는다.
    num, x, y, d, s, attack = p

    # 현재 위치에 총을 놓는다.
    heapq.heappush(gun[x][y], -1*attack)

    # 빈공간을 찾는다.
    for i in range(4):
        nd = (d+i)%4
        nx=x+dx[nd]
        ny=y+dy[nd]

        if in_range(nx,ny) and find_player(nx, ny) == EMPTY:
            p = [num, nx, ny, nd, s, 0]
            get_gun(p)
            break

def duel(p1, p2):
    num1, x1, y1, d1, s1, attack1 = p1
    num2, x2, y2, d2, s2, attack2 = p2

    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로 우선순위를 매겨 비교합니다.

    # p1이 이긴 경우
    if (s1 + attack1, s1) > (s2 + attack2, s2): # 이렇게 비교하면 첫 파라미터 비교후 같은 경우 두번째 파라미터를 비교한다.
        # p1은 포인트를 얻는다.
        point[num1] += (s1+attack1) - (s2+attack2)
        # p2는 진 사람의 움직임을 진행한다.
        loser_move(p2)
        # p1은 격자와 총을 교환함
        get_gun(p1)

    # p2가 이긴 경우
    else:
        point[num2] += (s2+attack2) - (s1+attack1)
        loser_move(p1)
        get_gun(p2)


def simulate():
    for i in range(m):

        num, x, y, d, s, attack = player[i]

        # 1-1. 연재 플레이어가 이동할 위치와 방향을 구합니다.
        nx, ny, nd = get_next(x,y,d)

        # 해당 위치에 있는 전 플레이어 정보를 얻는다.
        next_player = find_player(nx,ny)

        # 현재 플레이어의 위치와 방향을 바꿔준다.
        curr_player = [num, nx, ny, nd, s, attack]
        update(curr_player)

        # 2. 해당 위치로 이동한다.
        # 2.1 해당 위치에 플레이어가 없으면 그대로 움직인다.(사실 이미 움직이긴 했고 총을 교환하는 작업임)
        if next_player == EMPTY:
            get_gun(curr_player)
        # 2.2 만약 해당 위치에 플레이어가 있으면 싸운다.
        else:
            duel(curr_player, next_player)





EMPTY = [-1, -1, -1, -1, -1, -1] # 다음칸에 플레이어가 없을때 반환할 리스트

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,k = map(int, input().split())

gun = [ [[] for _ in range(n)] for _ in range(n) ]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        # 총이 놓여 있는 칸입니다.
        if nums[j] != 0:
            heapq.heappush(gun[i][j], -1 * nums[j]) # 각 칸의 리스트는 힙을 따라서 정렬

player = []
for i in range(m):
    x,y,d,s = map(int, input().split())
    player.append([i,x-1,y-1,d,s,0])

point = [0]*m

for _ in range(k):
    simulate()

print(*point)