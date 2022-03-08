from collections import deque
n, m = map(int, input().split())

school_map = []
for i in range(n):
    temp_campus = list(input())
    school_map.append(temp_campus)

visited = [[0] * m for _ in range(n)]# error


def find_me():
    for i in range(n):
        for j in range(m):
            if school_map[i][j] == 'I':
                visited[i][j] =1
                return [i,j]
my_loca = find_me()

count = 0
stack = []

def bfs() :
    queue = deque()
    queue.append([my_loca[0],my_loca[1]])
    global count


    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        visited[x][y] =1
        if school_map[x][y] == 'P':
            count += 1
        elif school_map[x][y] == 'X':
            return

        if x - 1 >= 0 and visited[x - 1][y] == 0:
            queue.append([x-1,y])
        if x + 1 < n and visited[x + 1][y] == 0:
            queue.append([x+1,y])
        if y - 1 >= 0 and visited[x][y - 1] == 0:
            queue.append([x,y-1])
        if y + 1 < m and visited[x][y + 1] == 0:
            queue.append([x,y+1])


bfs()

if count == 0:
    print('TT')
else:
    print(count)
