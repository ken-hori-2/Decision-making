import networkx as nx
import plotly.graph_objects as go

G = nx.Graph()

# Define nodes and edges
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Add node_info for customdata
G.nodes[1]["node_info"] = {
    "name": "node-1",
    "id": 1,
    "description": "This is the test node 1",
}
G.nodes[2]["node_info"] = {
    "name": "node-2",
    "id": 2,
    "description": "This is the test node 2",
}
G.nodes[3]["node_info"] = {
    "name": "node-3",
    "id": 3,
    "description": "This is the test node 3",
}

# Get node positions
pos = nx.spring_layout(G, k=0.3, seed=1)

# Set node positions
for node in G.nodes():
    G.nodes[node]["pos"] = pos[node]

# Create a node trace
node_x = []
node_y = []
node_info = []
for n in G.nodes():
    x, y = G.nodes[n]["pos"]
    node_x.append(x)
    node_y.append(y)
    node_info.append(G.nodes[n]["node_info"])
nodes = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers",
    marker=dict(size=20, line=dict(width=2)),
    customdata=node_info,
)

# Create a edge trace
edge_x = []
edge_y = []
for e in G.edges():
    x0, y0 = G.nodes[e[0]]["pos"]
    x1, y1 = G.nodes[e[1]]["pos"]
    edge_x.append(x0)
    edge_y.append(y0)
    edge_x.append(x1)
    edge_y.append(y1)
    edge_x.append(None) 
    edge_y.append(None) 
edges = go.Scatter(x=edge_x, y=edge_y, mode="lines", line=dict(width=2))

# Create a figure from nodes and edges
fig = go.Figure(
    data=[edges, nodes],
    layout=go.Layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        clickmode="select+event",
    ),
)

fig = go.Figure(data=[edges, nodes])
fig.write_html("../MAZE_GRID/algorism/meeting0401/file.html", auto_open=False)
G.edges