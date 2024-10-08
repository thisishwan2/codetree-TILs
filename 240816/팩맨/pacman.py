# 팩맨
import copy

def packman_available_move(tmp):
    if len(tmp) == 3:
        packman_move_list.append(copy.deepcopy(tmp))
        return

    for i in range(1,5):
        tmp.append(i)
        packman_available_move(tmp)
        tmp.pop()

def monster_move(monster_coordinate, monster_direction):
    new_monster_coordinate = []
    new_monster_direction = []
    for coordinate, direction in zip(monster_coordinate, monster_direction):
        x,y = coordinate
        for _ in range(8):
            nx, ny = x + monster_dir[direction][0], y + monster_dir[direction][1]
            if (1 <= nx <= 4 and 1 <= ny <= 4) and ([nx, ny] not in dead_coordinate) and ((nx, ny) != (r, c)):
                new_monster_coordinate.append([nx, ny])
                new_monster_direction.append(direction)
                break
            direction = (direction % 8) + 1
        else:
            new_monster_coordinate.append([x, y])
            new_monster_direction.append(direction)

    return new_monster_coordinate, new_monster_direction

def packman_move():
    global r,c, monster_direction, monster_coordinate
    max_eat_cnt = -1
    move_idx = 0
    # 팩맨이 이동할 길을 찾는다.
    for idx, val in enumerate(packman_move_list):
        first, sec, third = val[0],val[1],val[2]

        first_x, first_y = r+packman_dir[first][0], c+packman_dir[first][1]
        sec_x, sec_y = first_x + packman_dir[sec][0], first_y + packman_dir[sec][1]
        third_x, third_y = sec_x + packman_dir[third][0], sec_y + packman_dir[third][1]

        # 한군데라도 격자를 벗어나지 않아야한다.
        if 1<=first_x<=4 and 1<=first_y<=4 and 1<=sec_x<=4 and 1<=sec_y<=4 and 1<=third_x<=4 and 1<=third_y<=4:
            first_eat = monster_coordinate.count([first_x, first_y])
            sec_eat = monster_coordinate.count([sec_x, sec_y])
            third_eat = monster_coordinate.count([third_x, third_y])

            # 처음과 3번째가 갖은 좌표면 세번째 좌표의 몬스터는 이미 먹은 것이다.
            if (first_x, first_y)==(third_x, third_y):
                total_eat = first_eat+sec_eat
            else:
                total_eat = first_eat + sec_eat+ third_eat

            # 비교
            if max_eat_cnt<total_eat:
                max_eat_cnt=total_eat
                move_idx=idx

    # 이동할 길을 찾았으면, 실제 몬스터를 먹고 시체로 만든다.
    f,s,th = packman_move_list[move_idx]
    first_x, first_y = r + packman_dir[f][0], c + packman_dir[f][1]
    sec_x, sec_y = first_x + packman_dir[s][0], first_y + packman_dir[s][1]
    third_x, third_y = sec_x + packman_dir[th][0], sec_y + packman_dir[th][1]

    # 팩맨 위치 최신화
    r,c = third_x, third_y

    remove_monster_idx =[]
    # 시체 될 것들을 리스트에 담고
    for idx, (coordinate, direction) in enumerate(zip(copy.deepcopy(monster_coordinate), copy.deepcopy(monster_direction))):
        if[first_x, first_y] == coordinate or [sec_x, sec_y] == coordinate or [third_x, third_y] == coordinate:
            dead_coordinate.append(coordinate)
            dead_leave_cnt.append(3)
            remove_monster_idx.append(idx)

    monster_coordinate = [m for i, m in enumerate(monster_coordinate) if i not in remove_monster_idx]
    monster_direction = [d for i, d in enumerate(monster_direction) if i not in remove_monster_idx]

monster_dir = {1:[-1,0],2:[-1,-1],3:[0,-1],4:[1,-1],5:[1,0],6:[1,1],7:[0,1],8:[-1,1]} # 몬스터 방향
packman_dir = {1:[-1,0],2:[0,-1],3:[1,0],4:[0,1]} # 팩맨 방향
packman_move_list = []
packman_available_move([])

m,t = map(int, input().split()) # m: 몬스터 마리수, t: 턴수
r,c = map(int, input().split()) # r,c: 초기 위치

monster_coordinate = []
monster_direction = []
dead_coordinate = []
dead_leave_cnt = []

for _ in range(m):
    x,y,d = map(int, input().split()) # x,y: 몬스터 위치, d: 방향 정보
    monster_coordinate.append([x,y])
    monster_direction.append(d)

for _ in range(t):
    egg = [] # 몬스터 복제시 담을 알
    egg_direction = [] # 알의 방향

    # 1번 몬스터 복제 시도
    for coordinate, direction in zip(monster_coordinate, monster_direction):
        egg.append(coordinate)
        egg_direction.append(direction)

    # 2번 몬스터 이동
    monster_coordinate, monster_direction = monster_move(monster_coordinate, monster_direction)

    # 3번 팩맨 이동
    packman_move()

    # 4번 시체 소멸
    new_dead_coordinate=[]
    new_dead_leave_cnt = []
    for coordinate, cnt in zip(dead_coordinate, dead_leave_cnt):
        if cnt-1==0:
            continue
        else:
            new_dead_coordinate.append(coordinate)
            new_dead_leave_cnt.append(cnt-1)
    dead_coordinate=new_dead_coordinate
    dead_leave_cnt=new_dead_leave_cnt

    # 5번 몬스터 복제
    monster_coordinate += egg
    monster_direction += egg_direction

print(len(monster_coordinate))