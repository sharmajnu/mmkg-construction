import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image
import networkx as nx

def visualize_knowledge_graph_with_images(G: nx.MultiDiGraph):
    """
    Visualize a knowledge graph using networkx and matplotlib.

    Parameters:
    - G: A networkx MultiDiGraph object representing the knowledge graph.
    """

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(20, 12))

    # Draw nodes
    image_nodes = [node for node in G.nodes() if str(G.nodes[node]).startswith('content/images')]
    non_image_nodes = [node for node in G.nodes() if node not in image_nodes]

    # Draw non-image nodes
    nx.draw_networkx_nodes(G, pos, nodelist=non_image_nodes, node_size=3000, node_color='skyblue', alpha=0.8)

    # Draw image nodes
    for node in image_nodes:
        image_url = str(G.nodes[node])
        with urllib.request.urlopen(image_url) as url:
            image = Image.open(url)
            image_array = np.asarray(image)
            plt.imshow(image_array, extent=[pos[node][0]-0.1, pos[node][0]+0.1, pos[node][1]-0.1, pos[node][1]+0.1])

    # Draw edges
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray', arrowsize=20)

    # Draw node labels
    node_labels = {node: node for node in non_image_nodes}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=15)

    # Draw edge labels
    edge_labels = {(u, v): G[u][v]['relation'] for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

    plt.title("Knowledge Graph Visualization")
    plt.show()

    print("Graph is shown")
