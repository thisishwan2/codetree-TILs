# from collections import deque


# def first(play_thing, like_lst):
#     like_candidate = []
#     max_like = 0
#     for i in range(n):
#         for j in range(n):
#             like_friend_cnt = 0
#             if play_thing[i][j] == 0:
#                 for k in range(4):
#                     nx = i + dx[k]
#                     ny = j + dy[k]
#                     if 0 <= nx < n and 0 <= ny < n:
#                         if play_thing[nx][ny] in like_lst:
#                             like_friend_cnt += 1
#                 max_like = max(max_like, like_friend_cnt)
#                 tmp = [like_friend_cnt, i, j]
#                 like_candidate.append(tmp)
#     res = []
#     for i in like_candidate:
#         if i[0] == max_like:
#             res.append(i)

#     return res


# def second(play_thing, first_res):
#     candidate = []
#     res = []

#     # 1번 조건 만족하는 칸이 하나면
#     if len(first_res) == 1:
#         res.append([first_res[0][1], first_res[0][2]])

#     # 1번 조건 만족하는 칸이 2개 이상이면
#     else:
#         max_block = 0
#         for i in first_res:
#             empty_block = 0
#             for j in range(4):
#                 nx = i[1] + dx[j]
#                 ny = i[2] + dy[j]

#                 if 0 <= nx < n and 0 <= ny < n:
#                     if play_thing[nx][ny] == 0:
#                         empty_block += 1
#             max_block = max(max_block, empty_block)
#             tmp = [empty_block, i[1], i[2]]
#             candidate.append(tmp)

#         for i in candidate:
#             if i[0] == max_block:
#                 res.append([i[1],i[2]])

#     return res


# def find_place(second_res):
#     second_res = sorted(second_res)
#     return second_res[0]


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# n = int(input())

# play_thing = [[0 for _ in range(n)] for _ in range(n)]

# students = []
# students_dic={}
# for i in range(n * n):
#     student = list(map(int, input().split()))
#     tmp = [student[0], list(student[1:])]
#     students.append(tmp)  # n0,n1,n2,n3,n4
#     students_dic[student[0]]= list(student[1:])

# while True:

#     for i in students:
#         n0 = i[0]
#         like_lst = i[1]

#         # 1번
#         first_res = first(play_thing, like_lst)
#         # print(first_res)

#         # 후보 칸이 없으면 탈출
#         if len(first_res) == 0:
#             break

#         # 2번
#         second_res = second(play_thing, first_res)
#         # print(second_res)
#         # 3,4번
#         if len(second_res) == 1:
#             play_thing[second_res[0][0]][second_res[0][1]] = n0
#         else:
#             find_place_res = find_place(second_res)
#             play_thing[find_place_res[0]][find_place_res[1]] = n0
#     break

# # print(play_thing)

# # 최종 점수 계산
# total=0
# for i in range(n):
#     for j in range(n):
#         now_student = play_thing[i][j]
#         like_lst = students_dic.get(now_student)
#         like_friend_cnt=0
#         for k in range(4):
#             nx=i+dx[k]
#             ny=j+dy[k]

#             if 0<=nx<n and 0<=ny<n:
#                 if play_thing[nx][ny] in like_lst:
#                     like_friend_cnt+=1
        
#         if like_friend_cnt == 1:
#             total+=1
#         elif like_friend_cnt == 2:
#             total+=10
#         elif like_friend_cnt == 3:
#             total+=100
#         elif like_friend_cnt == 4:
#             total+=1000

# print(total)

# 놀이기구 탑승

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def find_friends(like_friends):
    res = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                like_friends_cnt = 0
                blank_cnt = 0
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]

                    if 0<=nx<n and 0<=ny<n:
                        # 비어 있다면
                        if board[nx][ny] ==0:
                            blank_cnt+=1
                        # 친한 친구가 있다면,
                        elif board[nx][ny] in like_friends:
                            like_friends_cnt+=1
                res.append([like_friends_cnt,blank_cnt,x,y])
    return res

n = int(input())
board = [[0 for _ in range(n)]for _ in range(n)]
like_dict = {}
for i in range(n*n):
    n0,n1,n2,n3,n4 = map(int, input().split())
    like_dict[n0] = [n1,n2,n3,n4]
    like_friends = [n1,n2,n3,n4]
    # 1. 각 칸별로 인접한 칸에 좋아하는 친구의 수를 확인
    res = find_friends(like_friends)
    # 우선순위에 맞게 정렬
    res = sorted(res, key=lambda x:(-x[0],-x[1],x[2],x[3]))

    board[res[0][2]][res[0][3]] = n0

    # print("======")
    # print(*board, sep = "\n")
    # print("======")

# 최종 점수 확인
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
point = 0
for x in range(n):
    for y in range(n):
        num = board[x][y]
        cnt = 0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] in like_dict[num]:
                    cnt+=1
        point+=score[cnt]
print(point)