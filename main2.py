import json
from typing import List
from entity_grounding import get_grounded_triples, get_images
from extract_triples import extract_entities
from mmkg_construction import add_triples_to_graph, build_graph
from typings import Triple
import os


def load_triples_from_json():
   # load the JSON data from the file
    with open('output_step2_triples_extraction.json', 'r') as f:
        data = json.load(f)

    # create a list of Triple objects from the JSON data
    triples = []
    for item in data:
        triple = Triple(item['subject'], item['relation'], item['object'])
        triples.append(triple)

    return triples


triples = load_triples_from_json()

entities = extract_entities(triples)

grounded_triples = get_grounded_triples(entities)

graph = build_graph(triples)

print(len(graph.nodes))

add_triples_to_graph(graph, grounded_triples)

print(len(graph.nodes))


