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
Reference:  screenshots -> test_case_1 
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

---

**Test Case 3 (Sparse Network)- Input:**
```
Enter width x (e.g., 50): 100
Enter length y (e.g., 50): 100
Enter number of sensor nodes N (e.g., 50): 40
Enter transmission range in meters (e.g., 15): 20
Graph type ('a' for adjacency matrix, 'b' for adjacency list): a
Traversal method ('a' for BFS, 'b' for DFS): b
Enter min data packets: 10
Enter max data packets: 100
```

**Output:**
```
Component 1: Nodes = [0, 39, 3, 12, 35, 26, 2, 7, 6, 1, 36, 33, 17, 23, 31, 22, 34, 25, 29, 16, 27, 30, 28, 21, 38, 19, 9, 4, 14, 37, 15, 24, 20, 8, 11, 18, 10, 5]
Rendezvous Point = Node5
Dijkstra Energy = 7.759448 J
MST Energy = 3.135477 J

Component 2: Nodes = [13]
Rendezvous Point = Node13
Dijkstra Energy = 0.000000 J
MST Energy = 0.000000 J

Component 3: Nodes = [32]
Rendezvous Point = Node32
Dijkstra Energy = 0.000000 J
MST Energy = 0.000000 J

Total Dijkstra Energy = 7.759448 J
Total MST Energy = 3.135477 J
```
```
Reference:  screenshots -> test_case_3
```


---

**Test Case 4 - Input:**
```
Enter width x (e.g., 50): 100
Enter length y (e.g., 50): 100
Enter number of sensor nodes N (e.g., 50): 60
Enter transmission range in meters (e.g., 15): 20
Graph type ('a' for adjacency matrix, 'b' for adjacency list): b
Traversal method ('a' for BFS, 'b' for DFS): a
Enter min data packets: 20
Enter max data packets: 40
```
**Output:**
```
Component 1: Nodes = [0, 4, 8, 26, 38, 56, 1, 12, 18, 40, 46, 20, 57, 30, 10, 17, 29, 34, 58, 15, 19, 6, 21, 35, 49, 50, 14, 48, 55, 2, 37, 52, 3, 7, 13, 23, 24, 39, 16, 27, 41, 45, 47, 11, 22, 51, 59, 9, 36, 42, 25, 28, 32, 54, 5, 43, 44, 53, 31, 33]
Rendezvous Point = Node38
Dijkstra Energy = 6.872407 J
MST Energy = 2.449162 J


Total Dijkstra Energy = 6.872407 J
Total MST Energy = 2.449162 J
```
```
Reference:  screenshots -> test_case_4
```
---

**Test Case 5 - Input:**
```
Enter width x (e.g., 50): 50
Enter length y (e.g., 50): 50
Enter number of sensor nodes N (e.g., 50): 50
Enter transmission range in meters (e.g., 15): 15
Graph type ('a' for adjacency matrix, 'b' for adjacency list): a
Traversal method ('a' for BFS, 'b' for DFS): b
Enter min data packets: 1
Enter max data packets: 100
```
**Output:**
```
Component 1: Nodes = [0, 34, 38, 48, 35, 46, 37, 41, 39, 20, 10, 36, 26, 40, 33, 29, 28, 11, 9, 27, 49, 45, 42, 30, 13, 8, 19, 15, 14, 3, 1, 44, 43, 31, 18, 12, 2, 22, 6, 4, 47, 32, 25, 17, 16, 23, 5, 24, 21, 7]
Rendezvous Point = Node12
Dijkstra Energy = 2.866424 J
MST Energy = 3.462153 J

Total Dijkstra Energy = 2.866424 J
Total MST Energy = 3.462153 J
```
```
Reference:  screenshots -> test_case_5
```

## Energy Comparison Summary
```
Test Case	Total Dijkstra Energy (J)	Total MST Energy (J)	Lower Energy Method

1	        1.996271	                1.288496	             MST
2	        0.354409	                0.477650	             Dijkstra
3	        7.759448	                3.135477	             MST
4	        6.872407	                2.449162	             MST
5	        2.866424	                3.462153	             Dijkstra
```


## MST (Minimum Spanning Tree) - Lower Energy
```
Test Case 1:

Dijkstra Energy = 1.996271 J
MST Energy = 1.288496 J
MST is more energy-efficient.

Test Case 3:

Dijkstra Energy = 7.759448 J
MST Energy = 3.135477 J
MST is more energy-efficient.

Test Case 4:

Dijkstra Energy = 6.872407 J
MST Energy = 2.449162 J
MST is more energy-efficient.
```

## Dijkstra’s Shortest Path - Lower Energy
```
Test Case 2:

Dijkstra Energy = 0.354409 J
MST Energy = 0.477650 J
Dijkstra is more energy-efficient.

Test Case 5:

Dijkstra Energy = 2.866424 J
MST Energy = 3.462153 J
Dijkstra is more energy-efficient.
```

# Summary:

MST (Minimum Spanning Tree): Test Cases 1, 3, and 4 have lower energy consumption with MST.

Dijkstra’s Shortest Path: Test Cases 2 and 5 are more energy-efficient using Dijkstra.


## Did you do the extra credit part?

Yes, the visualizations are structured under test_cases folder

