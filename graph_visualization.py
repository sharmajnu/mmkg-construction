import networkx as nx
import matplotlib.pyplot as plt

def visualize_knowledge_graph(G: nx.MultiDiGraph):
    """
    Visualize a knowledge graph using networkx and matplotlib.

    Parameters:
    - nodes: A list of node names.
    - edges: A list of edges, where each edge is represented as a tuple (source_node, target_node, relationship_type).
    """


    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(20, 12))

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, width=2, edge_color='gray', arrowsize=20)

    # Draw edge labels
    edge_labels = {(u, v): G[u][v]['relation'] for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.title("Knowledge Graph Visualization")
    plt.show()

    print("Graph is shown")