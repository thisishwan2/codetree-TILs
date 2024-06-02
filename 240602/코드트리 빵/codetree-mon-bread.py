from collections import deque


def find_basecamp(people_num):
    distance = 1e9
    x = n
    y = n
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:

                # 거리가 최단 거리면
                if abs(i - store[people_num][0]) + abs(j - store[people_num][1]) < distance:
                    distance = abs(i - store[people_num][0]) + abs(j - store[people_num][1])
                    x = i
                    y = j

                # 거리가 같으면
                elif abs(i - store[people_num][0]) + abs(j - store[people_num][1]) == distance:
                    if (x > i):  # 행이 작으면
                        x = i
                        y = j
                    elif (x == i):  # 행이 같으면
                        if (y > j):  # 열이 작은 경우만
                            x = i
                            y = j
    return x, y


dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = map(int, input().split())  # n: 격자의 크기, m: 사람의 수
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

store = {}
for i in range(m):
    x, y = map(int, input().split())
    store[i + 1] = [x - 1, y - 1]

# print(*arr, sep="\n")
# print(store)

time = 0
q = deque()
while True:

    disable_place = []

    # 1번: 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점을 향해 1칸 움직인다.
    for _ in range(len(q)):
        x, y, num = q.popleft()

        # 최단 거리 변수 설정
        distance = 1e9
        next_x = 0
        next_y = 0

        # 최단 거리로 움직이는 방법을 찾고, 여러개면 우선순위에 따라 움직인다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != -1:
                    if abs(store[num][0] - nx) + abs(store[num][1] - ny) < distance:
                        next_x = nx
                        next_y = ny
                        distance = abs(store[num][0] - nx) + abs(store[num][1] - ny)

        # 2번: 편의점에 도착하면 멈추고, 해당 칸을 못지나가게 만든다.(못지나가게 하는 것은 모든 사람이 지나간 뒤에 해야한다.)
        if [next_x, next_y] == store[num]:  # 편의점에 도착한 경우
            disable_place.append([next_x, next_y])
        else:  # 편의점이 아니면, 큐에 넣는다.
            q.append([next_x, next_y, num])

    # 모든 사람이 지나간 다음 못지나가는 부분은 처리
    for i in disable_place:
        arr[i[0]][i[1]] = -1

    # 3번: 현재 시간이 m보다 작거나 같으면, 베이스 캠프에 들어간다.
    time += 1
    if time <= m:
        # 베이스 캠프를 선정하고 거기에 위치시킨다.
        base_x, base_y = find_basecamp(time)
        arr[base_x][base_y] = -1
        q.append([base_x, base_y, time])

    if len(q) == 0:
        break
print(time)