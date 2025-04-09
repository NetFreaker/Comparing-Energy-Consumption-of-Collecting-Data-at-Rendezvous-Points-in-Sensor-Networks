import random
import math
import heapq
import matplotlib.pyplot as plt
import networkx as nx

# Constants for Energy Calculation
E_ELEC = 1e-7  # 100 nJ/bit
E_AMP = 1e-10  # 100 pJ/bit/m^2
PACKET_SIZE = 3200  # bits per packet

# Node class to store information about each sensor node
class SensorNode:
    def __init__(self, id, x, y, data_packets):
        self.id = id
        self.x = x
        self.y = y
        self.data_packets = data_packets

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"Node{self.id}(Packets: {self.data_packets})"

# Energy function

def energy_cost(k, l):
    et = E_ELEC * k + E_AMP * k * l ** 2
    er = E_ELEC * k
    return et + er

# Graph generation

def generate_graph(width, length, N, Tr, data_range):
    nodes = []
    for i in range(N):
        x, y = random.uniform(0, width), random.uniform(0, length)
        data_packets = random.randint(data_range[0], data_range[1])
        nodes.append(SensorNode(i, x, y, data_packets))

    adj = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N):
            d = nodes[i].distance_to(nodes[j])
            if d <= Tr:
                cost = energy_cost(PACKET_SIZE, d)
                adj[i].append((j, cost, d))
                adj[j].append((i, cost, d))
    return nodes, adj

# BFS/DFS to find connected components

def find_components(adj, method='bfs'):
    visited = set()
    components = []

    def bfs(start):
        q = [start]
        comp = []
        visited.add(start)
        while q:
            node = q.pop(0)
            comp.append(node)
            for neighbor, _, _ in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return comp

    def dfs(start):
        stack = [start]
        comp = []
        visited.add(start)
        while stack:
            node = stack.pop()
            comp.append(node)
            for neighbor, _, _ in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return comp

    for i in adj:
        if i not in visited:
            if method == 'bfs':
                components.append(bfs(i))
            else:
                components.append(dfs(i))

    return components

# Dijkstra for Shortest Path Tree

def dijkstra(adj, start):
    dist = {start: 0}
    pq = [(0, start)]
    prev = {}
    while pq:
        d, u = heapq.heappop(pq)
        for v, cost, _ in adj[u]:
            if v not in dist or d + cost < dist[v]:
                dist[v] = d + cost
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

# Prim for Minimum Spanning Tree

def prim(adj, start):
    visited = set([start])
    edges = []
    pq = []
    for v, cost, _ in adj[start]:
        heapq.heappush(pq, (cost, start, v))

    while pq:
        cost, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            edges.append((u, v, cost))
            for next_v, next_cost, _ in adj[v]:
                if next_v not in visited:
                    heapq.heappush(pq, (next_cost, v, next_v))
    return edges

# Energy calculation for Dijkstra

def total_energy_dijkstra(nodes, adj, component, rendezvous):
    dist, prev = dijkstra(adj, rendezvous)
    total = 0
    for node in component:
        if node == rendezvous:
            continue
        path = []
        u = node
        while u != rendezvous:
            v = prev[u]
            d = next(d for n, _, d in adj[u] if n == v)
            total += nodes[u].data_packets * energy_cost(PACKET_SIZE, d)
            u = v
    return total

# Energy calculation for MST

def total_energy_mst(nodes, mst_edges):
    total = 0
    for u, v, cost in mst_edges:
        total += nodes[u].data_packets * cost
        total += nodes[v].data_packets * cost
    return total

# Visualization

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

# Main Program
if __name__ == '__main__':
    width = int(input("Enter width x (e.g., 50): "))
    length = int(input("Enter length y (e.g., 50): "))
    N = int(input("Enter number of sensor nodes N (e.g., 50): "))
    Tr = float(input("Enter transmission range in meters (e.g., 15): "))
    graph_type = input("Graph type ('a' for adjacency matrix, 'b' for adjacency list): ")
    traversal = input("Traversal method ('a' for BFS, 'b' for DFS): ")
    min_packets = int(input("Enter min data packets: "))
    max_packets = int(input("Enter max data packets: "))

    nodes, adj = generate_graph(width, length, N, Tr, (min_packets, max_packets))
    components = find_components(adj, method='bfs' if traversal == 'a' else 'dfs')

    total_dijkstra = 0
    total_mst = 0

    for i, comp in enumerate(components):
        rendezvous = random.choice(comp)
        mst_edges = prim(adj, rendezvous)
        dijkstra_energy = total_energy_dijkstra(nodes, adj, comp, rendezvous)
        mst_energy = total_energy_mst(nodes, mst_edges)
        total_dijkstra += dijkstra_energy
        total_mst += mst_energy
        print(f"\nComponent {i+1}: Nodes = {comp}")
        print(f"Rendezvous Point = Node{rendezvous}")
        print(f"Dijkstra Energy = {dijkstra_energy:.6f} J")
        print(f"MST Energy = {mst_energy:.6f} J")
        visualize(nodes, adj, comp, rendezvous)

    print(f"\nTotal Dijkstra Energy = {total_dijkstra:.6f} J")
    print(f"Total MST Energy = {total_mst:.6f} J")
