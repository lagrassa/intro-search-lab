# Adapted from Fall 2020 MIT 6.034 Lab 1: Search
from typing import List, Optional

def distinct(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

class Node:
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"Node({self.name})"

    def __hash__(self):
        return hash(self.name)
        
    def __eq__(self, other):
        return (self.name == other.name)

    def copy(self):
        return Node(self.name)

    def __gt__(self, other):
        return self.name > other.name



class Edge:
    def __init__(self, start_node: Node, end_node: Node):
        self.start_node = start_node
        self.end_node = end_node
        self.length = 1

    def copy(self):
        return Edge(self.start_node, self.end_node)

    def __eq__(self, other):
        return (self.start_node == other.start_node
                and self.end_node == other.end_node
                and self.length == other.length)

    def __str__(self):
        return "Edge<"+",".join([self.start_node, self.end_node, str(self.length)])+">"

    __repr__ = __str__


class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = [Node(node) for node in nodes]
        self.edges = edges[:]

    def is_valid_path(self, path) :
        # all nodes are nodes in the path, and consecutive nodes are neighbors
        return all([x in self.nodes for x in path]) and all([self.get_edge(a,b) for (a,b) in zip(path, path[1:])])

    def set_nodes(self, node_strs : List[str]):
        self.nodes = [Node(node) for node in node_strs]

    def get_edges(self, start_node=None, end_node=None):
        """ Return a list of all the edges in the graph.  If start or end are
        provided, restricts to edges that start/end at particular nodes. """

        pred1 =  lambda node: (start_node is None) or (node == start_node)
        pred2 =  lambda node: (end_node is None)   or (node == end_node)
        return [e for e in [e if pred1(e.start_node) and pred2(e.end_node) else None
             for e in self.edges
        ] if e is not None]

    def get_neighbors(self, node):
        "Returns an alphabetical list of neighboring nodes. Each node appears at most once."
        return sorted(distinct([e.end_node for e in self.get_edges(node)]))

    def get_neighboring_edges(self, start_node):
        "Returns a list of neighboring edges."
        return self.get_edges(start_node)

    def get_edge(self, start_node, end_node):
        """ Returns the edge that directly connects start_node to end_node
        (or None if there is no such edge) """
        edges = self.get_edges(start_node, end_node)
        if len(edges) == 0:
            return None
        else:
            return edges[0]

    def is_neighbor(self, start_node, end_node):
        "Returns True if there is an edge connecting start_node to end_node, else False"
        return any([end_node == e.end_node for e in self.get_edges(start_node)])

    # CREATE AND MODIFY THE GRAPH

    def join(self, start_node_str: str, end_node_str: str, edge_length=None):
        # check whether edge already exists
        start_node = Node(start_node_str)
        end_node = Node(end_node_str)
        if self.is_neighbor(start_node, end_node):
            print("Graph.join: Error adding edge to graph")
            return self
        self.edges.append(Edge(start_node, end_node))
        for node in [start_node, end_node]:
            if node not in self.nodes:
                print("Graph.join: Adding", node, "to list of nodes")
                self.nodes.append(start_node)
        return self

    def copy(self):
        return Graph(self.nodes[:],
                               [e.copy() for e in self.edges])

    def __str__(self):
        return "\n\t".join(["Graph<",
                            "nodes: " + str(self.nodes),
                            "edges: " + str(self.edges),
                            "heuristic: " + str(0)]) + "\n>"
    __repr__ = __str__

        


class Path:
    def __init__(self, edges: list[Edge]):
        self.edges = edges
        self.check_valid_path()

    def check_valid_path(self):
        if not len(self.edges):
            raise RuntimeError("Path needs to contain at least one edge")
        for edge_idx, edge in enumerate(self.edges):
            if edge_idx < len(self.edges)-1: #there is a next edge
                curr_edge = self.edges[edge_idx]
                next_edge = self.edges[edge_idx + 1]
                if not next_edge.start_node == curr_edge.end_node:
                    raise RuntimeError(f"Invalid: edge index {edge_idx} contains an edge where the end node is {curr_edge.end_node} and the start node of the next is {next_edge.start_node}")
        return True

# Change to True for an example of graph creation:
if False:
    g = Graph()
    g.nodes = ["A","B","C","D","E"]
    g.join("A","B",5)
    print(g.get_neighboring_edges("B"))


def do_nothing_fn(graph, goalNode, paths):
    return paths

