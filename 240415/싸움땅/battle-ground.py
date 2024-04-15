def im_moving(x,y,nx,ny,player_num,d,s,gun): # 내가 이동

    # 우선 다음칸 격자에 내가 가진 총을 내려놓는다.
    if gun !=0:
        gun_arr[nx][ny].append(gun)
        gun=0

    # nx,ny에서 내가 원래 보유한 방향으로 움직인다.
    nnx,nny = nx+dx[d],ny+dy[d]


    # 빈칸의 정의가 총이 없는 고싱 아님
    # 만약 이동할 곳이 격자 밖이거나 플레이어가 있으면 오른쪽으로 90도씩 회전하여 보이는 빈칸에 이동
    if (not (0<=nnx<n and 0<=nny<n)) or player_arr[nnx][nny]!=0:
            for i in range(1,5):
                d+=1
                if d > 3:
                    d -= 4
                nnx, nny = nx + dx[d], ny + dy[d]

                if (0<=nnx<n and 0<=nny<n):
                    if player_arr[nnx][nny]==0: # 빈칸을 발견했다면
                        if gun_arr[nnx][nny]!=[]: # 총이 있다면
                            # 칸에서 젤 큰값의 총을 가짐
                            gun = max(gun_arr[nnx][nny])
                            gun_arr[nnx][nny].remove(gun)
                        break
    # 이동할 곳이 그냥 빈칸이면
    else:
        if gun_arr[nnx][nny] != []:  # 총이 있다면
            # 칸에서 젤 큰값의 총을 가짐
            gun = max(gun_arr[nnx][nny])
            gun_arr[nnx][nny].remove(gun)

    # 해당 칸으로 이동
    player_arr[nnx][nny] = [player_num, d, s, gun]
    player_arr[x][y] = 0
    player_dict[player_num] = [nnx, nny]


def next_player_moving(x,y,nx,ny,player_num, d,s,gun): # 나는 nx,ny로 가고, 먼저 온놈을 옮김
    next_player_num, next_player_d, next_player_s, next_player_gun = player_arr[nx][ny]

    # 현재 플레이어 다음 칸으로 이동

    # 우선 진 놈은 총을 현재 격자에 내려 놓는다.
    if next_player_gun!=0:
        gun_arr[nx][ny].append(next_player_gun)
        next_player_gun=0

    # 땅에 총이 있으면
    if gun_arr[nx][ny]!=[]:
        tmp = gun
        gun = max(gun_arr[nx][ny])
        gun_arr[nx][ny].remove(gun)
        gun_arr[nx][ny].append(tmp)

    # 현재 플레이어는 이동과 총을 교체하는 것 까지 끝
    player_arr[nx][ny] = [player_num, d, s, gun]
    player_arr[x][y]=0
    player_dict[player_num] = [nx,ny]

    # 이제 이미 온 놈을 이동시킨다.
    # nx,ny에서 내가 원래 보유한 방향으로 움직인다.
    nnx, nny = nx + dx[next_player_d], ny + dy[next_player_d]

    # 만약 이동할 곳이 격자 밖이거나 플레이어가 있으면 오른쪽으로 90도씩 회전하여 보이는 빈칸에 이동
    if (not (0 <= nnx < n and 0 <= nny < n)) or player_arr[nnx][nny] != 0:
        for i in range(1, 5):
            next_player_d += 1
            if next_player_d > 3:
                next_player_d -= 4
            nnx, nny = nx + dx[next_player_d], ny + dy[next_player_d]

            if (0 <= nnx < n and 0 <= nny < n):
                if player_arr[nnx][nny] == 0:  # 빈칸을 발견했다면
                    if gun_arr[nnx][nny] != []:  # 총이 있다면
                        # 칸에서 젤 큰값의 총을 가짐
                        next_player_gun = max(gun_arr[nnx][nny])
                        gun_arr[nnx][nny].remove(next_player_gun)
                    break
    # 이동할 곳이 그냥 빈칸이면
    else:
        if gun_arr[nnx][nny] != []:  # 총이 있다면
            # 칸에서 젤 큰값의 총을 가짐
            next_player_gun = max(gun_arr[nnx][nny])
            gun_arr[nnx][nny].remove(next_player_gun)

    # 이미온놈 플레이어는 이동과 총을 교체하는 것 까지 끝
    player_arr[nnx][nny] = [next_player_num, next_player_d, next_player_s, next_player_gun]
    player_dict[next_player_num] = [nnx, nny]


dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m,k = map(int, input().split()) # n: 격자 크기, m: 플레이어 수, k: 라운드 수
gun_arr = [] # 격자에 놓인 총
for i in range(n):
    tmp=list(map(int, input().split()))
    tmp2 = []
    for j in tmp:
        if j==0:
            tmp2.append([])
        else:
            tmp2.append([j])
    gun_arr.append(tmp2)

player_arr=[[0 for _ in range(n)]for _ in range(n)] # 플레이어 등의 위치와 정보가 담긴 배열
player_dict={}
for i in range(1, m+1):
    x,y,d,s = map(int, input().split())
    player_arr[x-1][y-1] = [i, d, s, 0] # 방향, 초기 능력치, 총 공격력
    player_dict[i] = [x-1,y-1]
# 플레이어 번호는 1번 부터 시작
score = [0]*(m+1)

# print(*player_arr, sep = '\n')
# print(*gun_arr, sep = '\n')
# print(player_dict)

for _ in range(k): # k 라운드 반복
    for i in range(1,m+1):
        # i번 플레이어 정보 뽑기
        x,y = player_dict[i]
        player_num, d, s, gun = player_arr[x][y]

        # 1-1. 이동할 다음 좌표 구하기
        nx=x+dx[d]
        ny=y+dy[d]

        if 0<=nx<n and 0<=ny<n:
            pass
        else:
            d += 2
            if d > 3:
                d -= 4

            nx = x + dx[d]
            ny = y + dy[d]

        # 2-1
        if player_arr[nx][ny]==0: # 다음 칸에 플레이어가 없고
            if gun_arr[nx][ny]!=[]: # 다음 칸에 총이 있으면
                # 내가 총을 가지고 있으면 더 강한 총으로 바꾼다.
                if gun!=0:
                    if gun < max(gun_arr[nx][ny]):
                        tmp=gun
                        gun = max(gun_arr[nx][ny])
                        gun_arr[nx][ny].remove(gun)
                        gun_arr[nx][ny].append(tmp)
                # 내가 총이 없으면 그냥 총을 주운다.
                else:
                    gun = max(gun_arr[nx][ny])
                    gun_arr[nx][ny].remove(gun)

            # 플레이어를 이동시키고, dict과 arr를 업데이트 해준다.
            player_arr[nx][ny]= [player_num, d, s, gun]
            player_arr[x][y] = 0
            player_dict[player_num] = [nx, ny]
            continue

        # 2-2-1. 다음 칸에 플레이어가 있는 경우
        elif player_arr[nx][ny]!=0: # 다음 칸에 플레이어가 있다면 두 플레이어가 싸운다.
            next_player_point = player_arr[nx][ny][2]+player_arr[nx][ny][3] # 다음 칸 유저의 점수
            now_player_point = player_arr[x][y][2] + player_arr[x][y][3] # 현재 내 점수
            point_res = abs(next_player_point-now_player_point) # 점수 차이

            # 점수 차이가 같다면, 초기 능력치를 비교한다.
            if point_res == 0:
                # 먼저 온 유저의 초기 능력치가 더 큰 경우
                if player_arr[nx][ny][2] > player_arr[x][y][2]:
                    # 내가 이동
                    im_moving(x,y,nx, ny, player_num, d, s, gun)

                    # 이긴놈이 떨어져있는 총중에 젤 쎈거랑 바꿈
                    if gun_arr[nx][ny]!=[]:
                        tmp = player_arr[nx][ny][3]
                        player_arr[nx][ny][3] = max(gun_arr[nx][ny])
                        gun_arr[nx][ny].remove(max(gun_arr[nx][ny]))
                        gun_arr[nx][ny].append(tmp)

                # 나의 초기 능력치가 더 큰 경우
                else:
                    # 먼저 온 유저가 이동하고, 난 nx,ny 자리로 이동
                    next_player_moving(x, y, nx, ny, player_num, d, s, gun)

            # 점수 차이가 다르면
            else:
                # 먼저 온 유저의 포인트가 더 큰 경우
                if next_player_point > now_player_point:
                    # 내가 이동
                    im_moving(x,y,nx, ny, i, d, s, gun)

                    # 이긴놈이 떨어져있는 총중에 젤 쎈거랑 바꿈
                    if gun_arr[nx][ny]!=[]:
                        tmp = player_arr[nx][ny][3]
                        player_arr[nx][ny][3] = max(gun_arr[nx][ny])
                        gun_arr[nx][ny].remove(max(gun_arr[nx][ny]))
                        gun_arr[nx][ny].append(tmp)

                    # 포인트 획득
                    score[player_arr[nx][ny][0]]+=point_res

                # 내가 더 큰 경우
                else:
                    # 먼저 온 유저가 이동하고, 난 nx,ny 자리로 이동
                    next_player_moving(x, y, nx, ny, player_num, d, s, gun)
                    # 포인트 획득
                    score[player_num]+=point_res

    # print("==========" + str(k) + "==========")
    # print(*player_arr, sep='\n')
    # print(*gun_arr, sep='\n')
    # print(player_dict)

print(*score[1:])