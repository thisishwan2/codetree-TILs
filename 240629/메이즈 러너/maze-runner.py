def move_people():
    global move

    # 상하좌우
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    del_position=[]

    # 모든 참가자는 한칸씩 움직인다.
    for idx, i in enumerate(position):
        x1 = i[0]
        y1 = i[1]

        distance = abs(x1-exit_x) + abs(y1-exit_y)

        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]

            # 움직일 수 있는 지 확인
            if 0<=nx<n and 0<=ny<n:
                if (nx,ny)==(exit_x, exit_y): #출구인 경우
                    move+=1 # 이동한 거리 더하기
                    del_position.append(idx) # 삭제할 인덱스를 다른곳에 담아두기
                    break

                elif miro[nx][ny]==0: #빈칸인 경우
                    # 출구와 가까워 지는 지 확인
                    if distance>abs(nx-exit_x) + abs(ny-exit_y):
                        # 이동한다
                        position[idx] = [nx,ny]
                        move+=1 # 이동한 거리 더하기
                        break

    for i in del_position:
        position.pop(i)

# 출구와 참가자를 포함하는 가장 작은 정사각형 찾기
def find_sqr():
    for k in range(1,n+1):
        for x1 in range(n):
            for y1 in range(n):
                x2 = x1+k
                y2 = y1+k

                if not (x1<= exit_x <=x2 and y1<= exit_y <=y2):
                    continue

                is_people = False
                for i in position:
                    if x1<= i[0] <=x2 and y1<= i[1] <=y2: # 사각형 안에 사람이 있다면
                        is_people=True

                if is_people:
                    return x1,y1,k

def turn():
    global exit_x, exit_y

    x1,y1,k = find_sqr()

    # 기존 미로를 새로운 k+1*k+1 배열로 옮긴다.
    extract_miso = [[0 for _ in range(k+1)]for _ in range(k+1)]

    for i in range(k+1):
        for j in range(k+1):
            extract_miso[i][j] = miro[i+x1][j+y1]

    # 90도 회전한다.
    new_arr = [[0 for _ in range(k+1)]for _ in range(k+1)]
    for i in range(k+1):
        for j in range(k+1):
            new_arr[j][k-i] = extract_miso[i][j]

    # 사람 좌표도 바꿔줘야함.
    for idx, val in enumerate(position):
        x = val[0]
        y = val[1]

        if x1<=x<=x1+k and y1<=y<=y1+k:
            nx, ny = x-x1, y-y1
            nnx, nny = ny, k-nx
            position[idx] = [nnx+x1, nny+y1]

    # 출구 좌표 새로운 배열에 맞게 변화
    n_exit_x, n_exit_y = exit_x-x1, exit_y-y1
    exit_x, exit_y = n_exit_y + x1, k-n_exit_x+y1

    # 내구도 감소
    for i in range(k+1):
        for j in range(k+1):
            if new_arr[i][j]>=1:
                new_arr[i][j]-=1

    # 원래 배열에 붙혀넣는다.
    for i in range(k+1):
        for j in range(k+1):
            miro[x1+i][y1+j] = new_arr[i][j]


n,m,k = map(int, input().split()) # 미로의 크기, 참가자 수, 게임 시간

miro = []
for _ in range(n):
    miro.append(list(map(int, input().split())))

position = []
for i in range(m):
    tmp = list(map(int, input().split()))
    n_tmp = [tmp[0]-1, tmp[1]-1]
    position.append(n_tmp)

e_x, e_y = map(int, input().split())

# 출구 좌표
exit_x=e_x-1
exit_y=e_y-1
move = 0 # 모든 참가자들의 이동거리

for i in range(k):

    # 참가자 이동
    move_people()

    # 모든 참가자 탈출 확인
    if len(position) == 0:
        break

    # 회전
    turn()

print(move)
print(exit_x+1, exit_y+1)