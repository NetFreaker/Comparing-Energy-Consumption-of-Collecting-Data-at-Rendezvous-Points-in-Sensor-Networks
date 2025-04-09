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
