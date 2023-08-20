# Entity Grounding: Search Engine based Method
from typing import List
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import os

from typings import Triple


def get_images(entity, search_eng):
  path = 'content/images/' + entity

  # create the directory if it doesn't exist
  if not os.path.exists(path):
      os.makedirs(path)

  if search_eng == 'Google':
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={'root_dir': path})

    filters = dict(
        size='medium',
        license='commercial,modify',
        date=((2020, 1, 1), None))

    print('Downloading Images for ' + entity + ':\n')
    google_crawler.crawl(keyword=entity, filters=filters, max_num=1, file_idx_offset=0)
    print()
  
  if search_eng == 'Bing':
    bing_crawler = BingImageCrawler(downloader_threads=4,
                                  storage={'root_dir': path})

    filters = dict(
        size='medium',
        license='commercial,modify')
    
    print('Downloading Images for ' + entity + '\n')
    bing_crawler.crawl(keyword=entity, filters=filters, offset=0, max_num=1)
    print('Image done')


def get_grounded_triples(entities: List[str]) -> List[Triple]:
    grounded_triples = []
    for entity in entities:
        image_dir = os.path.join('content', 'images', entity)
        if os.path.exists(image_dir):
            files = os.listdir(image_dir)
            if len(files) > 0:
                grounded_triple = Triple(entity, 'hasImage', image_dir+ '/'+ files[0])
                grounded_triples.append(grounded_triple)
    return grounded_triples




