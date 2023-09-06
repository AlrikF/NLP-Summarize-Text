import sys
from collections import deque

def graph_dfs(graph,curr_node,end,visited, curr_val ):
    if curr_node== end:
        ans =max(ans, curr_val)
    else:
        for new_node in graph[curr_node]:
            if new_node not in visited:
                graph_dfs(graph, new_node, end, visited.add(new_node), curr_val*graph[curr_node][new_node])
                visited.discard(new_node)
    return 


    



if __name__ == '__main__':
    inp_arr = []
    # for line in sys.stdin:
    #     inp_arr.append(line.strip())
        
    print("Running")
    

    inp_arr[0]= "USD,JPY,110;USD,AUD,1.45;JPY,GBP,0.0070"
    inp_arr[1]='GBP'
    inp_arr[2]='AUD'
    start = inp_arr[1]
    end   = inp_arr[2]
    conversions = inp_arr[0].split(';')
    graph={}



    for conv in conversions:
        c1, c2, rate = conv.split(',')
        gphc1 = graph.get(c1, {})
        gphc1[c2]= rate
        graph[c1]= gphc1

        gphc2 = graph.get(c2, {})
        gphc2[c1]= rate
        graph[c2]= gphc2

    visited = set([])
    q = deque()
    q.append([start,1])
    ans=1

    print("Graph",graph)
    graph_dfs(graph,start,end, visited, 1)

    print(ans)