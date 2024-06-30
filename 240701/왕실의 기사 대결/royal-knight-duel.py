from collections import deque
import copy


def move(num, d):
    # move_player_arr = copy.deepcopy(player_arr)
    move_player_arr = [[0 for _ in range(l)]for _ in range(l)]
    r, c, h, w, k = player[num]
    q = deque()
    for i in range(r, r + h):
        for j in range(c, c + w):
            q.append([i, j, num, d])

    move_ok = True
    move_people = set()

    while q:
        x, y, num, d = q.popleft()
        move_people.add(num)
        nx, ny = x + dx[d], y + dy[d]

        # 범위를 벗어난다면 break
        if not (0 <= nx < l and 0 <= ny < l):
            move_ok = False
            break

        # 다음칸이 벽이면
        if board[nx][ny] == 2:
            move_ok = False
            break
        # 다음칸이 빈칸이거나 같은 기사의 칸이고
        elif (player_arr[nx][ny] == num or player_arr[nx][ny] == 0):
            # 이동
            move_player_arr[nx][ny] = num
        # 다음칸이 다른 기사가 있으면
        elif player_arr[nx][ny] != num:
            # 다음칸 기사도 큐에 넣음
            new_player_num = player_arr[nx][ny]
            r, c, h, w, k = player[new_player_num]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    q.append([i, j, new_player_num, d])

            # 이동
            move_player_arr[nx][ny] = num

    # 이동안한 부분도 붙혀넣기
    for num in player.keys():
        if num not in move_people:
            r, c, h, w, k = player[num]

            for i in range(r,r+h):
                for j in range(c,c+w):
                    move_player_arr[i][j]=num

    # 이동 가능하면, 변경된 위치를 리턴한다.
    if move_ok:
        return move_player_arr
    # 이동 불가면 그냥 리턴한다.
    else:
        return move_ok


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
l, n, q = map(int, input().split())  # 체스판 크기, 기사의 수, 명령의 수

board = []
for i in range(l):
    board.append(list(map(int, input().split())))
# print(*board, sep="\n")

player = {}
player_arr = [[0 for _ in range(l)] for _ in range(l)]
for num in range(1, n + 1):
    r, c, h, w, k = map(int, input().split())  # 기사의 처음 위치(r,c), 세로 길이 h, 가로 길이 w, 초기 체력 k
    coordinate = []
    for i in range(r - 1, r - 1 + h):
        for j in range(c - 1, c - 1 + w):
            player_arr[i][j] = num
    player[num] = [r - 1, c - 1, h, w, k]
# print(player)
# print(*player_arr, sep="\n")

damage = 0
for _ in range(q):
    # i번 기사한테 d 방량으로 한칸 이동(이때 이동하려는 위치에 기사가 있으면 연쇄적으로 밀림)
    # 단, 만약 기사가 이동하려는 방향의 끝에 벽이 있으면 모든 기사는 이동 불가
    # i가 체스판에서 사라진 기사면 pass
    i, d = map(int, input().split())  # d는 상,우,하,좌 방향

    if i in player.keys():  # 기사가 있는 지 확인
        new_coordinate = move(i, d)

        # 이동했다면
        if new_coordinate:
            # 함정을 얼마나 밟았는지 확인해서 체력 및 r,c 를 조정해서 딕셔너리도 업데이트
            player_arr = new_coordinate

            not_update_dict = [i]
            # 이동을 시작한 기사는 데미지 없고, 나머지 애들만 데미지를 받는다.
            for o in range(l):
                for j in range(l):
                    num = player_arr[o][j]

                    if num == i:
                        continue

                    # 좌상단의 기사 좌표를 처음 만난 경우
                    if num != 0 and num not in not_update_dict:
                        not_update_dict.append(num)
                        r, c, h, w, k = player[num]

                        # 함정이 있는 경우
                        if board[o][j] == 1:
                            if k-1==0:
                                for _i in range(r, r+h):
                                    for _j in range(c,c+w):
                                        player_arr[_i][_j]=0
                                del player[num]
                            damage += 1
                        # 함정이 없는 경우
                        else:
                            player[num] = [o, j, h, w, k]
                    # 좌상단의 r,c 좌표가 아닌 경우(즉, not_update_dict에 이미 번호가 있는 경우)에는 함정이 있는지만 확인
                    elif num != 0 and num in not_update_dict:
                        r, c, h, w, k = player[num]

                        # 함정이 있는 경우
                        if board[o][j] == 1:
                            if k - 1 == 0:
                                for _i in range(r, r + h):
                                    for _j in range(c, c + w):
                                        player_arr[_i][_j] = 0
                                del player[num]
                            damage += 1

                        # 함정이 없는 경우
                        else:
                            player[num] = [r, c, h, w, k]
        # 이동 못했다면, 넘어감
        else:
            pass

    else:
        pass

print(damage)