import json

class Triple:
    def __init__(self, subject, relation, obj):
        self.subject = subject
        self.relation = relation
        self.obj = obj

class TripleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Triple):
            return {'subject': obj.subject, 'relation': obj.relation, 'object': obj.obj}
        return super().default(obj)
    

class Article:
    def __init__(self, textContent, images):
        self.textContent = textContent
        self.images = images

class Image:
    def __init__(self, imageUrl, caption):
        self.imageUrl = imageUrl
        self.caption = caption

class ArticleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Article):
            return {
                'textContent': obj.textContent,
                'images': [
                    {'imageUrl': image.imageUrl, 'caption': image.caption}
                    for image in obj.images
                ]
            }
        return super().default(obj)
