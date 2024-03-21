def go_out(arr):
    available = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]!=0:
                if arr[i][j][1]==k:
                    available+=1

    if available == 1:
        return True
    else:
        return False



def minus(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j]!=0:
                player_num = arr[i][j][0]
                registration = arr[i][j][1]

                if registration-1 == 0: # 독점 계약이 0이 되면 배열은 빈칸이 됨
                    arr[i][j]=0
                else:
                    arr[i][j]=[player_num, registration-1] # 기존 독점 계약수에 -1


# 현재 위치에 인접한 칸에 빈칸이 있는 지 확인
def check(arr, x, y):
    available = 0
    for i in range(1, 5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny]==0 or arr[nx][ny][1]==k+1: # 인전한 칸이 빈칸이거나 해당 턴에 누가 온 경우
                available += 1

    if available > 0:
        return True
    else:
        return False


# 다른 유저와 충돌하는 경우 해당 위치에 숫자가 더 작은 유저를 넣어놓는다.
def conflict_usr(arr, black_list, nx,ny, player_num, direction):
    if arr[nx][ny][0] > player_num:  # 먼저 도착한 유저가 현재 유저보다 번호가 높으면 => 먼저 도착한 유저를 없앤다.
        black_list.append(arr[nx][ny][0])  # 블랙리스트 처리
        arr[nx][ny] = [player_num, k+1]  # 해당 위치를 더 작은 유저로 변경
        q.append([nx, ny, player_num, direction])
    else:
        black_list.append(player_num)  # 블랙리스트 처리



from collections import deque

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())  # n=격자의 크기(정사각형), m=플레이어의 수, k=독점 계약 턴수
arr = []  # 격자
for i in range(n):
    arr.append(list(map(int, input().split())))

# 초기 방향 (1(상), 2(하), 3(좌), 4(우))
init_direction = list(map(int, input().split()))

q = deque()

# arr에 정보 기입
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            player_num = arr[i][j] # player 번호
            arr[i][j] = [player_num, k] # player 번호, 독점 계약 수
            q.append([i, j, player_num, init_direction[player_num - 1]]) # x,y, player 번호, 방향

direction_dic = {}
# 플레이어의 방향에 따른 이동 우선순위 위,아래,왼쪽, 오른쪽 향할때 우선순위가 각줄로 들어옴
for i in range(1, m + 1):
    tmp = {}
    for j in range(1, 5):
        tmp[j] = list(map(int, input().split()))
    direction_dic[i] = tmp

# print(arr)
# print(direction_dic)


ans = 0
black_list = [] # 탈락 유저 num을 기록

while ans < 1000:
    # 먼저 쳐다보는 방향으로 이동을 하기 위해 다음칸을 확인함. 만약 아무도 독점하지 않은 땅이다? 그럼 이동
    # 만약 쳐다보는 방향에 누가 독점을 했다? 쳐다보는 방향의 우선순위에 따라서 가장 처음 빈칸이 나오는 곳으로 이동(이때 자신 땅으로는 이동 x 자신 땅 이동은 아에 없는 경우)
    # 만약 다 막혀있다?? 그럼 내가 방금 왔던 내 독점 땅으로 이동한다.
    # 이전의 땅들은 독점 계약 수를 -1해주고, 현재 위치는 k 로 넣어준다.
    # 만약 두명이 같은 땅을 접근하려고 한다? 그럼 숫자 작은 놈이 이기고, 숫자 큰 플레이어는 탈락

    # 탈출 조건 재정의
    if go_out(arr):
        print(ans)
        exit()

    # q의 길이만큼 수행
    for i in range(len(q)):
        x, y, player_num, direction = q.popleft() # x,y, player 번호, 방향

        # 이미 탈락한 유저의 q면 통과
        if player_num in black_list:
            continue

        usr_dir = direction_dic.get(player_num)  # 해당 유저가 보유한 dir 목록 (ex: {1: [1, 2, 3, 4], 2: [2, 1, 3, 4], 3: [1, 3, 4, 2], 4: [4, 3, 2, 1]})
        now_dir_candidate = usr_dir.get(direction)  # dir 목록중 현재 바라보고 있는 방향의 dir 목록 조회. (ex: [1, 2, 3, 4])

        # 현재 위치에 인접한 칸에 빈칸이 있는 지 확인
        check_res = check(arr, x, y)

        # 인전한 칸이 존재하는 경우
        if check_res:
            for j in now_dir_candidate:  # 4가지 방향에 대해 우선순위에 따른 인접한 칸을 찾음
                nx = x + dx[j]
                ny = y + dy[j]

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == 0:  # 다음 공간이 빈공간이면 이동
                        q.append([nx, ny, player_num, j])
                        arr[nx][ny] = [player_num, k+1] # 일부러 새로 간 빈칸에 독점계약수를 k+1로 함. 왜냐면 마지막에 전체 탐색하면서 -1을 할것임
                        break

                    elif arr[nx][ny][1] == k+1: # 현재 턴에 다른 유저도 해당 위치가 가장 큰 우선순위라 온 경우
                        conflict_usr(arr, black_list, nx, ny, player_num, j)
                        break

        else:  # 인접한 칸이 없는 경우

            # 다른 유저와 겹치는 경우
            for j in now_dir_candidate: # 4가지 방향에 대해 탐색하면서 다른 유저와 겹치는 지 확인
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny][1] == k+1: # 이전에 이 위치로 온 유저가 있다면, 둘 중 player num이 큰놈을 없애야함
                        conflict_usr(arr, black_list, nx,ny, player_num, j)
                        break

                    # 내가 왔던 이전 칸이면
                    elif arr[nx][ny][0] == player_num and arr[nx][ny][1]==k-1:
                        # 다시 돌아가기
                        q.append([nx, ny, player_num, j])
                        arr[nx][ny] = [player_num, k + 1]
                        break

    # 이제 배열 전체를 탐색하면서 독점계약수가 0이 아닌 곳은 -1을 해준다.
    minus(arr)
    ans += 1

if ans>1000 or len(black_list)!=m-1:
    print(-1)
else:
    print(ans)