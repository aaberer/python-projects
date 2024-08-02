'''
Breadth First and Depth First Search

The objective is to write a Python program that traverses graphs in BFS
and DFS manner. BFS will determine the shortest path distance (number of
edges) from the root for each node reachable from the root. DFS will find
cycles in the graph of nodes reachable from the root. Study the lecture on
graphs, in particular graph traversals.


Some helper code is provided. Don't change it. Don't change your main,
it is used to check your code's correctness. 

It is your job to implement dfs and bfs. In both dfs and bfs, visit 
children of a node in left to right order, i.e., if adj is the
adjacency list of a node, visit the children as follows: for nxt in adj

Given an input file in:

a b
b c
c a d
d c

and root a

python dfbf.py in a produces:


dfbf.py
BFS
Input graph: nodeName (color, [adj list]) dictionary 
a ('white', ['b'])
b ('white', ['c'])
c ('white', ['a', 'd'])
d ('white', ['c'])
Root node: a
BFS queue: (node name, distance) pairs
[('a', 0), ('b', 1), ('c', 2), ('d', 3)]
END BFS

DFS
Input graph: nodeName (color, [adj list]) dictionary 
a ('white', ['b'])
b ('white', ['c'])
c ('white', ['a', 'd'])
d ('white', ['c'])
Root node a
graph with root a is cyclic
END DFS

'''

import sys

cyclic = False #keeping track in dfs whether a cycle was found

def read(fnm):
  """  
  read file fnm into dictionary
  each line has a nodeName followed by its adjacent nodeNames
  """
  f = open(fnm)
  gr = {} #graph represented by dictionary
  for line in f:
    l =line.strip().split(" ")
    # ignore empty lines
    if l==['']:continue
    # dictionary: key: nodeName  value: (color, adjList of names)
    gr[l[0]]= ('white',l[1:]) 
  return gr

def dump(gr):
  print("Input graph: nodeName (color, [adj list]) dictionary ")
  for e in gr:
    print(e, gr[e])

def white(gr) :
  """
   paint all gr nodes white
  """
  for e in gr :
    gr[e] = ('white',gr[e][1])
    

      
'''
  return bfs queue with (node, distance) pairs
'''
def bfs(gr,q):
  """  
  breadth first search gr from r
  """
  seen = {}
  while q:
    node, distance = q.pop(0)
    if node not in seen:
      seen[node] = distance
      for child in gr[node][1]:
        q.append((child, distance + 1))
  return [(node, distance) for node, distance in seen.items()]

'''
  return boolean: True gr bfrom r is cyclic, False otherwise
'''
def dfs(gr,r):
  """  
   depth first search gr from r for cycles
   """
  stack = [(r, None)]
  seen = {}
  while stack:
    node, parent = stack.pop()
    if node not in seen:
      seen[node] = parent
      for child in gr[node][1]:
        if child not in seen:
          stack.append((child, node))
        elif child != parent:
          cyclic = True
          return True
    return False

if __name__ == "__main__":
  print(sys.argv[0])
  gr = read(sys.argv[1])  # file name
  root = sys.argv[2]      # root node
  db = len(sys.argv)>3     # debug?
  
  print("BFS")
  dump(gr)
  print("Root node:", root)
  gr[root] = ('black',gr[root][1])
  q = bfs(gr,[(root,0)])
  print("BFS queue: (node name, distance) pairs")
  print(q)
  print("END BFS")
  print()


  print("DFS")
  white(gr)
  dump(gr)
  print("Root node", root)
  dfsInit(gr,root)
  if cyclic:
    print("graph with root",root,"is cyclic")
  else:
    print("graph with root",root,"is not cyclic")
  print("END DFS")
