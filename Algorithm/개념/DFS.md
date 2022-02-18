# DFS

### DFS(Depth First Search)란?

- 그래프 또는 트리를 탐색하며 보다 깊은 것을 우선적으로 하여 최대한 깊게 탐색하는 알고리즘이다. 주로 재귀와 스택을 이용하여 구현을 하며 상세한 알고리즘에 따라 다를 수 있지만, 방문한 곳을 표시하지 않으면 무한루프 등에 빠질 수 있는 위험이 있다.
- 백트래킹을 이용하여 불필요한 방문을 줄이지 않으면 굉장히 많은 시간을 소모할 수 있다.
- 대표적예시로 미로탐색인데, 코딩테스트 같은 경우 어떠한 경우의 수를 찾는 문제들과 연관되어 나올 때가 많다. 



### DFS의 작동원리

![img (1)](/home/seil/Desktop/TIL2022/Algorithm/개념/DFS.assets/img (1).gif)

- 시작노드를 지정 및 시작노드를 스택에 넣는다. 

  - stack = [1]

- 시작노드와 연결된 모든 노드를 찾고 스택에 넣는다. 

  - visit 1, new stack= [2,5,8] ,

- 가장 먼저 등록된 2와 연결된 노드를 찾고 이 가장 깊은 곳 까지 탐색을 진행한다.

  - visit 2, new stack = [3]
  - visit 3, new stack = [4]
  - visit 4, new stack = []

- 모든 탐색을 완료하면 기존의 스택으로 돌아와서 방문하지 않은 나머지 스택을 방문한다.

  - back stack = [2,5,8]
  - visit 5, new stack = [6,8]
  - visit 6, new stack = [7]
  - back stack = [6,8]
  - visit 8, new stack = []
  - back stack=[6,8] 모두 방문하였으므로 한 번 더 돌아간다.
  - back stack = [2,5,8]
  - 8에 대해서 위와 같은 과정을 진행

  .......

### Code

위에 원리를 이용하여 코드를 작성한다.

```python
d_check = [False for _ in range(n + 1)]
def dfs(x):
    d_check[x] = True
    print(x, end = ' ')
    for y in edge[x]:
        if d_check[y] == False:
            dfs(y)
```

이 코드는 dfs의 가장 기본적인 재귀 코드로, 아래 gif와 같은 노드가 있다면 1~10이 순서대로 프린트가 된다.

