from typing import List
import requests
import json

from typings import Triple

def get_openie_triples(text):
    url = "http://localhost:9000/?properties={\"annotators\": \"tokenize,ssplit,pos,lemma,depparse,natlog,openie\",\"outputFormat\": \"json\"}"
    response = requests.post(url, data=text.encode('utf-8'))
    results = json.loads(response.text)
    
    triples = []
    for sentence in results["sentences"]:
        for openie in sentence["openie"]:
            triple = Triple(openie["subject"], openie["relation"], openie["object"])
            triples.append(triple)
    return triples


def extract_entities(triples: List[Triple]) -> List[str]:
    entities = set()
    for triple in triples:
        entities.add(triple.subject)
        entities.add(triple.object)
    return list(entities)

