#graph basic operations implementation
#library to create and manage enum in python
#this will be useful for "visited" and "unvisited" nodes
from enum import Enum

class Node:
    def __init__(self,value):
        self.value = value
        
class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertices(self,node,vert):
        self.adj_list[node.value] = vert
        
    def PrintGraph(self,n1,visited =None):
        current = self.adj_list[n1]
        if visited == None:
            visited = set()
        
        visited.add(n1)
        print(current)
        for i in set(current) - visited:
            self.PrintGraph(i,visited)
        
        return visited
            
    
    
             
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

g = Graph()
g.add_vertices(n1,[20,40])
g.add_vertices(n2,[10,30])
g.add_vertices(n3,[20])
g.add_vertices(n4,[10,30])

g.PrintGraph(n1.value)
        