import random
from visualize import visualize
from energy_consumption import generate_graph, find_components, prim, total_energy_dijkstra, total_energy_mst

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