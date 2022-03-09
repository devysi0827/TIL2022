from collections import deque


def find_me():
    for i in range(n):
        for j in range(m):
            if school_map[i][j] == 'I':
                visited[i][j] = 1
                return [i, j]


n, m = map(int, input().split())
school_map = []
for i in range(n):
    temp_campus = list(input())
    school_map.append(temp_campus)
visited = [[0] * m for _ in range(n)]
my_loca = find_me()
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global cnt

    queue = deque()
    queue.append([my_loca[0], my_loca[1]])

    while queue:
        now = queue.pop()
        x = now[0]
        y = now[1]

        for i in range(4):
            after_x = x + dx[i]
            after_y = y + dy[i]

            if after_x >= 0 and after_x < n and after_y >= 0 and after_y < m and visited[after_x][after_y] == 0 and \
                    school_map[x][y] != 'X':
                queue.append([after_x, after_y])
                visited[after_x][after_y] = 1
                if school_map[after_x][after_y] == 'P':
                    cnt += 1


bfs()

if cnt:
    print(cnt)
else:
    print('TT')