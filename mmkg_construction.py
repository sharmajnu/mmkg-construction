import networkx as nx
from typing import List


from typings import Triple



def build_graph(triples: List[Triple]):
    graph = nx.MultiDiGraph()

    for triple in triples:
        graph.add_edge(triple.subject, triple.object, relation=triple.relation)
    
    return graph


def add_triples_to_graph(graph, triples: List[Triple]):
    for triple in triples:
        graph.add_edge(triple.subject, triple.object, relation=triple.relation)
    
    return graph