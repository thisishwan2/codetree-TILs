# # 1,2 경우에서 n에 도착했다면, 사람을 내린다.
# # 이동 하자마자 해당 위치의 안정성이 0인지 체크
# n, k = map(int, input().split())
# stability = list(map(int, input().split()))
# human = [0] * (len(stability) // 2)
# experience = 0

# while k > 0:
#     experience += 1

#     # 1번 동작(무빙워크 회전)
#     tmp = stability.pop()
#     stability.insert(0, tmp)  # o(n)

#     # 모든 인간 위치 조정
#     for i in range(len(human) - 2, -1, -1):
#         human[i + 1] = human[i]
#         human[i] = 0

#     # 인간위치를 조정 했는데 마지막에 인간이 있다면, 그 인간은 내리게 됨
#     if human[-1] == 1:
#         human.pop()
#         human.append(0)

#     # 2번 동작(가장 오른쪽 사람부터 무빙워크가 회전하는 방향으로 한칸 이동.(앞에 사람이 있거나 안정성이 0이면 이동 x))
#     for i in range(len(human) - 1, -1, -1):
#         if human[i] == 1 and human[i + 1] == 0 and stability[i + 1] > 0:
#             human[i + 1] = human[i]
#             human[i] = 0
#             stability[i + 1] -= 1
#             if stability[i + 1] == 0:
#                 k -= 1
#             if human[-1] == 1:
#                 human.pop()
#                 human.append(0)

#     # 3번 동작
#     if human[0] == 0 and stability[0] > 0:
#         human[0] = 1
#         stability[0] -= 1
#         if stability[0] == 0:
#             k -= 1

# print(experience)

# 불안한 무빙워크

# 사람이 어떤 칸에 올라가거나 이동하면, 그 칸의 안정성은 1만큼 감소하고, 안정성이 0인 칸에는 올라갈 수 없다.

# 2. 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한칸 이동가능하면 이동한다.
# 이때, 앞선 칸에 사람이 있거나 안정성이 0이면 이동x

# 3. 1번 칸에 사람이 없고, 안정성이 0이 아니면 사람을 한명 더 올린다.

# 4. 안정성 0인 칸이 k개 이상이면 종료

# 1번
def move_moving_walk():
    # 무빙워크 이동
    new_moving_walk = moving_walk[:2*n-1]
    new_moving_walk.insert(0,moving_walk[-1])
    # 사람들도 이동
    new_people = people[:n-1]
    new_people.insert(0,0)

    return new_moving_walk, new_people

n,k = map(int, input().split()) # n: 무빙워크 길이, k: 안정서 0인 판의 개수
moving_walk = list(map(int, input().split()))
people = [0]*n
turn=0
while True:
    turn+=1
    # 1. 무빙워크가 한칸 회전한다
    moving_walk, people = move_moving_walk()

    # 2. 가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한칸 이동가능하면 이동한다.
    # 이때, 앞선 칸에 사람이 있거나 안정성이 0이면 이동x
    for i in range(n-1, -1, -1):
        if people[i]!=0:
            # 무빙워크 끝자락이면
            if i == n-1:
                # 해당 사람은 내린다.
                people[i]=0
            else:
                # 앞칸에 사람이 없고, 안정성이 0이상이면 이동
                if people[i+1] == 0 and moving_walk[i+1]>0:
                    people[i+1] = 1
                    people[i]=0
                    # 안정성 감소
                    moving_walk[i+1]-=1

    # 3. 1번 칸에 사람이 없고, 안정성이 0이 아니면 사람을 한명 더 올린다.
    if people[0] == 0 and moving_walk[0]>0:
        people[0]=1
        moving_walk[0]-=1

    # 4. 안정성 0인 칸이 k개 이상이면 종료
    stable_cnt = 0
    for i in moving_walk:
        if i==0:
            stable_cnt+=1

    if stable_cnt>=k:
        break
print(turn)