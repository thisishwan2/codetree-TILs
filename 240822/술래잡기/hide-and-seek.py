# from collections import deque

# def move_runner():
#     global seeker_x, seeker_y
#     move_list = []
#     for i in runner_dic.keys():
#         x, y = runner_dic[i][0], runner_dic[i][1]

#         if abs(seeker_x - x) + abs(seeker_y - y) <= 3:
#             move_list.append(i)

#     for i in move_list:
#         x, y, d = runner_dic[i]


#         nx = x + dir_dic[d][0]
#         ny = y + dir_dic[d][1]

#         # 격자 벗어나지 않는 경우
#         if 0 <= nx < n and 0 <= ny < n:
#             # 술래가 없으면
#             if (nx,ny)!=(seeker_x, seeker_y):
#                 runner_dic[i] = [nx, ny, d]

#         # 격자를 벗어나는 경우
#         else:
#             d = d + 2
#             if d > 4:
#                 d = d - 4

#             nx = x + dir_dic[d][0]
#             ny = y + dir_dic[d][1]

#             if (nx,ny)!=(seeker_x, seeker_y): # 술래가 없으면
#                 runner_dic[i] = [nx, ny, d]



# def move_forward(next):
#     global seeker_x, seeker_y, total_score, turn
#     flag = False
#     for i in range(n):
#         if flag:
#             break

#         for j in range(n):
#             if seeker_move_arr[i][j]==next:
#                 seeker_x = i
#                 seeker_y = j
#                 d = seeker_forward[i][j]
#                 flag=True
#                 break


#     direction = dir_dic[d]
#     check_x = seeker_x
#     check_y = seeker_y


#     catch_runner_cnt=0
#     remove_lst = []
#     for i in range(3):
#         nx = check_x + direction[0]*i
#         ny = check_y + direction[1]*i

#         # 나무가 아님
#         if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
#             for j in runner_dic.keys():
#                 r_x = runner_dic[j][0]
#                 r_y = runner_dic[j][1]

#                 if (nx,ny) == (r_x, r_y):
#                     remove_lst.append(j)
#                     catch_runner_cnt+=1
#     for i in remove_lst:
#         runner_dic.pop(i)
#     total_score+=turn*catch_runner_cnt

# def move_backward(next):
#     global seeker_x, seeker_y, total_score, turn
#     flag = False
#     for i in range(n):
#         if flag:
#             break

#         for j in range(n):
#             if seeker_move_arr[i][j]==next:
#                 seeker_x = i
#                 seeker_y = j
#                 d = seeker_backward[i][j]
#                 flag = True
#                 break

#     direction = dir_dic[d]
#     check_x = seeker_x
#     check_y = seeker_y


#     catch_runner_cnt=0
#     remove_lst=[]
#     for i in range(3):
#         nx = check_x + direction[0]*i
#         ny = check_y + direction[1]*i

#         # 나무가 아님
#         if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
#             for j in runner_dic.keys():
#                 r_x = runner_dic[j][0]
#                 r_y = runner_dic[j][1]

#                 if (nx,ny) == (r_x, r_y):
#                     remove_lst.append(j)
#                     catch_runner_cnt+=1

#     for i in remove_lst:
#         runner_dic.pop(i)
#     total_score+=turn*catch_runner_cnt

# def forward():
#     x = n//2
#     y = n//2
#     q=deque()
#     q.append([x,y]) # x,y,d


#     while q:
#         x,y= q.popleft()
#         for i in range(1,5):
#             nx = x + dir_dic[i][0]
#             ny = y + dir_dic[i][1]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if seeker_move_arr[nx][ny]==seeker_move_arr[x][y]+1:

#                     for i in dir_dic.keys():
#                         if dir_dic[i] == [nx-x, ny-y]:
#                             seeker_forward[x][y]=i
#                     q.append([nx,ny])


# def backward():
#     x = 0
#     y = 0
#     q = deque()
#     q.append([x, y])  # x,y,d

#     while q:
#         x, y = q.popleft()
#         for i in range(1, 5):
#             nx = x + dir_dic[i][0]
#             ny = y + dir_dic[i][1]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if seeker_move_arr[nx][ny] == seeker_move_arr[x][y] - 1:

#                     for i in dir_dic.keys():
#                         if dir_dic[i] == [nx - x, ny - y]:
#                             seeker_backward[x][y] = i
#                     q.append([nx, ny])





# def find_seeker_move():
#     global seeker_x, seeker_y, seeker_dir

#     x = seeker_x
#     y = seeker_y
#     d = seeker_dir

#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     visited[x][y] = 1

#     for i in range(2, n * n + 1):
#         nx = x + dir_dic[d][0]
#         ny = y + dir_dic[d][1]

#         if visited[nx][ny] == 0:
#             x = nx
#             y = ny
#             d = d + 1

#             if d > 4:
#                 d = d - 4

#             seeker_move_arr[nx][ny] = i
#             visited[nx][ny]=1

#         # 다음칸이 이미 간곳
#         else:
#             d = d - 1

#             if d == 0:
#                 d = 4

#             nx = x + dir_dic[d][0]
#             ny = y + dir_dic[d][1]

#             if visited[nx][ny] == 0:
#                 x = nx
#                 y = ny
#                 d = d + 1

#                 if d > 4:
#                     d = d - 4

#                 seeker_move_arr[nx][ny] = i
#                 visited[nx][ny] = 1


# n, m, h, k = map(int, input().split())

# dir_dic = {1: [0, 1], 2: [1, 0], 3: [0, -1], 4: [-1, 0]}  # 우,하,좌,상

# seeker_x = n // 2
# seeker_y = n // 2
# seeker_dir = 4

# arr = [[0 for _ in range(n)] for _ in range(n)]
# runner_dic = {}

# # 도망자 x,y,d
# for i in range(1, m + 1):
#     x, y, d = map(int, input().split())
#     runner_dic[i] = [x - 1, y - 1, d]
# # 나무 x,y
# for _ in range(h):
#     x, y = map(int, input().split())
#     arr[x - 1][y - 1] = 2


# # 술래 이동 순서 배열 생성
# seeker_move_arr = [[0 for _ in range(n)] for _ in range(n)]
# seeker_move_arr[seeker_x][seeker_y] = 1
# find_seeker_move()

# # 순방향 배열 생성
# seeker_forward = [[0 for _ in range(n)] for _ in range(n)]
# forward()
# seeker_forward[0][0]=2
# # 역방향 배열 생성
# seeker_backward = [[0 for _ in range(n)] for _ in range(n)]
# backward()
# seeker_backward[n//2][n//2]=4

# # 이동할 순서 리스트 만들기
# seeker_move_seq = []
# tmp1 = [i for i in range(2, n*n+1)]
# tmp2 = [i for i in range(n*n-1,0,-1)]
# while 1:
#     if len(seeker_move_seq)>=k:
#         seeker_move_seq = seeker_move_seq[:k]
#         break
#     else:
#         seeker_move_seq = seeker_move_seq + tmp1 + tmp2

# seeker_move_seq.insert(0,1)

# total_score=0
# turn=1
# for i in range(1, len(seeker_move_seq)):
#     for j in range(2):

#         # 도망자 턴
#         if j == 0:
#             # 술래와 거리가 3인지를 확인하고, 움직임
#             move_runner()

#         # 술래 턴
#         elif j==1:

#             # 순방향
#             if seeker_move_seq[i-1] < seeker_move_seq[i]:
#                 move_forward(seeker_move_seq[i])
#             # 역방향
#             elif seeker_move_seq[i-1] > seeker_move_seq[i]:
#                 move_backward(seeker_move_seq[i])
#     turn+=1
# print(total_score)






# 술래잡기

# 도망자가 움직인 뒤, 술래가 움직인다.
# 도망자는 현재 술래와 거리가 3이하인 도망자만 움직인다. -> 도망자와 술래의 거리를 저장해놓는다.
# 바라보는 방향으로 1칸 움직인다.
from collections import deque

def move_hider(): # 술래와 거리가 3이하인 도망자들의 리스트를 전달받는다.
    new_hider_dict={}
    for key in hider.keys():
        x,y = key[0],key[1]
        # 거리가 3이하면
        if abs(fx-x)+abs(fy-y)<=3:

            for d in hider.get(key):
                nx=x+dir[d][0]
                ny=y+dir[d][1]

                # 격자를 벗어나지 않는 경우
                if 1<=nx<=n and 1<=ny<=n:
                    # 이동하는 칸에 술래가 없다면, 그 칸으로 이동한다.
                    if (nx,ny)!=(fx,fy):
                        if new_hider_dict.get((nx, ny)) == None:
                            new_hider_dict[(nx,ny)] = [d]
                        else:
                            new_hider_dict[(nx, ny)].append(d)
                    # 이동하는 칸에 술래가 있다면, 움직이지 않는다.
                    else:
                        if new_hider_dict.get((x, y)) == None:
                            new_hider_dict[(x,y)] = [d]
                        else:
                            new_hider_dict[(x, y)].append(d)
                # 격자를 벗어나는 경우
                else:
                    # 반대 방향으로 틀어준다.
                    if d==0: d=2
                    elif d==1: d=3
                    elif d==2: d=0
                    elif d==3: d=1

                    nx = x + dir[d][0]
                    ny = y + dir[d][1]

                    # 이동하는 칸에 술래가 없다면, 그 칸으로 이동한다.
                    if (nx, ny) != (fx, fy):
                        if new_hider_dict.get((nx, ny)) == None:
                            new_hider_dict[(nx, ny)] = [d]
                        else:
                            new_hider_dict[(nx, ny)].append(d)
                    else:
                        if new_hider_dict.get((x, y)) == None:
                            new_hider_dict[(x, y)] = [d]
                        else:
                            new_hider_dict[(x, y)].append(d)

        # 거리가 3이하가 아니면,
        else:
            # 새로운 딕셔너리에 위치를 넣는다.
            if new_hider_dict.get((x,y)) == None:
                new_hider_dict[(x,y)] = hider.get(key)
            else:
                new_hider_dict[(x, y)].extend(hider.get(key))
    return new_hider_dict

def move_available_finder(fx,fy):
    moving_lst = []
    visited = [[0 for _ in range(n+1)]for _ in range(n+1)]
    visited[fx][fy] = 1
    q=deque()
    q.append([fx,fy,0])

    while q:
        x,y,d = q.popleft()
        moving_lst.append([x, y, d])

        if (x,y) == (1,1):
            break

        nx=x+dir[d][0]
        ny=y+dir[d][1]

        if 1<=nx<=n and 1<=ny<=n:
            if visited[nx][ny]==0:
                visited[nx][ny]=1
                nd=(d+1)%4

                # 다음 방향이 방문하지 않으면 방향 바꾸고,
                if visited[nx+dir[nd][0]][ny+dir[nd][1]]==0:
                    q.append([nx,ny,nd])
                # 방문했으면, 그래도 유지
                else:
                    q.append([nx,ny,d])
    moving_lst.pop() # 마지막은 겹친다.
    # 반대 방향에 대해서도 탐색을 진행한다.
    q=deque()
    q.append([1,1,2])
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited[1][1] = 1
    while q:
        x,y,d = q.popleft()
        moving_lst.append([x, y, d])

        if (x,y) == (fx,fy):
            moving_lst.pop() # 마지막은 겹친다.
            break

        nx=x+dir[d][0]
        ny=y+dir[d][1]

        if 1<=nx<=n and 1<=ny<=n:
            if visited[nx][ny]==0:
                visited[nx][ny]=1

                # 직잔이 가능한지 확인하고, 가능하면 방향 유지
                if 1<= nx+dir[d][0]<= n and 1<= ny+dir[d][1]<= n and visited[nx+dir[d][0]][ny+dir[d][1]]==0:
                    q.append([nx,ny,d])
                # 직진이 불가하면 반시계로 꺾는다.
                else:
                    nd = d-1
                    if nd<0:
                        nd=3
                    q.append([nx,ny,nd])

    return moving_lst


dir = {0:[-1,0], 2:[1,0], 3:[0,-1], 1:[0,1]}
n,m,h,k = map(int, input().split())

fx, fy = n//2+1, n//2+1
# 술래가 갈 수 있는 길을 미리 만든다.
finder_moving_list = move_available_finder(fx, fy)


hider = {}
for _ in range(m):
    x,y,d = map(int, input().split()) # 도망자 위치와 방향
    # d가 1이면 좌우로만 움직인다.
    if d == 1:
        if hider.get((x,y)) == None:
            hider[(x,y)]=[1] # 이때 항상 오른쪽을 본다.
        else:
            hider[(x, y)].append(3)
    # d가 2면 상하로만 움직인다.
    elif d==2:
        if hider.get((x,y)) == None:
            hider[(x,y)] = [2]
        else:
            hider[(x, y)].append(1)

tree = {} # 나무는 고정임
for _ in range(h):
    x,y = map(int, input().split())
    tree[(x,y)] = 1

finder_idx=0
size = len(finder_moving_list)
score = 0
for turn in range(k):

    # 도망자가 움직인다.(동시에)
    # 현재 술래와 거리가 3이하인 도망자만 움직인다.
    hider = move_hider()
    # print(hider)

    # 술래가 움직인다.
    finder_idx=(finder_idx+1)%size
    finder_x, finder_y,d = finder_moving_list[finder_idx]
    # 시야 내의 3칸의 술래는 잡는다. 이때 나무의 위치는 넘어간다.
    nfinder_x, nfinder_y = finder_x+dir[d][0], finder_y+dir[d][1]
    nnfinder_x, nnfinder_y = nfinder_x+dir[d][0], nfinder_y+dir[d][1]

    # 나무가 아니고, 술래가 시야에 있으면
    if tree.get((finder_x,finder_y))==None and hider.get((finder_x, finder_y)) != None:
        people_cnt = len(hider.get((finder_x, finder_y)))
        del hider[(finder_x, finder_y)]
        score+=people_cnt*(turn+1)
    if tree.get((nfinder_x,nfinder_y))==None and hider.get((nfinder_x, nfinder_y)) != None:
        people_cnt = len(hider.get((nfinder_x, nfinder_y)))
        del hider[(nfinder_x, nfinder_y)]
        score+=people_cnt*(turn+1)
    if tree.get((nnfinder_x,nnfinder_y))==None and hider.get((nnfinder_x, nnfinder_y)) != None:
        people_cnt = len(hider.get((nnfinder_x, nnfinder_y)))
        del hider[(nnfinder_x, nnfinder_y)]
        score+=people_cnt*(turn+1)

    fx, fy = finder_x, finder_y

print(score)