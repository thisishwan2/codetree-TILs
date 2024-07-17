# 처음에는 이해가 안된 부분으로 지역을 나누는것이 헷갈렸다.
# 즉, 기울어진 사각형을 하나 그리고, 그 경계와 내부는 1번 부족의 지역
# 해당 사각형을 기준으로 왼쪽 상단의 나머지 공간 중 기울어진 사각형의 위쪽 꼭짓점 좌표는 포함하고, 왼쪽 꼭짓점은 포함하지 않는 부분이 2번부족
# 해당 사각형을 기준으로 오른쪽 상단의 나머지 공간 중 기울어진 사각형의 오른쪽 꼭짓점 좌표는 포함하고, 위쪽 꼭짓점은 포함하지 않는 부분이 3번부족
# 해당 사각형을 기준으로 왼쪽 하단의 나머지 공간 중 기울어진 사각형의 오른쪽 꼭짓점 좌표는 포함하고, 아래 꼭짓점은 포함하지 않는 부분이 4번부족
# 해당 사각형을 기준으로 오른쪽 하단의 나머지 공간 중 기울어진 사각형의 하단 꼭짓점 좌표는 포함하고, 오른쪽 꼭짓점은 포함하지 않는 부분이 2번부족

# 따라서 기울어진 사각형이 될 수 있는 경우를 모두 구해서, 가장 많은 인원 부족의 인원수와 가장 적은 인원 부족의 인원수의 차이를 구한다.
# 기울어진 사각형을 구하는게 어려움
def cal(x,y,d1,d2):
    temp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    temp[x][y]=5
    # 경계만 표시한다.
    # 왼쪽 상단 대각선
    for i in range(1, d1+1):
        temp[x+i][y-i] = 5
    # 오른쪽 상단 대각선
    for i in range(1, d2+1):
        temp[x+i][y+i] = 5
    # 왼쪽 하단 대각선
    for i in range(1, d2+1):
        temp[x+d1+i][y-d1+i]=5 # 시작점이 왼쪽 꼭짓점
    # 오른쪽 하단 대각선
    for i in range(1, d1 + 1):
        temp[x+d2+i][y+d2-i] = 5 # 시작점이 오른쪽 꼭짓점

    people = [0]*5 # 선거구는 5군데

    # 2번 구역 계산
    for i in range(1,x+d1):
        for j in range(1,y+1):
            if temp[i][j]==5:
                break
            people[1]+=graph[i][j]

    # 3번 구역 계산
    for j in range(n,y,-1):
        for i in range(1,x+d2+1):
            if temp[i][j]==5:
                break
            people[2]+=graph[i][j]

    # 4번 구역 계산
    for i in range(x+d1,n+1):
        for j in range(1,y-d1+d2):
            if temp[i][j]==5:
                break
            people[3]+=graph[i][j]

    # 5번 구역 계산
    for i in range(x+d2+1,n+1):
        for j in range(n, y-d1+d2-1, -1):
            if temp[i][j]==5:
                break
            people[4]+=graph[i][j]

    people[0] = total - sum(people)

    return max(people) - min(people)

n=int(input())
graph=[[]]
result= 1e9
total = 0
# area에는 지역별 인구수가 적혀있다.
# 문제는 0번 인덱스부터 사용하지 않고, 1번부터 이용하도록 한다.(계산의 복잡성을 줄이기 위해)
for i in range(1, n+1):
    graph.append([0] + (list(map(int, input().split()))))

for i in range(1,n+1):
    total+=sum(graph[i])

# i,j는 기울어진 사각형의 윗쪽 꼭짓점 좌표
# d1, d2는 기울어진 사각형의 윗쪽 꼭짓점으로 부터 경계선의 길이(왼쪽, 오른쪽)
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if y-d1>=1 and y+d2<=n and x+d1+d2<=n:
                    result = min(result, cal(x, y, d1, d2))

print(result)