import matplotlib.pyplot as plt
import networkx as nx

def visualize(nodes, adj, component, rendezvous):
    pos = {node.id: (node.x, node.y) for node in nodes}
    G = nx.Graph()
    for node in component:
        G.add_node(node, pos=(nodes[node].x, nodes[node].y))
    for u, lst in adj.items():
        for v, _, _ in lst:
            if u in component and v in component:
                G.add_edge(u, v)
    
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, node_color='skyblue', with_labels=True)
    # Highlight rendezvous point
    nx.draw_networkx_nodes(G, pos, nodelist=[rendezvous], node_color='red')
    
    labels = {i: f"{nodes[i].data_packets}" for i in component}
    nx.draw_networkx_labels(G, pos, labels=labels)
    plt.title("Sensor Network with Rendezvous Point")
    plt.show()