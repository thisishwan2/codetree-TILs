def turn(num, d, k):
    tmp=[0]*m
    if d == 0: # 시계로 회전
        for i in range(m):
            tmp[(i+k)%m] = target[num][i]
        target[num] = tmp
    else: # 반시계로 회전
        for i in range(m):
            tmp[i] = target[num][(i+k)%m]
        target[num] = tmp
    # print(tmp)

def is_erase():
    erase_list=set()
    for i in range(n):
        if i==0:
            for j in range(m):

                if (target[i][j] == target[i][j-1] != 0):
                    erase_list.add((i, j))
                    erase_list.add((i, j-1))

                if (target[i][j] == target[i][(j+1)%m] !=0):
                    erase_list.add((i, j))
                    erase_list.add((i, (j + 1)%m))
        else:
            for j in range(m):
                if (target[i][j] == target[i][j-1] != 0):
                    erase_list.add((i, j))
                    erase_list.add((i, j - 1))
                if (target[i][j] == target[i][(j+1)%m] != 0):
                    erase_list.add((i, j))
                    erase_list.add((i, (j + 1) % m))

                if (target[i][j] == target[i-1][j] != 0):
                    erase_list.add((i, j))
                    erase_list.add((i-1, j))
    return erase_list

def sum_target():
    total = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if target[i][j]!=0:
                total+= target[i][j]
                cnt+=1
    return total, cnt

def normalization(avg):
    for i in range(n):
        for j in range(m):
            if target[i][j] != 0 and target[i][j] > avg:
                target[i][j]-=1
            elif target[i][j] !=0 and target[i][j] < avg:
                target[i][j]+=1

def erase(erase_set):

    for x,y in list(erase_set):
        target[x][y] = 0

n,m,q = map(int, input().split()) # n: 원판의 개수, m: 원판내의 숫자의 개수, q: 회전 횟수

target = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    target.append(tmp)

# print(target)

for num in range(q):
    x,d,k = map(int, input().split()) # x: 원판의 종류(번호), d: 회전 방향(0: 시계, 1: 반시계), k: 회전 칸수

    # x의 경우 회전하는 원판의 번호가 x의 배수일 경우 회전 한다는 뜻
    card = 1
    while x*card <= n:
        turn(x*card-1, d, k)
        card+=1

    erase_set = is_erase()
    # 회전 이후 원판에 수가 남아 있으면, 인접하면서 숫자가 같은 수를 지운다.
    # 지워지는 수가 존재하는지 확인
    if erase_set:
        erase(erase_set)
    else: # 정규화를 수행한다.
        # 원판에 남은 수가 없으면 정규화를 진행하지 않는다.
        total, cnt = sum_target()
        if total==0:
            pass
        else: # 정규화 수행
            normalization(total//cnt)

print(sum_target()[0])