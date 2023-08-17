# MMKG Construction
## _IIITD_

## Tripple extraction using OpenIE

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
Client code can be found in extract_tripples.py