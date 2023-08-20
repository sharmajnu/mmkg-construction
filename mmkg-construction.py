import networkx as nx
from typing import List


from typings import Triple

graph = nx.MultiDiGraph()


def build_graph(triples: List[Triple]):
    for triple in triples:
        graph.add_edge(triple.subject, triple.object, relation=triple.relation)
        


