from collections import deque
def neighbors(p):
    x,y=p; return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
def plan(grid, start, goal):
    q=deque([start]); prev={start:None}
    while q:
        p=q.popleft()
        if p==goal: break
        for n in neighbors(p):
            if 0<=n[1]<len(grid) and 0<=n[0]<len(grid[0]) and grid[n[1]][n[0]]==0 and n not in prev:
                prev[n]=p; q.append(n)
    if goal not in prev: return []
    path=[]; p=goal
    while p is not None: path.append(p); p=prev[p]
    return path[::-1]
