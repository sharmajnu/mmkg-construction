from networkx import bull_graph
from entity_grounding import get_grounded_triples, get_images
from mmkg_construction import add_triples_to_graph, build_graph
from text_extraction import scrape_article
from extract_triples import extract_entities, get_openie_triples
import json

from typings import ArticleEncoder, Triple, TripleEncoder


output = scrape_article('http://www.dailymail.co.uk/news/article-3197220/CHRISTOPHER-BOOKER-Lunacy-biggest-white-elephant-Britain.html')

with open('output_step1_text_extraction.json', 'w') as f:
    json.dump(output, f, cls=ArticleEncoder)

# Extract triples from the text content
triples = get_openie_triples(output.textContent)
with open('output_step2_triples_extraction.json', 'w') as f:
    json.dump(triples, f, cls=TripleEncoder)

# Extract entities from the triples
entities = extract_entities(triples)

# Download images for each entity
for index, entity in enumerate(entities):
  print('downloading images for ' + str(index) + ' of ' + str(len(entities)))
  get_images(entity, 'Google')

grounded_triples = get_grounded_triples(entities)

graph = build_graph(triples)

print(graph.nodes)

add_triples_to_graph(graph, grounded_triples)













