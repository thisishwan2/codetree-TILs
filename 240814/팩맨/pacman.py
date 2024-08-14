import copy
from collections import deque
m,t = map(int, input().split()) # m:몬스터 수, t: 턴수
pr,pc = map(int, input().split()) # 초기위치

monster = deque()
dead = [] # 힙으로 둔다.

dx=[0,-1,-1,0,1,1,1,0,-1]
dy=[0,0,-1,-1,-1,0,1,1,1]

# 상좌하우
p_d={1:[-1,0],2:[0,-1],3:[1,0],4:[0,1]}
p_move=[]
# 팩맨의 이동 순서를 모두 만들어 놓는다.
def dfs(tmp):
    if len(tmp) == 3:
        p_move.append(copy.deepcopy(tmp))
        return

    for i in range(1, 5):
        tmp.append(i)
        dfs(tmp)
        tmp.pop()

dfs([])

for i in range(m):
    r,c,d = map(int, input().split())
    monster.append([r,c,d])

for _ in range(t):
    egg = []
    monster_coordi={}

    # 1. 몬스터 복제 시도(현재 위치에 자신과 같은 방향의 몬스터 알을 만든다.)
    for r,c,d in monster:
        egg.append([r,c,d])

    # 2. 몬스터 이동(움직이려는 방향의 칸에 시체, 팩맨, 격자 밖이면 반시계 45도로 회전 후 움직일 수 있는지 체크)
    # 못간다면, 가능할때 까지 45도 돈다. 움직일 수 없다면 안 움직임.
    for _ in range(len(monster)):
        r,c,d = monster.popleft()
        nr, nc = r+dx[d], c+dy[d]
        # 다음 위치 좌표에 팩맨이 있거나, 격자를 벗어나거나, 시체가 있다면,
        if not(1<=nr<=4 and 1<=nc<=4) or ([nr,nc] in dead) or ((nr,nc)==(pr,pc)):
            flag = False # 이동 가능 여부를 확인
            cnt=0
            # 반시계로 회전한다.
            while cnt<7:
                d=(d+1)%9
                if d==0:
                    d+=1
                nr, nc = r + dx[d], c + dy[d]
                cnt+=1
                # 이동 조건에 충족한다면
                if (1 <= nr <= 4 and 1 <= nc <= 4) and ([nr, nc] not in dead) and ((nr, nc) != (pr, pc)):
                    flag = True
                    break
            if flag == True:
                monster.append([nr, nc, d])
                if monster_coordi.get((nr,nc)) == None:
                    monster_coordi[(nr,nc)]=1
                else:
                    monster_coordi[(nr,nc)]+=1
        # 조건 충족시 이동
        elif (1 <= nr <= 4 and 1 <= nc <= 4) and ([nr, nc] not in dead) and ((nr, nc) != (pr, pc)):
            # 이동한다.
            monster.append([nr,nc,d])
            if monster_coordi.get((nr, nc)) == None:
                monster_coordi[(nr, nc)] = 1
            else:
                monster_coordi[(nr, nc)] += 1

    move_candidate=""
    eat_cnt=0
    # 3. 팩맨 이동(팩맨은 3칸을 이동한다.)
    for first, sec, third in p_move:
        npr, npc = pr+p_d[first][0], pc+p_d[first][1]
        nnpr, nnpc = npr+p_d[sec][0], npc+p_d[sec][1]
        nnnpr, nnnpc = nnpr+p_d[third][0], nnpc+p_d[third][1]

        can_eat_count = 0
        # 격자 안에 있는지를 확인
        if 1<=npr<=4 and 1<=npc<=4 and 1<=nnpr<=4 and 1<=nnpc<=4 and 1<=nnnpr<=4 and 1<=nnnpc<=4:
            # 먹을 수 있는 몬스터 수
            if (npr,npc) in monster_coordi:
                can_eat_count+=monster_coordi[(npr,npc)]
            if (nnpr,nnpc) in monster_coordi:
                can_eat_count += monster_coordi[(nnpr, nnpc)]
            if (nnnpr,nnnpc) in monster_coordi and (nnnpr,nnnpc)!=(npr,npc):
                can_eat_count += monster_coordi[(nnnpr, nnnpc)]

        if can_eat_count>eat_cnt:
            eat_cnt=can_eat_count
            move_candidate=[first, sec, third]

    # 이동할 좌표를 구했으면, 이동하고, 먹은 팩맨들은 시체 처리한다.
    first, sec, third = move_candidate[0], move_candidate[1], move_candidate[2]
    npr, npc = pr + p_d[first][0], pc + p_d[first][1]
    nnpr, nnpc = npr + p_d[sec][0], npc + p_d[sec][1]
    nnnpr, nnnpc = nnpr + p_d[third][0], nnpc + p_d[third][1]

    # 시체를 먼저 만든다.
    if (npr,npc) in monster_coordi:
        for i in range(monster_coordi[(npr,npc)]):
            dead.append([npr,npc,3])
    if (nnpr,nnpc) in monster_coordi:
        for i in range(monster_coordi[(nnpr,nnpc)]):
            dead.append([nnpr,nnpc,3])
    if (nnnpr,nnnpc) in monster_coordi:
        for i in range(monster_coordi[(nnnpr,nnnpc)]):
            dead.append([nnnpr,nnnpc,3])

    # monster 큐에서 해당하는 좌표는 지운다.(for문?)
    remove_list=[]
    for i in monster:
        if (i[0],i[1]) == (npr,npc) or (i[0],i[1]) == (nnpr,nnpc) or (i[0],i[1]) == (nnnpr,nnnpc):
            remove_list.append(i)
    for i in remove_list:
        monster.remove(i)

    # 팩맨 위치 최신화
    pr = nnnpr
    pc = nnnpc

    # 4. 시체 소멸
    new_dead = []
    for i in dead:
        if i[2]-1 == 0:
            continue
        else:
            new_dead.append([i[0],i[1],i[2]-1])

    # 몬스터 복제
    for i in egg:
        monster.append(i)

print(len(monster))