# 턴이 살아있는 동안 최대 백만개까지 몬스터가 살아있을 수 있다.
# 이말은 즉, 살아있는 몬스터를 배열로 관리하면. 100만번을 돌아야하는데, 이는 100번만 100만번인체로 돌면 시간초과다.
# 4*4 크기의 2차원 배열에서 그러면 몬스터를 효과적으로 관리하기 위해서는 겹치는 칸에 살아있는 몬스터를 개수로 관리해야한다.

# 3차원 배열은 [행][열][현재 바라보는 방향] 으로 구성한다. 이때, 값은 몇마리의 몬스터가 있는지를 나타낸다.
# 팩맨이 이동할때 특정 [행][열]에 있는 애들을 잡아먹는다.
# 이때, 시체도 분명 같은 칸에 존재하는 것이 있기 때문에, 딕셔너리로 관리하려고 한다.
# key = 좌표, value = 남아있는 가장 최신 시체의 사라지기 까지의 시간

# 팩맨의 모든 이동경로를 구한다.
import copy

def packman_available_move(tmp):
    if len(tmp) == 3:
        packman_move_list.append(copy.deepcopy(tmp))
        return

    for i in range(1,5):
        tmp.append(i)
        packman_available_move(tmp)
        tmp.pop()

def move_monster():
    new_monster_info = [[[0 for _ in range(9)]for _ in range(5)]for _ in range(5)]
    for x in range(1,5):
        for y in range(1,5):
            for k in range(1,9):
                if monster_info[x][y][k]!=0:
                    # 이동하려는 칸을 확인한다.
                    # 이동하려는 칸은 격자 안이며, 팩맨이 없고, 몬스터 시체가 없어야한다.
                    nx, ny = x+monster_dir[k][0], y+monster_dir[k][1]
                    if (1<=nx<=4 and 1<=ny<=4) and dead.get((nx,ny))==None and (nx,ny)!=(r,c):
                        new_monster_info[nx][ny][k]+=1
                    else: # 이동하지 못한다면
                        origin_dir = k
                        # 반시계로 돌리면서 이동 가능한 칸을 찾는다.
                        move_ok=False
                        cnt = 0
                        while cnt<7:
                            k = (k%8)+1
                            nx, ny = x+monster_dir[k][0], y+monster_dir[k][1]
                            cnt += 1
                            if (1<=nx<=4 and 1<=ny<=4) and dead.get((nx,ny))==None and (nx,ny)!=(r,c):
                                move_ok = True
                                break
                        # 반시계로 돌면서 이동 가능한 칸을 찾은 경우
                        if move_ok:
                            new_monster_info[nx][ny][k] += 1
                        # 이동 가능한 칸이 없는 경우는 아무것도 안하면 되므로 고려하지 않는다.
    return new_monster_info
def move_packman():
    global r,c
    eat_monster_cnt = -1
    first_x, first_y, sec_x, sec_y, third_x, third_y = 0,0,0,0,0,0

    for move in packman_move_list:
        first, sec, third = move[0], move[1], move[2]

        nx, ny= r +packman_dir[first][0], c+packman_dir[first][1]
        nnx, nny = nx+packman_dir[sec][0], ny+packman_dir[sec][1]
        nnnx, nnny = nnx+packman_dir[third][0], nny+packman_dir[third][1]

        # 3좌표가 격자 안인지를 파악하고, 하나라도 아니면 continue
        if not (1<=nx<=4 and 1<=ny<=4 and 1<=nnx<=4 and 1<=nny<=4 and 1<=nnnx<=4 and 1<=nnny<=4):
            continue

        # 첫번째와 세번째 위치가 같으면 한번만 잡아먹어야한다.
        if (nx, ny)==(nnnx,nnny):
            eat_cnt = sum(monster_info[nx][ny]) + sum(monster_info[nnx][nny])
        else:
            eat_cnt = sum(monster_info[nx][ny]) + sum(monster_info[nnx][nny]) + sum(monster_info[nnnx][nnny])

        # 먹은 횟수 더 큰지 비교
        if eat_monster_cnt<eat_cnt:
            eat_monster_cnt = eat_cnt
            first_x, first_y, sec_x, sec_y, third_x, third_y = nx,ny, nnx, nny, nnnx, nnny

    # 팩맨이 갈 위치를 찾았으니, 해당 위치로 이동시키고, 시체를 만들어 준다.
    r,c = third_x, third_y

    # 먹는다. => 그 좌표의 몬스터의 개수는 0
    for i in range(1, 9):
        monster_info[first_x][first_y][i]=0
        monster_info[sec_x][sec_y][i] = 0
        monster_info[third_x][third_y][i] = 0

    # 시체를 만든다.
    dead[(first_x, first_y)] = 3
    dead[(sec_x, sec_y)] = 3
    dead[(third_x, third_y)] = 3

monster_dir = {1:[-1,0],2:[-1,-1],3:[0,-1],4:[1,-1],5:[1,0],6:[1,1],7:[0,1],8:[-1,1]} # 몬스터 방향
packman_dir = {1:[-1,0],2:[0,-1],3:[1,0],4:[0,1]} # 팩맨 방향
packman_move_list = []
packman_available_move([])

m,t = map(int, input().split()) # m: 몬스터 마리수, t: 턴의 수
r,c = map(int, input().split()) # r,c: 팩맨 위치

# 몬스터의 위치 정보를 나타낼 3차원 배열
monster_info = [[[0 for _ in range(9)]for _ in range(5)]for _ in range(5)]
# 시체를 나타낼 딕셔너리
dead={}
for _ in range(m):
    x,y,d = map(int, input().split())
    monster_info[x][y][d]+=1

for _ in range(t):

    # 몬스터 복제 시도
    # 몬스터 정보를 보고, 몇개의 알을 낳을지를 딕셔너리로 관리
    egg={}
    for x in range(1,5):
        for y in range(1,5):
            for k in range(1,9):
                if monster_info[x][y][k]!=0:
                    egg[(x,y,k)] = monster_info[x][y][k]

    # 몬스터 이동
    monster_info = move_monster()

    # 팩맨 이동
    move_packman()

    # 몬스터 시체 소멸
    key_list = dead.keys()
    for key in key_list:
        if dead[key]-1 == 0:
            del dead[key]
        else:
            dead[key] = dead[key]-1

    # 몬스터 복제
    for x,y,k in egg.keys():
        monster_info[x][y][k] +=1

# 몬스터 출력
answer = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,9):
            answer+=monster_info[i][j][k]
print(answer)