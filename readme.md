# MMKG Construction
## _IIITD_

## Text extraction

In this project we are using the ION Corpus dataset. It is composed of news articles from 5 different online
news portals like The New York Times and The Daily Mail. For a particular article, we are
extracting the article text along with the image-caption pairs from the URLs listed in the dataset
using the Python-based HTML parsing library, BeautifulSoup. The article text serves as the
input for the base knowledge graph, the image is used for scene graph generation, while the
captions are expected to serve as the link between the two separate graphs thus obtained.

## Triple extraction using OpenIE

OpenIE (Open Information Extraction) is a technique that automatically extracts structured information from unstructured text in the form of triples: (Subject, Relation, Object). The Stanford NLP group offers a popular implementation of OpenIE.

To generate triples using OpenIE for a text paragraph in Python, following steps are used:

### 1. Setting up StanfordNLP:
- Download the Stanford CoreNLP suite from the official [Stanford NLP downloads page](https://stanfordnlp.github.io/CoreNLP/download.html).
- Extract the downloaded file to a directory, say ./stanford-corenlp.
### 2. Run Stanford CoreNLP as a server:
- Navigate to the stanford-corenlp directory.
- Start the server with OpenIE enabled:
```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```

### 3. Client code to extract triples
Client code can be found in extract_triples.py