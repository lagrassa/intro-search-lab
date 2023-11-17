# MIT 6.034 Lab 1: Search

from search import Graph, Edge, Node, Path

from read_graphs import get_graphs
all_graphs = get_graphs()
GRAPH_0 = all_graphs['GRAPH_0']
GRAPH_1 = all_graphs['GRAPH_1']
GRAPH_2 = all_graphs['GRAPH_2']
GRAPH_3 = all_graphs['GRAPH_3']


def test_path_length(path_length_fn):
    g1_ab_edge = Edge(Node("a"), Node("b"))
    g1_path = Path([g1_ab_edge])
    edge_sa = Edge(Node("s"), Node("a"))
    edge_ac = Edge(Node("a"), Node("c"))
    edge_cy = Edge(Node("c"), Node("y"))
    g2_path = Path([edge_sa, edge_ac, edge_cy])
    assert path_length_fn(g2_path) == 3


def test_neighbors(successors_fn):
    g0_n1n2_edge = Edge(Node("n1"), Node("n2"))
    g0_n1n2_path = Path([g0_n1n2_edge])
    student_successors = successors_fn(GRAPH_0, g0_n1n2_path)
    assert len(student_successors) == 1
    assert student_successors[0].edges[-1].end_node == Node("n3")
    assert len(student_successors[0].edges) == 2 #should include old edge in the path


    g1_ab_edge = Edge(Node("a"), Node("b"))
    g1_path = Path([g1_ab_edge])
    student_successors = successors_fn(GRAPH_1, g1_path)
    assert len(student_successors) == 2
    assert student_successors[0].edges[-1].end_node == Node("c")
    assert student_successors[1].edges[-1].end_node == Node("d")

