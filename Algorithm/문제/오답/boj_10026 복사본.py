from collections import deque

def check_color() :
    global cnt, now_color
    while q:
        num = q.popleft()
        i = num[0]
        j = num[1]
        visited[i][j] = 1
        if now_color != colors[i][j]:
            cnt +=1
            now_color = colors[i][j]

        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x >= 0 and x < n and y >= 0 and y < n and visited[x][y] == 0:
                if colors[x][y] == now_color:
                    q.appendleft([x, y])
                else:
                    q.append([x, y])

def color_change():
    global colors
    for i in range(n):
        for j in range(n):
            if colors[i][j] == 'G':
                colors[i][j] = 'R'

n = int(input())
colors = []
for i in range(n):
    color = list(input())
    colors.append((color))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# first
visited = [[0] * n for _ in range(n)]
cnt = 0
q = deque()
q.append([0,0])
now_color = 'N'

check_color()
first_cnt = cnt

# second
color_change()
visited = [[0] * n for _ in range(n)]
cnt = 0
q = deque()
q.append([0,0])
now_color = 'N'

check_color()

print(first_cnt,cnt)



