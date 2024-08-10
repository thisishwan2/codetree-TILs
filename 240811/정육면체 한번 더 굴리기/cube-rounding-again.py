# def dice_change(dice, direction):
#     if direction == 1:
#         up = dice[0][1]
#         floor = dice[1][1]
#         down = dice[2][1]
#         celing = dice[1][3]

#         dice[0][1] = celing
#         dice[1][1] = up
#         dice[2][1] = floor
#         dice[1][3] = down

#     elif direction == 2:
#         up = dice[0][1]
#         floor = dice[1][1]
#         down = dice[2][1]
#         celing = dice[1][3]

#         dice[0][1] = floor
#         dice[1][1] = down
#         dice[2][1] = celing
#         dice[1][3] = up

#     elif direction == 3:
#         tmp = dice[1].pop()
#         dice[1].insert(0, tmp)

#     else:
#         tmp = dice[1].pop(0)
#         dice[1].append(tmp)


# def bfs(board, nx, ny):
#     q = deque()
#     q.append([nx, ny])
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     visited[nx][ny] = 1
#     num = board[nx][ny]
#     score = num
#     while q:
#         x, y = q.popleft()
#         for i in range(1, 5):
#             nx = x + dir.get(i)[0]
#             ny = y + dir.get(i)[1]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if board[nx][ny] == num and visited[nx][ny] == 0:
#                     q.append([nx, ny])
#                     visited[nx][ny] = 1
#                     score += num
#     return score


# from collections import deque

# n, m = map(int, input().split())

# board = []
# for i in range(n):
#     board.append(list(map(int, input().split())))

# x, y = 0, 0
# direction = 4
# dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

# dice = [[0, 5, 0, 0], [4, 6, 3, 1], [0, 2, 0, 0]]
# dice_floor_x = 1
# dice_floor_y = 1

# total = 0
# for i in range(m):

#     nx = x + dir.get(direction)[0]
#     ny = y + dir.get(direction)[1]

#     # 격자 안인지를 고려하기, 밖으로 나가려하면 반대로 튕겨나감
#     if 0 > nx:
#         direction = 2
#         nx = x + dir.get(direction)[0]
#     elif nx >= n:
#         direction = 1
#         nx = x + dir.get(direction)[0]

#     if 0 > ny:
#         direction = 4
#         ny = y + dir.get(direction)[1]
#     elif ny >= n:
#         direction = 3
#         ny = y + dir.get(direction)[1]

#     # 주사위를 굴림
#     dice_change(dice, direction)

#     # 점수 입력
#     total += bfs(board, nx, ny)

#     # 바닥의 칸보다 큰 경우
#     if dice[dice_floor_x][dice_floor_y] > board[nx][ny]:
#         if direction == 1:
#             direction = 4
#         elif direction == 2:
#             direction = 3
#         elif direction == 3:
#             direction = 1
#         else:
#             direction = 2
#     elif dice[dice_floor_x][dice_floor_y] < board[nx][ny]:
#         if direction == 1:
#             direction = 3
#         elif direction == 2:
#             direction = 4
#         elif direction == 3:
#             direction = 2
#         else:
#             direction = 1
#     else:
#         pass
#     x = nx
#     y = ny
# print(total)

# 정육면체 한번 더 굴리기
import copy
from collections import deque


def dice_up(dice):
    new_dice = copy.deepcopy(dice)
    new_dice[1][1] = dice[0][1]
    new_dice[1][0] = dice[1][0]
    new_dice[1][2] = dice[1][2]
    new_dice[2][1] = dice[1][1]
    new_dice[0][1] = 7-new_dice[2][1]

    return new_dice
def dice_down(dice):
    new_dice = copy.deepcopy(dice)
    new_dice[1][1] = dice[2][1]
    new_dice[1][0] = dice[1][0]
    new_dice[1][2] = dice[1][2]
    new_dice[0][1] = dice[1][1]
    new_dice[2][1] = 7-new_dice[0][1]

    return new_dice
def dice_left(dice):
    new_dice = copy.deepcopy(dice)
    new_dice[1][1] = dice[1][0]
    new_dice[1][2] = dice[1][1]
    new_dice[0][1] = dice[0][1]
    new_dice[2][1] = dice[2][1]
    new_dice[1][0] = 7-new_dice[1][2]

    return new_dice
def dice_right(dice):
    new_dice = copy.deepcopy(dice)
    new_dice[1][1] = dice[1][2]
    new_dice[1][0] = dice[1][1]
    new_dice[0][1] = dice[0][1]
    new_dice[2][1] = dice[2][1]
    new_dice[1][2] = 7-new_dice[1][0]

    return new_dice

n,m = map(int, input().split()) # n: 격자 크기, m: 굴리는 횟수
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# print(board)

# 상우하좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

score = 0
x,y = 0,0
dir = 1
dice = [[0,5,0],[4,6,3],[0,2,0]]
# m번 주사위를 굴린다.
for _ in range(m):

    # 방향을 따라서 주사위를 굴린다. (격자 밖을 나간다면 방향을 반대로 돌리고 한칸 움직인다.)
    nx=x+dx[dir]
    ny=y+dy[dir]

    # 격자 밖으로 나가는 경우
    if not(0<=nx<n and 0<=ny<n):
        dir = (dir+2)%4
        nx = x + dx[dir]
        ny = y + dy[dir]

    if dir == 0:
        dice = dice_up(dice)
    elif dir == 2:
        dice = dice_down(dice)
    elif dir == 3:
        dice = dice_left(dice)
    elif dir == 1:
        dice = dice_right(dice)

    # 놓여진 칸에 인접하며 같은 숫자가 적힌 칸의 합만큼 점수를 얻는다.
    q=deque()
    cnt = 1
    num = board[nx][ny]
    q.append([nx,ny])
    visited = [[0 for __ in range(n)] for __ in range(4)]
    visited[nx][ny]=1
    while q:
        x_,y_ = q.popleft()
        for i in range(4):
            nx_ = x_+dx[i]
            ny_ = y_+dy[i]

            if 0<=nx_<n and 0<=ny_<n and num == board[nx_][ny_] and visited[nx_][ny_]==0:
                cnt+=1
                q.append([nx_, ny_])
                visited[nx_][ny_]=1

    score+= cnt * num

    # 주사위 아랫면과 보드의 숫자를 비교한다.
    # 이때 주사위 아랫면이 크면, 현재 방향에서 90도 시계방향으로 회전한다.(방향 변경)
    # 작으면, 반시계로 90도 회전
    # 동일하면, 방향 변경 x
    center = dice[1][1]
    if center == board[nx][ny]:
        pass
    elif center > board[nx][ny]:
        dir = (dir + 1)%4
    elif center < board[nx][ny]:
        if dir-1<0:
            dir = 3
        else:
            dir=dir-1

    x=nx
    y=ny

print(score)