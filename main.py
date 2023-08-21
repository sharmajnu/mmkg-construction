import os
from networkx import bull_graph
from entity_grounding import get_grounded_triples, get_images
from image_caption import get_image_captions
from mmkg_construction import add_triples_to_graph, build_graph
from text_extraction import save_images_on_local_folder, scrape_article
from extract_triples import extract_entities, get_openie_triples
import json

from typings import ArticleEncoder, Triple, TripleEncoder


article = scrape_article('http://www.dailymail.co.uk/news/article-3197220/CHRISTOPHER-BOOKER-Lunacy-biggest-white-elephant-Britain.html')

with open('output_step1_text_extraction.json', 'w') as f:
    json.dump(article, f, cls=ArticleEncoder)

save_images_on_local_folder(article.images)


# Extract triples from the text content
triples = get_openie_triples(article.textContent)
with open('output_step2_triples_extraction.json', 'w') as f:
    json.dump(triples, f, cls=TripleEncoder)

# Extract entities from the triples
entities = extract_entities(triples)

# Download images for each entity
# for index, entity in enumerate(entities):
#   print('downloading images for ' + str(index) + ' of ' + str(len(entities)))
#   get_images(entity, 'Google')

grounded_triples = get_grounded_triples(entities)

graph = build_graph(triples)

print(graph.nodes)

add_triples_to_graph(graph, grounded_triples)

images = []
for image in os.listdir('article/images'):
  path = 'article/images/' + image
  if os.path.isfile(path):
     images.append(path)

captions = get_image_captions(images)

#  Add image captions to the graph generated from the image summarization
for caption in captions:
  triples = get_openie_triples(caption)
  add_triples_to_graph(graph, triples)


# Add images from the caption downloaded from the article
for image in article.images:
  triples = get_openie_triples(image.caption)
  add_triples_to_graph(graph, triples)
















