import tkinter as tk
from tkinter import *
from PIL import ImageTk

from igraph import *
edges = [(0, 1), (0, 2), (1, 3), (2, 5), (1, 4), (4, 5)]
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
path = []

def bfs(visited, graph, node, goal):
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

def getColors():
    colors = []
    for key in graph:
        print(key)
        if key in path:
            colors.append("green")
        else:
            colors.append("white")

    return colors

def createGraph():
    # Create graph
    g = Graph(directed=True)

    # Add 5 vertices
    g.add_vertices(6)

    names = ["A","B","C","D","E","F"]
    # Add ids and labels to vertices
    for i in range(len(g.vs)):
        g.vs[i]["id"] = i
        g.vs[i]["label"] = names[i]

    # Add edges
    g.add_edges(edges)

    # Add weights and edge labels
    weights = [8, 6, 3, 6, 4, 9]
    g.es['weight'] = weights
    g.es['label'] = weights

    my_layout = g.layout_lgl()

    visual_style = {}

    out_name = "C:\\Users\\Zoey\\Desktop\\graph_coloured.png"

    # Set bbox and margin
    visual_style["bbox"] = (800, 700)
    visual_style["margin"] = 27

    # Set vertex colours
    if len(path) != 0:
        g.vs["color"] = getColors()
    else:
        visual_style["vertex_color"] = 'white'

    # Set vertex size
    visual_style["vertex_size"] = 45

    # Set vertex lable size
    visual_style["vertex_label_size"] = 22

    # Don't curve the edges
    visual_style["edge_curved"] = False

    # Set the layout
    visual_style["layout"] = my_layout

    # Plot the graph
    plot(g, out_name, **visual_style)

def displayGraph():
    createGraph()
    img = ImageTk.PhotoImage(file = "C:\\Users\\Zoey\\Desktop\\graph_coloured.png")
    panel = Label(window, image=img)
    panel.grid(row=0, column=1)
    window.mainloop()

def bfsSearchGraph():
    start = entry1.get()
    end = entry2.get()

    bfs(visited, graph, start, end)

    displayGraph()

def dfsSearchGraph():
    pass

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

fr_buttons.grid(row=0, column=0, sticky="ns")
displayGraph()


