# 0=HMY, 1=JXY, 2=WHM, 3=WTH
game = [
    [2,3], [2,3], [2,1], [1,2], [2,1], [2,1], \
    [2,1], [1,2], [1,2], [3,0], [3,0], [1,3], [3,1], [1,3], [1,3], \
    [2,3], [2,1], [0,3], [1,3], [0,2], \
    [3,1], [3,1], [0,2], [2,0], [2,0], [1,0], [3,2], [3,2], [2,3], [2,3], [2,3], \
    [3,2], [2,3], [2,3], [0,1], [1,0], [1,0], [3,0], [1,2], [1,2], [2,1], [2,1], [2,1], \
    [3,1], [3,1], [0,2], [2,0], [2,0], [1,0], [3,2], [2,3], [3,2], [3,2], \
    [3,0], [3,0], [2,1], [1,2], [2,1], [0,1], [2,3], [3,2], [3,2], [3,2], \
    [0,2], [1,3], [2,1], [0,3], [2,3], [1,0], \
    [1,3], [2,3], [3,0], [2,1], [2,0], [1,0], \
    [1,2], [2,1], [1,2], [3,0], [0,3], [0,3], [2,3], [1,0], [1,0], [1,0], \
    [2,3], [2,3], [0,1], [1,0], [1,0], [0,3], [2,1], [2,1], [1,2], [2,1], \
    [1,0], [3,2], [2,0], [3,1], [1,2], [3,0], \
    [3,0], [2,1], [1,2], [3,0], \
    [2,0], [2,0], [3,1], [1,3], [3,1], [1,0], [3,2], [3,2], [3,2], \
    [3,1], [1,3], [3,1], [3,2], [2,3], [2,3], \
    [3,1], [3,2], [1,2], \
    [2,0], [0,2], [2,0], [3,1], [3,1], [1,0], [3,2], [2,3], [3,2], [3,2], \
    [1,0], [1,0], [3,2], [3,2], [2,0], [3,1], [3,1], [1,3], [3,1], \
    [3,2], [1,3], [2,1], [1,3], [3,2], [2,1],\
    [0,3], [3,0], [3,0] ,[2,1], [1,2], [1,2], [2,0], [3,1], [1,3], [1,3], [3,1], [1,3],\
    [0,1], [1,0], [0,1], [2,3], [3,2], [2,3], [1,3], [2,0], [2,0], [2,0],\
    [3,1], [2,3], [2,1],\
    [1,3], [2,1], [3,2], [1,2],\
    [3,0], [3,0], [2,1], [1,2], [1,2], [0,2], [1,3], [3,1], [1,3], [1,3], \
    [3,2], [2,3], [3,2], [0,1], [0,1], [2,1], [3,0], [3,0], [3,0], \
    [0,2], [2,0], [2,0], [1,3], [3,1], [3,1]
]

record = [[0 for _ in range(4)] for _ in range(4)]
continue_win = [0 for _ in range(4)]
continue_lose = [0 for _ in range(4)]

for g in game:
    record[g[0]][g[1]] += 1
    
    continue_win[g[0]] += 1
    continue_lose[g[1]] += 1

    if continue_lose[g[0]] >= 5:
        print('player %d %d continue lose'%(g[0], continue_lose[g[0]]))
    if continue_win[g[1]] >= 5:
        print('player %d %d continue win'%(g[1], continue_win[g[1]]))
    
    continue_lose[g[0]] = 0
    continue_win[g[1]] = 0

print('relative record:')
for i in range(4):
    for j in range(4):
        print(record[i][j], end=' ')
    print()

p_record = [[0 for _ in range(2)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        p_record[i][0] += record[i][j]
        p_record[j][1] += record[i][j]

win_rate = [0 for _ in range(4)]
max_win_rate = 0
max_record = [0 for _ in range(2)]
for i in range(4):
    win_rate[i] = p_record[i][0]/(p_record[i][0]+p_record[i][1])
    if win_rate[i] > max_win_rate:
        max_record = p_record[i]
        max_win_rate = win_rate[i]

win_deviation = [0 for _ in range(4)]
for i in range(4):
    win_deviation[i] = ((max_record[0]-max_record[1])-(p_record[i][0]-p_record[i][1]))/2

print('personal record:')
for i in range(4):
    print('player %d: %d %d-%d %d-%d %.2f %.1f'%(i, (p_record[i][0]+p_record[i][1]),\
                                                 p_record[i][0], p_record[i][1],\
                                                 continue_win[i], continue_lose[i],\
                                                 win_rate[i], win_deviation[i]))
# print(len(game))