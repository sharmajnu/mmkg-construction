from text_extraction import ArticleEncoder, scrape_article
from extract_triples import get_openie_triples
import json


output = scrape_article('http://www.dailymail.co.uk/news/article-3197220/CHRISTOPHER-BOOKER-Lunacy-biggest-white-elephant-Britain.html')

with open('output_step1_text_extraction.json', 'w') as f:
    json.dump(output, f, cls=ArticleEncoder)


triples = get_openie_triples(output.textContent)
with open('output_step2_triples_extraction.json', 'w') as f:
    json.dump(triples, f)








