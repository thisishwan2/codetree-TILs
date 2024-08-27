# from collections import deque

# def bfs(i,j,g_num):
#     q=deque()
#     q.append((i,j))
#     visited[i][j]=1
#     graph_group[i][j] = g_num

#     while q:
#         x,y =q.popleft()

#         # 머리면
#         if graph[x][y]==1:
#             dic_head[g_num] = [x,y]

#         # 꼬리면
#         elif graph[x][y]==3:
#             dic_tail[g_num] = [x,y]

#         for d in range(4):
#             nx=x+dx[d]
#             ny=y+dy[d]

#             if 0<=nx<n and 0<=ny<n:
#                 if visited[nx][ny]==0:
#                     if graph[nx][ny]!=0:
#                         q.append((nx,ny))
#                         visited[nx][ny]=1
#                         graph_group[nx][ny]=g_num

# def find_body(num):
#     x,y = dic_head[num] # 헤드의 좌표

#     body_list=[] # 헤드를 시작점으로 하여 순차적을 바디값들을 넣음
#     while 1:
#         body_flag = False # body 위치인지를 식별하는 flag
#         for d in range(4):
#             nx=x+dx[d]
#             ny=y+dy[d]

#             if 0<=nx<n and 0<=ny<n:
#                 if graph_group[nx][ny]==num: # 같은 그룹의 좌표인지 확인
#                     if graph[nx][ny]==2:
#                         if [nx,ny] not in body_list: # 방문처리 대신 포함 여부로 대신
#                             body_list.append([nx,ny])
#                             body_flag=True
#                             x,y=nx,ny
#                             break
#         if body_flag==False: # 다음 칸이 몸통이 아니라면
#             break # while 문 탈출
#     dic_body[num] = body_list

# def make_drow_ball_list():
#     drow_ball_list = []

#     # x,y,dir 을 넣는다.

#     for i in range(n):
#         drow_ball_list.append([i,0,0])
#     for i in range(n):
#         drow_ball_list.append([n-1,i,1])
#     for i in range(n-1,-1,-1):
#         drow_ball_list.append([i,n-1,2])
#     for i in range(n-1,-1,-1):
#         drow_ball_list.append([0,i,3])

#     # 정해진 턴수만큼만 drow_ball_list의 크기 설정
#     while 1:
#         if len(drow_ball_list)>=k:
#             return drow_ball_list[:k]
#         else:
#             drow_ball_list+=drow_ball_list

# def move_people(num):
#     x,y = dic_head[num] # 헤드의 x,y
#     head_move = False
#     # 머리는 빈칸을 찾거나, 빈칸이 아니면 원형으로 이어진 경우임(즉 머리와 꼬리가 인접함)
#     for d in range(4):
#         nx=x+dx[d]
#         ny=y+dy[d]

#         if 0<=nx<n and 0<=ny<n:
#             if graph_group[nx][ny]==num:
#                 if [nx,ny] not in dic_body[num] and [nx,ny] != dic_tail[num]:
#                     head_move=True
#                     dic_head[num]=[nx,ny]
#                     break

#     # 머리가 빈칸을 못찾은 경우에는 머리와 꼬리가 인접한 형태.
#     if head_move==False:
#         dic_head[num]=dic_tail[num]

#     # 몸통 이동
#     now_body = dic_body[num]

#     # 몸통이 없는 경우 (머리-꼬리 와 같은 형태)
#     if now_body==[]:
#         dic_tail[num] = [x,y]
#     else:
#         dic_body[num] = [[x,y]]+now_body[:-1] # 현재의 머리 좌표+ 몸통의 마지막 제외 더해서 몸통으로 변경
#         dic_tail[num] = now_body[-1]

# def switch(num):
#     dic_head[num], dic_tail[num] = dic_tail[num], dic_head[num]
#     new_body = []
#     for i in range(len(dic_body[num])-1,-1,-1):
#         new_body.append(dic_body[num][i])
#     dic_body[num] = new_body


# def start_drow_ball(x,y,dir):
#     global total_score
#     for speed in range(n):
#         nx = x + dx[dir]*speed
#         ny = y + dy[dir]*speed

#         if 0<=nx<n and 0<=ny<n:
#             # 현재 칸에 사람이 있는지 확인


#             for num in dic_head.keys():

#                 # 머리위치의 사람이라면
#                 if [nx,ny] == dic_head[num]:
#                     total_score+=(1*1)
#                     switch(num)
#                     return
#                 # 꼬리위치의 사람이라면
#                 elif [nx,ny] == dic_tail[num]:
#                     score = len(dic_body[num])+2
#                     total_score+=(score*score)
#                     switch(num)
#                     return

#                 # 몸통이라면
#                 else:
#                     for idx in range(len(dic_body[num])):
#                         a,b = dic_body[num][idx]
#                         if [a,b] ==[nx,ny]:
#                             score = 2+idx # 1(인덱스니까 +1) + (헤드의 존재 더하기) + idx
#                             total_score+=(score*score)
#                             switch(num)
#                             return

# n, m, k = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# # 해당 방향은 공을 던지는 방향을 고려해서 설정
# dx=[0,-1,0,1]
# dy=[1,0,-1,0]

# total_score = 0

# # 각 팀의 머리 몸통 꼬리를 담을 딕셔너리
# dic_head={}
# dic_tail={}
# dic_body={}

# # 각 팀별 그래프 만들기
# graph_group = [[0 for _ in range(n)] for _ in range(n)]
# visited = [[0 for _ in range(n)] for _ in range(n)]
# g_num = 0 # 그룹 넘버

# # 방문 처리를 통해서 dic_head, dic_tail의 좌표 찾기 및 그룹별로 그래프상에 위치 나타내기
# for i in range(n):
#     for j in range(n):
#         if visited[i][j]==0:
#             if graph[i][j]!=0:
#                 g_num+=1
#                 bfs(i,j,g_num)

# # head의 key 값을 시작점으로 몸통 좌표 찾아서 dic_body에 넣기
# for num in dic_head.keys():
#     find_body(num)

# drow_ball_list = make_drow_ball_list() # 볼을 던지는 시작좌표와 방향을(x,y,dir) 리스트에 순차적으로 다 넣는다.

# for turn in range(1,k+1):
#     for num in dic_head.keys():
#         move_people(num) # 사람 이동

#     # 공 던지기
#     idx = turn-1
#     x,y,dir = drow_ball_list[idx]
#     start_drow_ball(x,y,dir)

# print(total_score)

# 몸통없이 머리, 꼬리만 있는 경우(이 경우는 없을것 같다. 그 이유는 각팀의 이동선이 이어져있기 때문)
# 몸통이 길어서 머리 꼬리가 맞닿은 경우를 고려해야한다.
from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
direction = {0:[0,1], 1:[-1,0], 2:[0,-1], 3:[1,0]}

# 각팀의 머리를 따라 이동을 어떻게 할까?
# 머리 기준으로 이동선을 따라서 이동할때, 몸통이 아닌 위치로 이동한다.
def dfs(x,y,next_x,next_y,new_board,team_num): # 현재 위치, 이동할 위치
    if (next_x,next_y)==(None,None):
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0:
                if board[nx][ny]==2: # 몸통이면, 다음 dfs를 시작할 위치이다.
                    move_x, move_y = nx, ny
                else: # 몸통이 아니면, 머리가 이동할 위치
                    new_board[nx][ny] = board[x][y]
                    head[team_num] = [nx,ny]
        dfs(move_x, move_y, x,y,new_board,team_num)

    # 머리 이동이 아니면
    else:
        # 현좌표가 꼬리면 이것까지 하고 끝
        if board[x][y]==3:
            new_board[next_x][next_y] = board[x][y]
            tail[team_num] = [next_x, next_y]
        # 몸통이면, 다음 몸통을 찾는다.
        else:
            new_board[next_x][next_y] = board[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and (nx,ny)!=(next_x, next_y):
                    if board[nx][ny] == 2 or board[nx][ny] == 3:  # 몸통이면, 다음 dfs를 시작할 위치이다.
                        dfs(nx, ny, x,y,new_board,team_num)
                        break
    return new_board
def move():
    global board
    t_num=0
    new_board = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for key in head.keys():
                    if head.get(key) == [i,j]:
                        t_num = key
                        break
                new_board = dfs(i,j,None,None, new_board,t_num)

    # 나머지 길을 4로 바꿔준다.
    for i in range(n):
        for j in range(n):
            if board[i][j]!=0 and new_board[i][j]==0:
                new_board[i][j]=4

    board = new_board

def get_point(x,y):
    q=deque()
    q.append([x,y,1])
    visited=[[0 for _ in range(n)]for _ in range(n)]
    visited[x][y]=1

    while q:
        x,y,cnt = q.popleft()
        if board[x][y]==1:
            for key in head.keys():
                if head[key]==[x,y]:
                    board[x][y]=3
                    tmp = tail[key]
                    tail[key]=[x,y]
                    head[key]=tmp
                    board[tmp[0]][tmp[1]]=1
            return cnt*cnt

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and board[nx][ny]!=0 and board[nx][ny]!=4:
                if board[x][y]==3 and board[nx][ny]==1:
                    # 머리와 꼬리가 한바퀴 돌고 붙은 경우와 몸통이 없는 경우를 구분해야함.
                    continue
                elif board[nx][ny]!=3:
                    q.append([nx, ny, cnt + 1])
                    visited[nx][ny] = 1

def throw_ball(ball_dir, line):
    global score
    if ball_dir == 0:
        x = line
        y = 0
    elif ball_dir == 1:
        x = n - 1
        y = line
    elif ball_dir == 2:
        x = line
        y = n - 1
    else:
        x = 0
        y = line

    # 던져지는 위치에 사람이 있다면,
    if board[x][y] != 0 and board[x][y] != 4:
        score += get_point(x, y)
        return

    # x,y가 정해졌으므로(시작점) 한칸씩 이동하면서 사람이 맞는지 확인한다.
    nx = x
    ny = y
    for i in range(n - 1):
        nx = nx + direction[ball_dir][0]
        ny = ny + direction[ball_dir][1]
        if board[nx][ny] != 0 and board[nx][ny] != 4:
            score += get_point(nx, ny)
            break

n,m,k = map(int, input().split()) # n: 격자 크기, m: 팀의 개수, k: 라운드 수
board = [] # 0은 빈칸, 1은 머리, 2는 몸통, 3은 꼬리, 4는 이동선
for i in range(n):
    board.append(list(map(int, input().split())))

# 각 팀의 머리와 꼬리를 딕셔너리로 관리한다.
head = {}
tail = {}

visited = [[0 for _ in range(n)]for _ in range(n)]
team=1
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            head[team] = [i,j]
            q=deque()
            q.append([i,j])
            visited[i][j]=1
            while q:
                x,y = q.popleft()
                if board[x][y] == 3:
                    tail[team] = [x,y]
                    break
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]!=0 and visited[nx][ny]==0:
                        q.append([nx,ny])
                        visited[nx][ny]=1
            team+=1
# print(head)
# print(tail)

score = 0
for round in range(k):
    # 각팀의 머리 사람을 따라 한칸 이동
    move()
    # print(*board, sep = '\n')
    # 각 라운드 마다 공이 던져질 선과 방향을 구한다. (n배수마다 방향과 던져지는 라인이 바뀐다.)
    ball_dir = (round//n)%4
    line = round%n

    if ball_dir>=2:
        line = n-1-line

    # 던져서 맞는 사람을 찾는다.
    throw_ball(ball_dir, line)

    # 맞는 사람을 기준으로 머리 사람으로 부터 몇번째 사람인지 파악하고 점수를 더한다.

    # 맞은 팀은 머리와 꼬리가 바뀐다.
print(score)