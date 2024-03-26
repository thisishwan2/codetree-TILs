from collections import deque


def first(play_thing, like_lst):
    like_candidate = []
    max_like = 0
    for i in range(n):
        for j in range(n):
            like_friend_cnt = 0
            if play_thing[i][j] == 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if play_thing[nx][ny] in like_lst:
                            like_friend_cnt += 1
                max_like = max(max_like, like_friend_cnt)
                tmp = [like_friend_cnt, i, j]
                like_candidate.append(tmp)
    res = []
    for i in like_candidate:
        if i[0] == max_like:
            res.append(i)

    return res


def second(play_thing, first_res):
    candidate = []
    res = []

    # 1번 조건 만족하는 칸이 하나면
    if len(first_res) == 1:
        res.append([first_res[0][1], first_res[0][2]])

    # 1번 조건 만족하는 칸이 2개 이상이면
    else:
        max_block = 0
        for i in first_res:
            empty_block = 0
            for j in range(4):
                nx = i[1] + dx[j]
                ny = i[2] + dy[j]

                if 0 <= nx < n and 0 <= ny < n:
                    if play_thing[nx][ny] == 0:
                        empty_block += 1
            max_block = max(max_block, empty_block)
            tmp = [empty_block, i[1], i[2]]
            candidate.append(tmp)

        for i in candidate:
            if i[0] == max_block:
                res.append([i[1],i[2]])

    return res


def find_place(second_res):
    second_res = sorted(second_res)
    return second_res[0]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

play_thing = [[0 for _ in range(n)] for _ in range(n)]

students = []
students_dic={}
for i in range(n * n):
    student = list(map(int, input().split()))
    tmp = [student[0], list(student[1:])]
    students.append(tmp)  # n0,n1,n2,n3,n4
    students_dic[student[0]]= list(student[1:])

while True:

    for i in students:
        n0 = i[0]
        like_lst = i[1]

        # 1번
        first_res = first(play_thing, like_lst)
        # print(first_res)

        # 후보 칸이 없으면 탈출
        if len(first_res) == 0:
            break

        # 2번
        second_res = second(play_thing, first_res)
        # print(second_res)
        # 3,4번
        if len(second_res) == 1:
            play_thing[second_res[0][0]][second_res[0][1]] = n0
        else:
            find_place_res = find_place(second_res)
            play_thing[find_place_res[0]][find_place_res[1]] = n0
    break

# print(play_thing)

# 최종 점수 계산
total=0
for i in range(n):
    for j in range(n):
        now_student = play_thing[i][j]
        like_lst = students_dic.get(now_student)
        like_friend_cnt=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]

            if 0<=nx<n and 0<=ny<n:
                if play_thing[nx][ny] in like_lst:
                    like_friend_cnt+=1
        
        if like_friend_cnt == 1:
            total+=1
        elif like_friend_cnt == 2:
            total+=10
        elif like_friend_cnt == 3:
            total+=100
        elif like_friend_cnt == 4:
            total+=1000

print(total)