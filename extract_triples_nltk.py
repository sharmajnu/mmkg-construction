from typing import List
import nltk
from nltk import pos_tag, word_tokenize, sent_tokenize, RegexpParser

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

class Triple:
    def __init__(self, subject, relation, object):
        self.subject = subject
        self.relation = relation
        self.object = object

    def to_dict(self):
        return {
            'subject': self.subject,
            'relation': self.relation,
            'object': self.object
        }

def get_nltk_triples(text: str) -> List[Triple]:
    sentences = sent_tokenize(text)
    triples = []

    for sentence in sentences:
        words = word_tokenize(sentence)
        pos_tags = pos_tag(words)
        
        grammar = r"""
            NP: {<DT>?<JJ>*<NN.*>}
            VP: {<VB.*>}
        """
        
        chunker = RegexpParser(grammar)
        tree = chunker.parse(pos_tags)
        
        subject, verb, obj = "", "", ""
        
        for subtree in tree:    
            if isinstance(subtree, nltk.Tree):
                if subtree.label() == 'NP' and not subject:
                    subject = " ".join(word for word, pos in subtree.leaves())
                elif subtree.label() == 'VP':
                    verb = " ".join(word for word, pos in subtree.leaves())
                elif subtree.label() == 'NP' and subject and verb:
                    obj = " ".join(word for word, pos in subtree.leaves())
                    triples.append(Triple(subject, verb, obj))
                    subject, verb, obj = "", "", ""

    return triples

def extract_entities(triples: List[Triple]) -> List[str]:
    entities = set()
    for triple in triples:
        entities.add(triple.subject)
        entities.add(triple.object)
    return list(entities)
