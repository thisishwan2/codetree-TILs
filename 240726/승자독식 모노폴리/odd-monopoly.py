# 승자독식 모노폴리

# 아무도 독점 계약 맺지 않은 칸으로 이동, 없으면, 4방향중 본인이 독점한 당으로 이동
# 이때, 우선순위에 따라 움직일 칸을 결정함.
# 플레이어가 바라보는 방향은 직전에 이동한 방향
# 한칸에 여러 플레이어가 있으면 가장 작은 번호를 가진 플레이어만 살아남는다.

# 중요한건, 본인이 독점계약한 땅과 유효한 턴의 수를 인지해야함

# 1:위, 2:아래, 3:왼쪽, 4:오른쪽
d = {1:[-1,0], 2:[1,0], 3:[0,-1], 4:[0,1]}

# 이동하는 함수
def move():
    for num in player_info.keys():
        x,y,dir = player_info[num][0],player_info[num][1],player_info[num][2]
        for direction in directions[num][dir]:
            nx = x+d[direction][0]
            ny = y+d[direction][1]

            # 이동 여부를 확인하는 flag
            move_flag = False

            # 범위 안이고,
            if 0<=nx<n and 0<=ny<n:
                # 독점하지 않은 위치라면
                if area[nx][ny] == []:
                    player_info[num] = [nx,ny,direction]
                    move_flag = True
                    break

        # 이동하지 못했다면,
        if move_flag == False:
            for direction in directions[num][dir]:
                nx = x + d[direction][0]
                ny = y + d[direction][1]
                # 범위 안이고,
                if 0 <= nx < n and 0 <= ny < n:
                    # 자신이 독점한 곳이면 이동
                    if area[nx][ny][0] == num:
                        player_info[num] = [nx, ny, direction]
                        break

def minus():
    # 기존의 칸들에 대해 계약 턴 수를 -1한다.
    for i in range(n):
        for j in range(n):
            if area[i][j] != []:
                if area[i][j][1] - 1 == 0:  # 남은 계약 수-1이 0이면 그 칸은 계약해제
                    area[i][j] = []
                else:
                    area[i][j] = [area[i][j][0], area[i][j][1] - 1]

def contract():
    minus()
    # 새로운 칸들에 대해 계약을 수행한다.
    for num in player_info.keys():
        x, y, dir = player_info[num][0], player_info[num][1], player_info[num][2]
        # 플레이어가 반대방향으로 이동해서 본인이 계약한 칸으로 되돌아 간경우면, 계약 수만 최신화
        if area[x][y] != [] and area[x][y][0] == num:
            area[x][y][1] = k
        else:
            area[x][y].append(num)
            area[x][y].append(k)

    # 만약 area에서 [] 내부의 크기가 2보다 큰 칸이 있으면 크 칸은 플레이어가 겹친 곳이므로 처리한다.
    for i in range(n):
        for j in range(n):
            if len(area[i][j])>2: # 플레이어가 겹침
                #0,2,4,... 인덱스만 뽑아서 제일 작은 값의 인덱스를 구한다.
                min_num, min_num_idx = find_min_num(area[i][j])
                delete_num = []
                for _ in range(0,len(area[i][j]),2):
                    if min_num != area[i][j][_]:
                        delete_num.append(area[i][j][_])

                area[i][j] = [min_num, k]

                # player_info에서 delete_num에 해당하는 플레이어 삭제
                for del_num in delete_num:
                    del player_info[del_num]

def find_min_num(arr):
    min_num = 1e9
    min_num_idx=0
    for i in range(0,len(arr),2):
        if min_num>arr[i]:
            min_num = arr[i]
            min_num_idx = i
    return min_num, min_num_idx



# n: 격자의 크기, m: 플레이어의 수, k: 독점 계약 턴수
n,m,k = map(int, input().split())

# 격자의 정보
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 플레이어 정보(위치, 방향)
player_info = {}
# 독점 정보
area = [[[]for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j]!=0:
            player_info[board[i][j]] = [i,j]
            area[i][j] = [board[i][j], k] # 플레이어 번호, 남은 턴수

# 각 플레이어의 초기 방향 추가
direc = list(map(int, input().split()))
for idx, val in enumerate(direc):
    player_info[idx+1].append(val)

# 방향에 따르 우선순위
directions = {}
for i in range(1,m+1):
    tmp = {}
    for j in range(1, 5):
        tmp[j] = list(map(int, input().split()))

    directions[i] = tmp
# print(player_info)
# print(area)
# print(priority_for_direction)

turn = 0
# turn이 1000 이상이면 -1 출력
while turn<1000:
    turn+=1

    # 이동
    move()

    # 독점 계약 처리 및 겹치는 플레이어 처리
    contract()

    # 남은 플레이어 확인(1만 남았다면 break, 1은 가장 작은 번호 이기 때문에 무조건 살아남음)
    if len(player_info) == 1:
        break

if turn==1000:
    print(-1)
else:
    print(turn)

'''

4 2 4
0 0 0 2 
0 0 1 0 
0 0 0 0 
0 0 0 0 
2 3 
2 3 4 1 
3 4 2 1 
2 3 4 1 
1 2 3 4 
1 4 3 2 
2 3 1 4 
1 3 4 2 
1 2 3 4

'''