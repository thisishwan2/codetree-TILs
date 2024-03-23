# 1,2 경우에서 n에 도착했다면, 사람을 내린다.
# 이동 하자마자 해당 위치의 안정성이 0인지 체크
n, k = map(int, input().split())
stability = list(map(int, input().split()))
human = [0] * (len(stability) // 2)
experience = 0

while k > 0:
    experience += 1

    # 1번 동작(무빙워크 회전)
    tmp = stability.pop()
    stability.insert(0, tmp)  # o(n)

    # 모든 인간 위치 조정
    for i in range(len(human) - 2, -1, -1):
        human[i + 1] = human[i]
        human[i] = 0

    # 인간위치를 조정 했는데 마지막에 인간이 있다면, 그 인간은 내리게 됨
    if human[-1] == 1:
        human.pop()
        human.append(0)

    # 2번 동작(가장 오른쪽 사람부터 무빙워크가 회전하는 방향으로 한칸 이동.(앞에 사람이 있거나 안정성이 0이면 이동 x))
    for i in range(len(human) - 1, -1, -1):
        if human[i] == 1 and human[i + 1] == 0 and stability[i + 1] > 0:
            human[i + 1] = human[i]
            human[i] = 0
            stability[i + 1] -= 1
            if stability[i + 1] == 0:
                k -= 1
            if human[-1] == 1:
                human.pop()
                human.append(0)

    # 3번 동작
    if human[0] == 0 and stability[0] > 0:
        human[0] = 1
        stability[0] -= 1
        if stability[0] == 0:
            k -= 1

print(experience)