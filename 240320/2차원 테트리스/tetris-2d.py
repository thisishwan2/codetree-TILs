def move_t1(arr, x, y):
    while x + 1 < 10 and arr[x + 1][y] == 0:
        arr[x][y] = 0
        arr[x + 1][y] = 1
        x = x + 1

# type 2 형태를 하고 내려오는 경우에 사용
def move_t2(arr, x,y):
    while x + 1 <10  and arr[x + 1][y] == 0 and arr[x+1][y + 1] == 0:
        arr[x][y]=0
        arr[x][y+1]=0

        arr[x+1][y]=1
        arr[x+1][y+1]=1

        x=x+1

# type 3 형태를 하고 내려오는 경우에 사용
def move_t3(arr, x,y):
    while x+2<10 and arr[x+2][y]==0:
        arr[x][y]=0
        arr[x+2][y]=1

        x=x+1


# 꽉찬 행을 검사 및 삭제
def check(arr):
    remove_row = 0
    for i in arr:
        if sum(i) == 4:
            arr.remove(i)
            arr.insert(0, [0, 0, 0, 0])
            remove_row += 1
    return remove_row


# 연한 부분에 블럭이 존재하는지?
def check_top_area(arr):
    if sum(arr[4]) != 0:  # 밑에 2행을 없애야함
        arr.pop()
        arr.pop()
        arr.insert(4, [0, 0, 0, 0])
        arr.insert(4, [0, 0, 0, 0])

    elif sum(arr[5]) != 0:  # 밑에 1행을 없애야함
        arr.pop()
        arr.insert(4, [0, 0, 0, 0])


k = int(input())

yellow_arr = [[0 for _ in range(4)] for _ in range(10)]
red_arr = [[0 for _ in range(4)] for _ in range(10)]
ans = 0
for i in range(k):
    t, x, y = map(int, input().split())  # 블록 타입, x,y

    if t==1: #1번 타입은 노란색은 그대로 두고, 붉은 색을 위해 로테이션 된 좌표가 필요
        yellow_arr[x][y]=1
        red_arr[y][4-x-1]=1
    elif t==2:
        yellow_arr[x][y]=1
        yellow_arr[x][y+1]=1

        red_arr[y][4-x-1]=1
        red_arr[y+1][4-x-1]=1
    else:
        yellow_arr[x][y]=1
        yellow_arr[x+1][y]=1

        red_arr[y][4-x-1]=1
        red_arr[y][4-(x+1)-1]=1

    if t==1:
        move_t1(yellow_arr, x,y)
        move_t1(red_arr, y,4-x-1)

    elif t==2:
        move_t2(yellow_arr, x,y)
        move_t3(red_arr, y, 4-x-1)

    else:
        move_t3(yellow_arr, x, y)
        move_t2(red_arr, y, 4-x-2)

    # 움직인 결과 행이 꽉찬 경우는 행을 삭제하고 위에 배열을 아래로 밀기(고민할 부분 check 전에 연한 부분을 체크하나?)
    ans += check(yellow_arr)
    ans += check(red_arr)

        # 연한 부분 처리
    check_top_area(yellow_arr)
    check_top_area(red_arr)

# 블럭이 차지하는 칸 확인
block_exist = 0
for i in range(4, 10):
    for j in range(4):
        if red_arr[i][j] == 1:
            block_exist += 1
        if yellow_arr[i][j] == 1:
            block_exist += 1

print(ans)
print(block_exist)