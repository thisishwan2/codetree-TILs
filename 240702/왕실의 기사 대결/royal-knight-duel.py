from collections import deque

def move(num, d):
    global player_arr, player, moving_list
    new_arr = [[0 for _ in range(l)]for _ in range(l)]
    q=deque()
    move_ok = True

    coordinate, heart = player[num]

    for x,y in coordinate:
        q.append([x,y,d,num])

    while q:
        x,y,d,num = q.popleft()

        nx,ny = x+dx[d], y+dy[d]

        # 다음 이동하는 칸이 범위 밖이면 이동하지 않는다.
        if not 0<=nx<l and 0<=ny<l:
            move_ok = False
            break

        # 다음 이동하는 칸이 벽인 경우에는 이동하지 않는다.
        if chess[nx][ny] == 2:
            move_ok = False
            break

        # 다음 이동하는 칸이 같은 기사의 칸이거나 기사가 없으면 그냥 이동한다.
        if player_arr[nx][ny] == num or player_arr[nx][ny] == 0:
            new_arr[nx][ny] = num

        # 다른 기사가 있으면, 다른 기사의 좌표도 q에 넣고, 이동한다.
        elif player_arr[nx][ny] != num:
            new_arr[nx][ny] = num

            # 처음으로 다른 기사 좌표를 만난게 아니면, 아래 로직은 수행하지 않는다.
            if player_arr[nx][ny] not in moving_list:
                moving_list.append(player_arr[nx][ny])
                coordinate, heart = player[player_arr[nx][ny]]
                for x,y in coordinate:
                    q.append([x,y,d,player_arr[nx][ny]])

    # 기사 이동이 정상적으로 이루어졌으면, player와 player_arr를 업데이트 해준다.
    if move_ok:

        # 이동 안한 기사에 대해 new_arr에 반영해줘야 한다.
        for num in player.keys():
            if num not in moving_list:
                coordinate, heart = player[num]
                for x, y in coordinate:
                    new_arr[x][y] = num

        player_arr = new_arr

        # 기존의 딕셔너리의 기사 좌표를 지움
        for i in player.keys():
            player[i][0] = []

        # 딕셔너리에 각 기사의 좌표 최신화
        for i in range(l):
            for j in range(l):
                if player_arr[i][j] !=0:
                    num = player_arr[i][j]
                    player[num][0].append([i,j])
        return True
    # 기사 이동에 문제가 있으면 이동하지 않는다.
    else:
        return False


def fight_damage(num):

    # num 기사는 데미지를 받지 않는다.
    for key in list(player.keys()):
        if key!=num and key in moving_list: # num 기사가 아니고(움직임 시작 기사), 움직인 기사인 경우
            coordinate, heart = player[key]
            for x,y in coordinate:
                if chess[x][y]==1 and heart>0: # 함정에 위치하고, 피가 0보다 큰 경우
                    heart-=1

            # 변경된 heart를 딕셔너리에 저장
            player[key][1] = heart

            # heart가 0이 되면, 배열과 딕셔너리에서 제외시킨다.
            if heart==0:
                for x, y in coordinate:
                    player_arr[x][y] = 0
                del player[key]


dx = [-1,0,1,0]
dy = [0,1,0,-1]

l, n, q = map(int, input().split())  # 체스판 크기, 기사의 수, 명령의 수

chess = []
for i in range(l):
    chess.append(list(map(int, input().split()))) # 0 빈칸, 1 함정, 2 벽

player = {}
player_arr = [[0 for _ in range(l)]for _ in range(l)]
player_heart = {}
for num in range(1,n+1):
    r,c,h,w,k = map(int, input().split())

    player_coordinate = []
    for i in range(r-1, r-1+h):
        for j in range(c-1, c-1+w):
            player_coordinate.append([i,j])
            player_arr[i][j]=num

    player[num] = [player_coordinate, k]
    player_heart[num] = k

for _ in range(q):
    i,d = map(int, input().split())

    moving_list = [i]  # 이동한 기사를 담는 리스트

    # 기사 이동
    if i in player.keys():
        if move(i,d):
            # 대결 데미지 확인
            fight_damage(i)
    # 이동하지 않으면 pass
    else:
        pass

# 처음 주어진 체력과 생존한 기사들의 체력만 비교해서 정답 추출
answer= 0
for key in player.keys():
    coordinate, heart = player[key]
    origin_heart = player_heart[key]
    answer+=(origin_heart-heart)

print(answer)