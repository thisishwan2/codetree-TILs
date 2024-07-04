def near_santas(santas, Rr, Rc):
    near_santa_list = []
    # 거리 구하기
    for santa in santas:
        # 산타의 y좌표, x좌표, 산타의 충돌여부 및 탈락여부
        santa_y, santa_x, santa_over = santa[1], santa[2], santa[3]

        # 거리 계산하기
        distance = (Rr - santa_y) ** 2 + (Rc - santa_x) ** 2

        # 거리, 산타의 좌표 넣기
        near_santa_list.append([distance, santa_y, santa_x, santa_over])
    
    # 거리, y좌표, x좌표 순으로 정렬하기
    near_santa_list.sort(key=lambda x:(x[0], -x[1], -x[2]))

    for ns in near_santa_list:
        # 게임에서 탈락한 산타가 아닐 경우 가장 가까운 산타 리턴
        if ns[3] != 2:
            return ns

# 산타와 좌표 비교 후 루돌프 이동하기
def coordinate_compare_with_rudolf(Sr, Sc, Rr, Rc):
    # 산타가 더 아래에 있음
    if Sr - Rr > 0:
        # 산타가 더 오른쪽에 있음
        if Sc - Rc > 0:
            return [1, 1]
        elif Sc - Rc == 0:
            return [1, 0]
        else:
            return [1, -1]
    # 산타와 y축이 동일함
    elif Sr - Rr == 0:
        if Sc - Rc > 0:
            return [0, 1]
        elif Sc - Rc == 0:
            return [0, 0]
        else:
            return [0, -1]
    # 산타가 더 위에 있음
    else:
        if Sc - Rc > 0:
            return [-1, 1]
        elif Sc - Rc == 0:
            return [-1, 0]
        else:
            return [-1, -1]

def coordinate_compare_with_santa(santa, santas, Rr, Rc, N):
    # 산타의 이동은 상우하좌 우선순위에 맞춰서 이동해야 함
    Sr, Sc = santa[1], santa[2]
    santa_move = []
    prev_distance = (Sr - Rr) ** 2 + (Sc - Rc) ** 2
    # 산타가 더 아래에 있음
    if Sr - Rr > 0:
        # 산타가 더 오른쪽에 있음
        if Sc - Rc >= 0:
            if not is_next_santa(santa, santas, -1, 0, N):
                # 산타 위로 이동
                distance = (Sr - Rr - 1) ** 2 + (Sc - Rc) ** 2
                if distance < prev_distance:
                    santa_move.append([0, distance, -1, 0])
            if not is_next_santa(santa, santas, 0, -1, N):
                # 산타 왼쪽으로 이동
                distance = (Sr - Rr) ** 2 + (Sc - Rc - 1) ** 2
                if distance < prev_distance:
                    santa_move.append([3, distance, 0, -1])
        # 산타가 더 왼쪽에 있음
        else:
            if not is_next_santa(santa, santas, -1, 0, N):
                # 산타 위로 이동
                distance = (Sr - Rr - 1) ** 2 + (Sc - Rc) ** 2
                if distance < prev_distance:
                    santa_move.append([0, distance, -1, 0])
            if not is_next_santa(santa, santas, 0, 1, N):
                distance = (Sr - Rr) ** 2 + (Sc - Rc + 1) ** 2
                if distance < prev_distance:
                    santa_move.append([1, distance, 0, 1])
    elif Sr - Rr == 0:
        if Sc - Rc >= 0:
            if not is_next_santa(santa, santas, 0, -1, N):
                distance = (Sr - Rr) ** 2 + (Sc - Rc - 1) ** 2
                if distance < prev_distance:
                    santa_move.append([3, distance, 0, -1])
        else:
            if not is_next_santa(santa, santas, 0, 1, N):
                distance = (Sr - Rr) ** 2 + (Sc - Rc + 1) ** 2
                if distance < prev_distance:
                    santa_move.append([1, distance, 0, 1])    
    # 산타가 더 위에 있을 때
    else:
        # 산타가 더 오른쪽에 있음
        if Sc - Rc >= 0:
            if not is_next_santa(santa, santas, 1, 0, N):
                # 산타 위로 이동
                distance = (Sr - Rr + 1) ** 2 + (Sc - Rc) ** 2
                if distance < prev_distance:
                    santa_move.append([2, distance, 1, 0])
            if not is_next_santa(santa, santas, 0, -1, N):
                # 산타 왼쪽으로 이동
                distance = (Sr - Rr) ** 2 + (Sc - Rc - 1) ** 2
                if distance < prev_distance:
                    santa_move.append([3, distance, 0, -1])
        # 산타가 더 왼쪽에 있음
        else:
            if not is_next_santa(santa, santas, 1, 0, N):
                # 산타 위로 이동
                distance = (Sr - Rr + 1) ** 2 + (Sc - Rc) ** 2
                if distance < prev_distance:
                    santa_move.append([2, distance, 1, 0])
            if not is_next_santa(santa, santas, 0, 1, N):
                distance = (Sr - Rr) ** 2 + (Sc - Rc + 1) ** 2
                if distance < prev_distance:
                    santa_move.append([1, distance, 0, 1])
    # 우선순위에 맞게 정렬
    santa_move.sort(key = lambda x:(x[1], x[0]))

    if len(santa_move):
        return [santa_move[0][2], santa_move[0][3]]
    return [0, 0]
# 상하좌우 산타 존재여부 체크
def is_next_santa(santa, santas, next_y, next_x, N):
    santa_number, santa_y, santa_x = santa[0], santa[1], santa[2]

    if move(santa_y, santa_x, next_y, next_x, N):
        for s in santas:
            if s[0] != santa_number and s[1] == (santa_y+next_y) and s[2] == (santa_x+next_x):
                return True
    return False
    

# 이동
def move(Rr, Rc, next_y, next_x, N):
    if 0 < Rr + next_y <= N and 0 < Rc + next_x <= N:
        return True
    return False

# 루돌프 이동 - 산타 충돌
def crash_rudolf(Rr, Rc, santas):
    for santa in santas:
        if santa[1] == Rr and santa[2] == Rc:
            return [True, santa]
    return [False, santa]

def crash_santa(Rr, Rc, santa):
    if santa[1] == Rr and santa[2] == Rc:
        return True
    return False

def fly_santa(santa, santas, next_y, next_x):
    for s in santas:
        if s[0] != santa[0] and santa[1] == s[1] and santa[2] == s[2]:
            s[1] += next_y
            s[2] += next_x
            ## 다음 산타도 한칸 옆으로 이동
            fly_santa(s, santas, next_y, next_x)

# 게임판 크기, 게임 턴 수, 산타 수, 루돌프 힘, 산타 힘
N, M, P, C, D = map(int, input().split())

# 루돌프의 초기 위치 (상하, 좌우)
Rr, Rc = map(int, input().split())

santas = []

santa_score = [0 for _ in range(P+1)]

for _ in range(P):
    # 산타 번호, 산타 초기 위치
    santa, Sr, Sc = map(int, input().split())
    # 산타 번호, 산타 초기 위치, 기절 여부, 기절 카운트
    santas.append([santa, Sr, Sc, 0, 0])

# 순서대로 정렬
santas.sort()

for idx in range(1, M+1):
    # 전부 탈락했을 경우 게임 종료
    if P == 0:
        break
    # 루돌프 이동
    
    ## 가장 가까운 산타 구하기
    first_santa = near_santas(santas, Rr, Rc)

    ## 산타와 좌표 비교 후 루돌프 이동하기
    next_y, next_x = coordinate_compare_with_rudolf(first_santa[1], first_santa[2], Rr, Rc)
    
    ## 루돌프가 이동가능한 위치일 경우
    if move(Rr, Rc, next_y, next_x, N):
        ## 루돌프 이동하기
        Rr += next_y
        Rc += next_x

        ## 현 루돌프 위치와 산타 위치 비교
        cr = crash_rudolf(Rr, Rc, santas)

        if cr[0]:
            ## 충돌 발생 시 산타 밀려나면서 C만큼 점수를 얻음
            cs = cr[1]
            santa_score[cs[0]] += C

            ## 루돌프와 충돌한 산타는 기절하게 됨
            cs[3], cs[4] = 1, 0

            ## 그리고 루돌프가 이동한 방향 * C 만큼 밀려남
            cs[1] += (C * next_y)
            cs[2] += (C * next_x)

            ## 착지한 위치에 산타가 있는지 체크
            fly_santa(cs, santas, next_y, next_x)
            
    # 산타 이동
    for santa in santas:
        ## 산타 기절 여부 및 게임 종료 여부 체크
        if santa[3] == 0:
            ## 현 위치에서 상하좌우 산타가 있는지 확인하기
            santa_next_y, santa_next_x = coordinate_compare_with_santa(santa, santas, Rr, Rc, N)

            santa[1] += santa_next_y
            santa[2] += santa_next_x

            ## 산타 이동 시 충돌 발생 여부 체크하기
            if crash_santa(Rr, Rc, santa):
                santa[1] += (-santa_next_y * D)
                santa[2] += (-santa_next_x * D)

                santa_score[santa[0]] += D

                ## 루돌프와 충돌한 산타는 기절하게 됨
                santa[3], santa[4] = 1, 0

                ## 충돌 후 날아간 위치에 산타가 있을 경우
                fly_santa(santa, santas, -santa_next_y, -santa_next_x)
    
    ## 기절 여부 판단
    for santa in santas:
        if santa[3] == 1:
            santa[4] += 1

            if santa[4] == 2:
                santa[3], santa[4] = 0, 0
    
    ## 탈락 여부 판단
    for santa in santas:
        if not move(santa[1], santa[2], 0, 0, N) and santa[3] != 2:
            santa[3] = 2
            P -= 1
            continue

        if santa[3] == 2:
            continue
        santa_score[santa[0]] += 1

#    print(f"산타 점수 : {santa_score}")
#    print(f"산타 위치 : {santas}")
#    print(f"루돌프 위치 : {Rr}, {Rc}")


print(*santa_score[1:])