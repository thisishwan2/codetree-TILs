def near_santas(santas, Rr, Rc):
    near_santa_list=[] # 모든 산타와 루돌프의 거리를 비교해서 정보를 넣을 리스트

    # 거리 구하기
    for idx, santa in enumerate(santas):
        # 산타 x,y,산타의 충돌 및 탈락 여부
        santa_x, santa_y, santa_over = santa[1], santa[2], santa[3]

        # 탈락한 산타이면, continue
        if santa[3] == 2:
            continue

        # 거리 계산
        distance = (Rr - santa_x)**2 + (Rc - santa_y)**2

        # 거리, x, y 좌표, 충돌 및 탈락 여부
        near_santa_list.append([distance, santa_x, santa_y, santa_over, idx])

    # 거리, x좌표, y좌표 순으로 정렬
    near_santa_list.sort(key = lambda x:(x[0], -x[1], -x[2]))

    return near_santa_list[0] # 가장 가까운 산타 리스트 반환

# 루돌프 이동후 좌표
def move_rudolf(Sx,Sy,Rr,Rc):
    dx=[-1,-1,-1,0,1,1,1,0]
    dy=[-1,0,1,1,1,0,-1,-1]

    min_distance = (Sx-Rr)**2 + (Sy-Rc)**2

    for i in range(8):
        nRr, nRc = Rr+dx[i], Rc+dy[i]

        if 0<nRr<=N and 0<nRc<=N:
            distance = (Sx-nRr)**2 + (Sy-nRc)**2

            if distance<min_distance:
                next_x=nRr
                next_y=nRc
                dir = i
                min_distance = distance

    return next_x, next_y, dx[dir], dy[dir] # 다음 루돌프 x,y, 어느방향으로 몇정도 움직인지

def crash_rudolf(Rr, Rc, near_santa_index):
    # 충돌한다면
    if (santas[near_santa_index][1], santas[near_santa_index][2]) == (Rr, Rc):
        return True
    else:
        False

# 재귀를 통해서 연쇄작용을 구현한다.(중요)
def fly_santa(fly_santa_index, santas, next_x, next_y): # 날라가는 산타 인덱스, 산타 배열, x,y좌표로 몇만큼이동하는지 수치(dx,dy)
    for index, s in enumerate(santas):
        # 날라가는 산타랑 인덱스가 다르고(탈락여부는 확인안해도 되나?)
        if index != fly_santa_index:
            if s[1] == santas[fly_santa_index][1] and s[2] == santas[fly_santa_index][2]: #날라간 위치에 다른 산타가 있으먄
                s[1] += next_x
                s[2] += next_y
                fly_santa(index, santas, next_x, next_y)

# 산타 이동
def move_santa(santa, Rr, Rc):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    distance = (santa[1]-Rr)**2 + (santa[2]-Rc)**2
    next_x = 0
    next_y = 0
    dir = 0

    for i in range(4):
        nx = dx[i]+santa[1]
        ny = dy[i]+santa[2]

        in_there_santa = False

        if 0<nx<=N and  0<ny<=N:
            if distance> (nx-Rr)**2 + (ny-Rc)**2: # 거리가 가까워졌다면
                for s in santas: # 탈락여부 안따지나? => 따질 필요가 없는게, 탈락한 산타는 보드 밖에 존재함. 즉, 아래 조건을 비교해서 걸릴 일이 없음.
                    # 상하좌우에 산타가 있다면
                    if (s[1],s[2]) == (nx,ny):
                        in_there_santa=True
                        break
                if in_there_santa == False: # 다음칸에 산타가 없으면
                    # 없다면 리턴(상우하좌 우선순위를 고려해서 작으면 바로 return 하면 틀림.)
                    distance = (nx-Rr)**2 + (ny-Rc)**2
                    next_x = nx
                    next_y = ny
                    dir = i

    return next_x, next_y, dx[dir], dy[dir]

def crash_santa(Rr, Rc, santa):
    if santa[1] == Rr and santa[2] == Rc:
        return True
    return False

# 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
N, M, P, C, D = map(int, input().split())

# 루돌프의 초기 위치 (상하, 좌우)
Rr, Rc = map(int, input().split())

santas = []
santa_score = [0 for _ in range(P+1)]
for _ in range(P):
    # 산타 번호, 산타 초기 위치
    santa, Sr, Sc = map(int, input().split())
    # 산타 번호, 산타 초기 위치, 기절 여부(탈락 여부도), 기절 카운트
    santas.append([santa, Sr, Sc, 0, 0])

# 순서대로 정렬
santas.sort()

for idx in range(1, M+1):

    # P명의 산타가 모두 탈락하면 게임이 종료됩니다.
    if P == 0:
        break

    ### 루돌프 이동 ###
    # 루돌프 이동
    first_santa = near_santas(santas, Rr, Rc) # 거리, x, y, 기절 및 탈락 여부, 산타 배열에서의 인덱스
    # 가장 가까운 산타의 인덱스
    near_santa_index = first_santa[-1]

    ## 산타와 좌표 비교 후 루돌프 이동
    Rr, Rc, move_x, move_y = move_rudolf(first_santa[1], first_santa[2], Rr, Rc) # santa의 x,y 루돌프의 x,y

    # 루돌프 이동 - 산타 충돌 확인
    if crash_rudolf(Rr, Rc, near_santa_index): # 충돌한다면
        # 산타는 밀려나면서 C점을 얻는다.
        santa_score[near_santa_index+1] += C

        # 루돌프와 충돌한 산타는 기절한다.
        santas[near_santa_index][3] = 1 # 기절
        santas[near_santa_index][4] = 0  # 기절 카운트

        # 루돌프가 이동한 방향 * C만큼 밀린다.
        santas[near_santa_index][1] += (C*move_x)
        santas[near_santa_index][2] += (C*move_y)

        # 밀려난 위치에 산타가 있는지 확인한다.(격자 내에 있으면)
        if 0<santas[near_santa_index][1]<=N and 0<santas[near_santa_index][2]<=N:
            fly_santa(near_santa_index, santas, move_x, move_y)


    ### 산타 이동 ###
    for index, santa in enumerate(santas):
        # 산타 기절 여부 판단
        if santa[3] == 0: # 기절하지 않았으면
            # 산타 이동
            santa_next_x, santa_next_y, move_x, move_y = move_santa(santa, Rr, Rc)

            santa[1] = santa_next_x
            santa[2] = santa_next_y

            # 산타 이동시 루돌프와 충돌 발생 여부 체크
            if crash_santa(Rr, Rc, santa):
                # 산타는 이동하려던 방향의 반대로 밀린다.
                santa[1] += (-move_x*D)
                santa[2] += (-move_y*D)

                santa_score[santa[0]] += D

                # 루돌프와 충돌한 산타는 기정
                santa[3], santa[4] = 1,0

                # 충돌 후 날아간 위치에 산타가 있는 경우
                if 0 < santa[1] <= N and 0 < santa[2] <= N:
                    fly_santa(index, santas, -move_x, -move_y)

    # 기절 여부 판단
    for santa in santas:
        if santa[3] == 1: # 기절한 경우
            santa[4] += 1 # 기절한 시간을 늘려준다.

            if santa[4] == 2: # 기절에서 깰 시간이 되면
                santa[3], santa[4] = 0,0 # 초기화

    # 탈락여부 판단
    for santa in santas:
        if not(0<santa[1]<=N and 0<santa[2]<=N) and santa[3] != 2: # 탈락하지 않고, 밖으로 밀려난 산타는 탈락처리한다.
            santa[3] = 2 # 탈락 표시
            P -= 1
            continue

        if santa[3] ==2:
            continue

        # 모든 산타에게 점수를 1점씩 준다.
        santa_score[santa[0]] +=1


print(*santa_score[1:])