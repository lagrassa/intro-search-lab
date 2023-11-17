from search import *
from tests import *
from typing import List
def path_length(path:Path) -> int:
    return len(path.edges)


def successors(graph: Graph, path: Path) -> List[Path]:
    #TODO implement here
    last_edge = path.edges[-1]
    last_node = last_edge.end_node
    node_extensions =  graph.get_neighbors(last_node)
    new_paths = []
    for node in node_extensions:
        old_edges = [edge.copy() for edge in path.edges]
        new_edge = Edge(last_node.copy(), node.copy())
        new_path = Path(old_edges + [new_edge])
        new_paths.append(new_path)
    return new_paths 



#These functions will test your code
#run_path_length_tests()
#test_path_length(path_length)
test_neighbors(successors)
#run_successor_tests()

#Test function
#result = path_reaches_end_node(graph1, my_path, end_node)
#assert(result)


def depth_first_search(graph: Graph, start_node: Node, goal_node: Node)-> Path:
    #TODO fill in the code below for depth-first search
    raise NotImplementedError


def breadth_first_search(graph: Graph, start_node: Node, goal_node: Node) -> Path:
    #TODO fill in the code below for breadth-first search
    raise NotImplementedError


