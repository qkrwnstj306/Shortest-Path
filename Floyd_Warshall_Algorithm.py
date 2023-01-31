import numpy as np
import copy

inf = int(1e10)
# initialize node distance
# 그림 1
node1 = [ [0,1,inf,4,inf,inf],
         [1,0,3,inf,1,inf],
         [inf,3,0,inf,1,2],
         [4,inf,inf,0,1,inf],
         [inf,1,1,1,0,4],
         [inf,inf,2,inf,4,0]
]
# 그림 2

node2 = [
    [0,4,5,inf,inf,inf,inf],
    [4,0,6,5,10,inf,inf],   
    [5,6,0,4,inf,9,inf],
    [inf,5,4,0,6,3,inf],
    [inf,10,inf,6,0,3,2],
    [inf,inf,9,3,3,0,2],
    [inf,inf,inf,inf,2,2,0]
]

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in range(len(graph)):
                if m in path or graph[n][m] == inf or graph[n][m] == 0:
                    continue
                
                stack.append((m, path + [m]))
    return result
def min_path(path,node) :
    sum_list = [] ## path의 cost 계산
    for i in range(len(path)):
        sum = 0
        for j in range(len(path[i])-1):
            sum += node[path[i][j]][path[i][j+1]]
        sum_list += [sum]
    
    return_index = []
    for i in range(len(sum_list)): ## 가장 작은 path의 index return
        if min(sum_list) == sum_list[i]:
            return_index += [i]
    return return_index

def multiple_path(node) : # node의 1부터 print
    
    for i in range(len(node)):
        distance = Floyd_Warshall(node,i)
       
        print("<<<---------------------node {}----------------------->>".format(i+1))
        for j in range(len(node)):
            if i == j :
                continue
            path = dfs_paths(node,i,j) # i+1 -> j+1로 가는 path를 여러 개 만들었다.
            
            min_path_index = []
            min_path_index = min_path(path,node) # 그 여러 개의 path중, 가장 cost가 적은 path의 index를 return
            print(f"[{i+1} -> {j+1}], cost : {distance[j]}")
            
            for z in min_path_index:
                print("\t",end="")
                for q in path[z]:
                    if q == j:
                        print("{}".format(q+1),end="")
                    else :
                        print("{} -> ".format(q+1),end="")
                print("")
    print()
#Floyd-Warshall Algorithm
def Floyd_Warshall(node,start):
    cost = copy.deepcopy(node)
    cost1 = cost.copy()

    for n in range(len(node)):
        cost = cost1.copy()
        for i in range(len(node)):
            for j in range(len(node)):
                if i==j :
                    continue
                if cost[i][j] > cost[i][n] + cost[n][j]:
                    cost1[i][j] = cost[i][n] + cost[n][j]
    start_path = cost1[start].copy()
    
    return start_path
multiple_path(node1)
print("========================================graph2============================================\n")
multiple_path(node2)
    