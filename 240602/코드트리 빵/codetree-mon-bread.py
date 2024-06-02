from collections import deque

# 최단 거리를 찾기 위한 bfs
def bfs(x,y,num):

    q = deque()
    q.append((x,y))
    visited = [[-2 for _ in range(n)]for _ in range(n)]
    visited[x][y]=-1

    while q:
        x,y = q.popleft()

        if (x,y) == (store[num][0], store[num][1]):
            return visited[x][y]


        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny]!=-1 and visited[nx][ny] == -2:
                    if visited[x][y] == -1: # 첫 for문일때는 다음칸에 현재 이동하게된 방향의 인덱스를 넣어줌
                        visited[nx][ny] = i
                    else:
                        visited[nx][ny] = visited[x][y]
                    q.append([nx, ny])

def find_basecamp(num):
    store_x, store_y = store[num]
    distance = 1e9
    b_x=0
    b_y=0
    index=0

    for idx, val in enumerate(basecamp_candidate):
        base_x, base_y = val

        q=deque()
        q.append([base_x,base_y,0])
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[base_x][base_y] = 1

        while q:
            x,y,cnt = q.popleft()

            if (x,y) == (store_x,store_y):
                if distance > cnt:
                    distance = cnt
                    b_x=base_x
                    b_y=base_y
                    index = idx

                break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] != -1 and visited[nx][ny]==0:
                        visited[nx][ny]=1
                        q.append([nx,ny,cnt+1])

    return b_x,b_y,index

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m = map(int, input().split())  # n: 격자의 크기, m: 사람의 수
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

basecamp_candidate=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            basecamp_candidate.append([i,j])
basecamp_candidate = sorted(basecamp_candidate, key = lambda x: (x[0], x[1]))
# print(basecamp_candidate)

store = {}
for i in range(m):
    x, y = map(int, input().split())
    store[i + 1] = [x - 1, y - 1]

time = 0
q = deque()
while True:

    disable_place = []

    # 1번: 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점을 향해 1칸 움직인다.
    for _ in range(len(q)):
        x, y, num = q.popleft()
        # 최단 거리로 움직이는 방법을 찾고, 여러개면 우선순위에 따라 움직인다.(이떄 막히는 칸을 고려해서 최단거리를 찾아야한다.)
        dir = bfs(x,y,num)
        next_x = x+dx[dir]
        next_y = y+dy[dir]

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
        base_x, base_y, idx = find_basecamp(time)
        arr[base_x][base_y] = -1
        basecamp_candidate.pop(idx)
        q.append([base_x, base_y, time])

    if len(q) == 0:
        break
print(time)