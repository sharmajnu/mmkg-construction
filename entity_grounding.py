# Entity Grounding: Search Engine based Method
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler

def get_images(entity, search_eng):
  path = '/content/Images/' + entity

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
    print()