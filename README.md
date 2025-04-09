#  Sensor Network Energy Comparison using Dijkstra and Prim's MST

This project simulates a wireless sensor network to compare energy consumption when transmitting data using two popular graph algorithms:

- **Dijkstra’s Shortest Path Tree (SPT)**
- **Prim’s Minimum Spanning Tree (MST)**

Each sensor node generates a random amount of data and communicates with a selected **rendezvous node**. The goal is to evaluate total energy usage based on the structure of the network and the routing strategy used.

---

##  Features

- Random sensor node generation on a 2D field
- Customizable network size, number of nodes, and transmission range
- Graph generation using either Adjacency Matrix or Adjacency List
- Traversal using BFS or DFS to find connected components
- Energy computation for:
  - **Shortest Path Tree (Dijkstra)**
  - **Minimum Spanning Tree (Prim)**
- Network visualization with clear node labels and structure using matplotlib

---

## Requirements
- Python 3.13.2
- Required libraries:
  - `networkx`
  - `matplotlib`

Install missing libraries using:
```sh
pip install networkx matplotlib
```

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the script using:
```sh
python sensors.py
```

## Example Input & Output
**Test Case 1 (Dense Network)- Input:**
```
Enter width x (e.g., 50): 50
Enter length y (e.g., 50): 50
Enter number of sensor nodes N (e.g., 50): 40
Enter transmission range in meters (e.g., 15): 15
Graph type ('a' for adjacency matrix, 'b' for adjacency list): a
Traversal method ('a' for BFS, 'b' for DFS): b
Enter min data packets: 1
Enter max data packets: 50
```
**Output:**
```
Component 1: Nodes = [0, 38, 39, 30, 37, 36, 23, 12, 8, 7, 29, 18, 4, 22, 20, 1, 15, 10, 3, 31, 28, 24, 16, 13, 9, 35, 34, 33, 32, 27, 26, 25, 21, 19, 17, 14, 11, 6, 5, 2]
Rendezvous Point = Node25
Dijkstra Energy = 1.996271 J
MST Energy = 1.288496 J

Total Dijkstra Energy = 1.996271 J
Total MST Energy = 1.288496 J
```

```
Reference:  screenshots -> test_case_1 -> figure_1_component.png
```

---

**Test Case 2 (Dense Network)- Input:**
```
Enter width x (e.g., 50): 50
Enter length y (e.g., 50): 50
Enter number of sensor nodes N (e.g., 50): 20
Enter transmission range in meters (e.g., 15): 10
Graph type ('a' for adjacency matrix, 'b' for adjacency list): b
Traversal method ('a' for BFS, 'b' for DFS): a
Enter min data packets: 10
Enter max data packets: 40
```


**Output:**
```
Component 1: Nodes = [0, 10]
Rendezvous Point = Node0
Dijkstra Energy = 0.009891 J
MST Energy = 0.034949 J

Component 2: Nodes = [1, 11, 12, 15, 16, 6, 7, 14, 9, 3, 4]
Rendezvous Point = Node7
Dijkstra Energy = 0.268796 J
MST Energy = 0.351662 J

Component 3: Nodes = [2, 5]
Rendezvous Point = Node5
Dijkstra Energy = 0.012231 J
MST Energy = 0.018668 J

Component 4: Nodes = [8, 13, 17]
Rendezvous Point = Node17
Dijkstra Energy = 0.063491 J
MST Energy = 0.072371 J

Component 5: Nodes = [18]
Rendezvous Point = Node18
Dijkstra Energy = 0.000000 J
MST Energy = 0.000000 J

Component 6: Nodes = [19]
Rendezvous Point = Node19
Dijkstra Energy = 0.000000 J
MST Energy = 0.000000 J

Total Dijkstra Energy = 0.354409 J
Total MST Energy = 0.477650 J
```

```
Reference:  screenshots -> test_case_2
```