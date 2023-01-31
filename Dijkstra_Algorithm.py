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
##Dijkstra's algorithm
# distance list, visit list, stack 
# 1. initialize : start 노드 stack에 저장, distance 초기화
# 2. node 찾기 -> cost가 가장 적은 노드 선택, stack에 저장
# 3. ->j path를 찾을껀데, min[Dj,Di + dij] (여기서 i는 내가 선택한 노드)
# 4. 2~3번 반복

##Dijkstra's algorithm
# distance list, visit list, stack 
# 1. initialize : start 노드 stack에 저장, distance 초기화
# 2. node 찾기 -> cost가 가장 적은 노드 선택, stack에 저장
# 3. ->j path를 찾을껀데, min[Dj,Di + dij] (여기서 i는 내가 선택한 노드)
# 4. 2~3번 반복

def dijkstra(node,start):
    visit = [start] # 방문하면 저장 -> 재방문 방지 목적
    distance = node[start].copy() 
    while(True): #모든 노드가 visit에 들어오면 끝
        temp = inf
        temp_index = -1
    
        
        for i in range(len(node)): # 
            if i in visit: # 방문한 노드면? 
                continue

             #갈 수 있는 노드 중 가장 작은 노드 선택하자
            if temp > distance[i]:
                temp = distance[i]
                temp_index = i

        if len(visit) == len(node):
            break
        if temp_index != -1:
            visit += [temp_index] # 방문했다고 가정.
            for j in range(len(node)):
                if j in visit:
                    continue
                if(distance[j]>distance[temp_index]+ node[temp_index][j]):
                    distance[j] = distance[temp_index]+ node[temp_index][j]
    return distance

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
        distance = dijkstra(node,i)
        #print(distance)
        print("<<<---------------------node {}----------------------->>".format(i+1))
        for j in range(len(node)):
            if i == j :
                continue
            path = dfs_paths(node,i,j) # i+1 -> j+1로 가는 path를 여러 개 만들었다
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
multiple_path(node1)
print("========================================graph2============================================\n")
multiple_path(node2)