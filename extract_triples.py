import requests
import json

def get_openie_triples(text):
    url = "http://localhost:9000/?properties={\"annotators\": \"tokenize,ssplit,pos,lemma,depparse,natlog,openie\",\"outputFormat\": \"json\"}"
    response = requests.post(url, data=text.encode('utf-8'))
    results = json.loads(response.text)
    
    triples = []
    for sentence in results["sentences"]:
        for openie in sentence["openie"]:
            triple = {
                "subject": openie["subject"],
                "relation": openie["relation"],
                "object": openie["object"]
            }
            triples.append(triple)
    return triples

