nodes = ('monoblock', 'ingenieria', 'derecho', 'cotacota') 
distances = { 
    'monoblock': {'ingenieria': 10, 'derecho': 8, 'cotacota': 25},
    'ingenieria': {'monoblock': 10, 'derecho': 4, 'cotacota': 29}, 
    'derecho': {'monoblock': 8, 'ingenieria': 4, 'cotacota': 27}, 
    'cotacota': {'monoblock': 25, 'ingenieria': 29, 'derecho': 27} 
    } 
import pandas as pd
data = pd.read_csv("data.csv")
print(data['coste'])
unvisited = {node: None for node in nodes} #using None as +inf 
visited = {} 
current = 'monoblock' 
currentDistance = 0 
unvisited[current] = currentDistance 

while True: 
    for neighbour, distance in distances[current].items():
     print(distance)    
     if neighbour not in unvisited: continue 
     newDistance = currentDistance + distance 
     if unvisited[neighbour] is None or unvisited[neighbour] > newDistance: 
      unvisited[neighbour] = newDistance 
    visited[current] = currentDistance 
    del unvisited[current] 
    if not unvisited: break 
    candidates = [node for node in unvisited.items() if node[1]] 
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0] 

print(visited) 