import tkinter as tk
from tkinter import *
from PIL import ImageTk
from igraph import *

# A0 B1 C2 D3 E4 F5 G6 H7
edges = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3),
         (3, 5), (4, 4), (4, 6), (5, 5), (5, 7), (6, 6), (6, 7), (6, 4), (7, 7), (7, 5)]

graph = {
  'A' : ['A','B','C'],
  'B' : ['B', 'D'],
  'C' : ['A','C','E'],
  'D' : ['B','D','F'],
  'E' : ['E','G'],
  'F' : ['F','H'],
  'G' : ['G','H','E'],
  'H' : ['H','F']
}
path = []

def getColors():
    colors = []

    for key in graph:
        if key in path:
            colors.append("green")
        else:
            colors.append("white")
    print(path)
    print(colors)
    return colors

def createGraph():
    # Create graph
    g = Graph(directed=True)

    # Add 5 vertices
    g.add_vertices(8)

    names = ["A","B","C","D","E","F","G","H"]

    # Add ids and labels to vertices
    for i in range(len(g.vs)):
        g.vs[i]["id"] = i
        g.vs[i]["label"] = names[i]

    # Add edges
    g.add_edges(edges)

    # Add weights and edge labels
    weights = [' ', 'RT', 'R', ' ', 'R', 'L', ' ', 'RT', 'L', ' ',
               'RT', ' ', 'L', ' ', 'L', ' ', 'RT', 'R', ' ', 'R']
    g.es['weight'] = weights
    g.es['label'] = weights

    my_layout = g.layout("kk")

    visual_style = {}

    out_name = "graph_coloured.png"

    # Set bbox and margin
    visual_style["bbox"] = (700, 700)
    visual_style["margin"] = 40

    # Set vertex colours
    if len(path) != 0:
        g.vs["color"] = getColors()
    else:
        visual_style["vertex_color"] = 'white'

    # Set vertex size
    visual_style["vertex_size"] = 50

    # Set vertex lable size
    visual_style["vertex_label_size"] = 10

    # Don't curve the edges
    visual_style["edge_curved"] = True

    # Set the layout
    visual_style["layout"] = my_layout

    # Plot the graph
    plot(g, out_name, **visual_style)

def displayGraph():
    createGraph()
    img = ImageTk.PhotoImage(file = "graph_coloured.png")
    panel = Label(window, image=img)
    panel.grid(row=0, column=1)
    text = ''
    text = ''.join(path)
    pathOrder = tk.Label(window, text=text, height=3,width=10 )
    pathOrder.grid(row=1, column=1)
    window.mainloop()

def bfs(visited, graph, node, goal):
  queue = []
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    path.append(s)
    if s == goal:
        break

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def bfsSearchGraph():
    start = entry1.get()
    end = entry2.get()

    global path
    path = []
    visited = []
    bfs(visited, graph, start, end)

    displayGraph()

def dfs(graph, source, goal):
    if source is None or source not in graph:
        return "Invalid input"

    stack = [source]

    while (len(stack) != 0):

        s = stack.pop()

        if s not in path:

            path.append(s)
        elif s in path:

            continue
        if s == goal:
            break

        if s not in graph:
            # leaf node
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)

def dfsSearchGraph():
    start = entry1.get()
    end = entry2.get()

    #visited = []
    global path
    path = []
    dfs(graph, start, end)
    displayGraph()


window = tk.Tk()
window.title("Search graph")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=1000, weight=1)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

label1 = tk.Label(fr_buttons, text="Start Node")
entry1 = tk.Entry(fr_buttons)
label2 = tk.Label(fr_buttons, text="End goal")
entry2 = tk.Entry(fr_buttons)

bfsBtn = tk.Button(fr_buttons, text="breadth first search", command=bfsSearchGraph)
dfsBtn = tk.Button(fr_buttons, text="depth first search", command=dfsSearchGraph)

label1.grid(row=0, column=0, sticky="ew", padx=1, pady=1)
entry1.grid(row=1, column=0, sticky="ew", padx=1, pady=1)
label2.grid(row=3, column=0, sticky="ew", padx=1, pady=1)
entry2.grid(row=4, column=0, sticky="ew", padx=1, pady=1)
bfsBtn.grid(row=6, column=0, sticky="ew", padx=1, pady=20)
dfsBtn.grid(row=7, column=0, sticky="ew", padx=1, pady=20)

fr_buttons.grid(row=0, column=0, sticky="ns")
displayGraph()


