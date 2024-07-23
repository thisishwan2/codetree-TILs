# def move_down_t1(x,y, board):
#     global score
#
#     # 멈출때까지 내려간다.
#     while (x+1<=9 and board[x+1][y] == 0):
#         x=x+1
#
#     # 멈춘 위치에 블럭을 넣는다.
#     board[x][y]=1
#
#     # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
#     for i in range(6, 10):
#         if sum(board[i]) == 4:
#             board.pop(i)
#             board.insert(0, [0, 0, 0, 0])
#             score+=1
#
#     # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
#     if sum(board[4])>=1 or sum(board[5])>=1:
#         board.pop()
#         board.insert(0,[0,0,0,0])
#
# def move_down_t2(x,y, board):
#     global score
#
#     # 멈출때까지 내려간다.
#     while (x+1<=9 and (board[x+1][y] == 0 and board[x+1][y+1]==0)):
#         x=x+1
#
#     # 멈춘 위치에 블럭을 넣는다.
#     board[x][y]=1
#     board[x][y+1] = 1
#
#     # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
#     for i in range(6, 10):
#         if sum(board[i]) == 4:
#             board.pop(i)
#             board.insert(0, [0, 0, 0, 0])
#             score+=1
#
#     # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
#     if sum(board[4])>=1 or sum(board[5])>=1:
#         board.pop()
#         board.insert(0,[0,0,0,0])
#
# def move_down_t3(x,y, board):
#     global score
#
#     # 멈출때까지 내려간다.
#     while (x+2<=9 and board[x+2][y] == 0):
#         x=x+1
#
#     # 멈춘 위치에 블럭을 넣는다.
#     board[x][y]=1
#     board[x+1][y]=1
#
#     # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
#     for i in range(6, 10):
#         if sum(board[i]) == 4:
#             board.pop(i)
#             board.insert(0, [0, 0, 0, 0])
#             score+=1
#
#     # 연한 부분에 얼마나 겹치는 지 확인
#     stage_area = 0
#     if sum(board[4])>=1:
#         stage_area+=1
#     if sum(board[5])>=1:
#         stage_area+=1
#
#     # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
#     if stage_area==1:
#         board.pop()
#         board.insert(0,[0,0,0,0])
#     elif stage_area==2:
#         board.pop()
#         board.pop()
#         board.insert(0, [0, 0, 0, 0])
#         board.insert(0, [0, 0, 0, 0])
#
# k = int(input())
#
# down_board = [[0 for _ in range(4)]for _ in range(10)]
# right_board = [[0 for _ in range(4)]for _ in range(10)]
# score = 0
#
# for i in range(k):
#     t,x,y = map(int, input().split()) # t: 블록 종류, x,y: 블록 위치
#
#     # 테스리스 이동(단, 이동하는 중에 블럭의 일부가 다른 블럭과 닿는다면 멈춘다.)
#     if t==1:
#         move_down_t1(x,y, down_board)
#         move_down_t1(y,3-x, right_board)
#     elif t==2:
#         move_down_t2(x,y, down_board)
#         move_down_t3(y,3-x, right_board)
#     elif t==3:
#         move_down_t3(x,y, down_board)
#         move_down_t2(y,2-x, right_board)
#
# tile_cnt = 0
# # 보드에 놓인 타일 개수를 센다.
# for i in range(10):
#     for j in range(4):
#         if down_board[i][j]==1:
#             tile_cnt+=1
#         if right_board[i][j]==1:
#             tile_cnt+=1
#
# print(score)
# print(tile_cnt)

#===========================================
# 배열 앞뒤에 append를 하기 위해서 deque을 이용한다.
from collections import deque

def move_down_t1(x,y, board):
    global score

    # 멈출때까지 내려간다.
    while (x+1<=9 and board[x+1][y] == 0):
        x=x+1

    # 멈춘 위치에 블럭을 넣는다.
    board[x][y]=1

    # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
    for i in range(6, 10):
        if sum(board[i]) == 4:
            # board.pop(i) 주의 deque에서는 pop에 매개변수를 받지 않고, 단순히 pop과 popleft만 지원함
            del board[i]
            board.appendleft([0,0,0,0])
            score+=1

    # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
    if sum(board[4])>=1 or sum(board[5])>=1:
        board.pop()
        board.appendleft([0,0,0,0])

def move_down_t2(x,y, board):
    global score

    # 멈출때까지 내려간다.
    while (x+1<=9 and (board[x+1][y] == 0 and board[x+1][y+1]==0)):
        x=x+1

    # 멈춘 위치에 블럭을 넣는다.
    board[x][y]=1
    board[x][y+1] = 1

    # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
    for i in range(6, 10):
        if sum(board[i]) == 4:
            del board[i]
            board.appendleft([0,0,0,0])
            score+=1

    # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
    if sum(board[4])>=1 or sum(board[5])>=1:
        board.pop()
        board.appendleft([0,0,0,0])

def move_down_t3(x,y, board):
    global score

    # 멈출때까지 내려간다.
    while (x+2<=9 and board[x+2][y] == 0):
        x=x+1

    # 멈춘 위치에 블럭을 넣는다.
    board[x][y]=1
    board[x+1][y]=1

    # 만약 타일이 가득찬 행이 있는 경우엔 해당 행을 없애고 위에 있는 배열을 한칸 내린다.
    for i in range(6, 10):
        if sum(board[i]) == 4:
            del board[i]
            board.appendleft([0,0,0,0])
            score+=1

    # 연한 부분에 얼마나 겹치는 지 확인
    stage_area = 0
    if sum(board[4])>=1:
        stage_area+=1
    if sum(board[5])>=1:
        stage_area+=1

    # 만약 연한 부분에 블럭이 있다면 연한 행수만큼 배열을 밑으로 내린다.
    if stage_area==1:
        board.pop()
        board.appendleft([0,0,0,0])
    elif stage_area==2:
        board.pop()
        board.pop()
        board.appendleft([0,0,0,0])
        board.appendleft([0, 0, 0, 0])

k = int(input())

down_board = deque([[0 for _ in range(4)]for _ in range(10)])
right_board = deque([[0 for _ in range(4)]for _ in range(10)])
score = 0

for i in range(k):
    t,x,y = map(int, input().split()) # t: 블록 종류, x,y: 블록 위치

    # 테스리스 이동(단, 이동하는 중에 블럭의 일부가 다른 블럭과 닿는다면 멈춘다.)
    if t==1:
        move_down_t1(x,y, down_board)
        move_down_t1(y,3-x, right_board)
    elif t==2:
        move_down_t2(x,y, down_board)
        move_down_t3(y,3-x, right_board)
    elif t==3:
        move_down_t3(x,y, down_board)
        move_down_t2(y,2-x, right_board)

tile_cnt = 0
# 보드에 놓인 타일 개수를 센다.
for i in range(10):
    for j in range(4):
        if down_board[i][j]==1:
            tile_cnt+=1
        if right_board[i][j]==1:
            tile_cnt+=1

print(score)
print(tile_cnt)