import pandas as pd
import networkx as nx
from pyvis.network import Network

df = pd.read_csv('data.csv')

X = nx.Graph()

X2 = Network(height="1500px", width="100%", bgcolor="#222222", font_color="white")

# set the physics layout of the network
X2.barnes_hut()
X2.from_nx(X)

Origins = df['Origin']
Destinations = df['Dest']
Weights = df['Distance']

edge_data = zip(Origins, Destinations, Weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    X2.add_node(src, src, title=src, color="#03DAC6", shape="triangle")
    X2.add_node(dst, dst, title=dst, color="#da03b3", shape="box")
    X2.add_edge(src, dst, value=w, color="#018786", label=w)

    X2.set_edge_smooth("dynamic")

#neighbor_map = G2.get_adj_list()

# add neighbor data to node hover data
# for node in G2.nodes:
#     node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
#     node['value'] = len(neighbor_map[node['id']])


X2.show("Assign.html")
