import os
from entity_grounding import get_grounded_triples, get_images
from graph_visualization import visualize_knowledge_graph
from graph_visualization_with_images import visualize_knowledge_graph_with_images
from image_caption import get_image_captions
from mmkg_construction import add_triples_to_graph, build_graph
from text_extraction import save_images_on_local_folder, scrape_article
from extract_triples import extract_entities, get_openie_triplesz
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


visualize_knowledge_graph_with_images(graph)


print("Graph visualization is done")

#####################################################################################################################################

#Triples Extraction Using NLTK

# import json
# from text_extraction_nltk import scrape_article
# from extract_triples_nltk import extract_entities, get_nltk_triples  

# class Article:
#     def __init__(self, url, textContent, images):
#         self.url = url
#         self.textContent = textContent
#         self.images = images
    
#     def to_dict(self):
#         return {
#             'url': self.url,
#             'textContent': self.textContent,
#             'images': self.images  # No need to call to_dict() on each image dictionary
#         }

# # Custom JSON encoder for Article class
# class ArticleEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Article):
#             return obj.to_dict()
#         return super().default(obj)

# if __name__ == "__main__":
#     # Scraping the article
#     article_url = 'http://www.dailymail.co.uk/news/article-3197220/CHRISTOPHER-BOOKER-Lunacy-biggest-white-elephant-Britain.html'
#     article_data = scrape_article(article_url)

#     # Checking if article_data is in the expected format
#     if isinstance(article_data, dict) and 'textContent' in article_data and 'images' in article_data:
#         article = Article(article_url, article_data['textContent'], article_data['images'])
        
#         # Saving the extracted article text // optional
#         with open('output_article_text.json', 'w') as f:
#             json.dump(article.to_dict(), f, cls=ArticleEncoder, indent=2)

#         # Extracting triples from the text content using NLTK
#         triples = get_nltk_triples(article.textContent)

#         # Saving the extracted triples
#         with open('output_triples.json', 'w') as f:
#             json.dump([triple.to_dict() for triple in triples], f, indent=2)

#         # Optionally extracting entities from the triples and print them
#         entities = extract_entities(triples)
#         print("Extracted Entities:", entities)
#     else:
#         print("Error: Invalid article data format from scrape_article function.")

