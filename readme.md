# MMKG Construction

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


## Representing Knowledge Graph

We are building the knowledge graph with the extracted triples using Python networkx library, the code can be found in the mmkg_construction.py file

## Symbol Grounding

Entity Grounding for MMKG Construction
Once we’ve constructed the KG from the article text, we ground all the entities identified in the
KG to their corresponding images, so that each entity can be better described using more than
one modality. To achieve entity grounding, we use the Python-based icrawler package [6]. The
crawlers are composed of:
1. Feeder: To identify relevant page URLs for specified keywords under specified filters
2. Parser: To parse the corresponding pages and extract the image URLs
3. Downloader: To request the images identified and save them
We use the Search Engine based method of grounding. This can be achieved via the builtin
crawlers like GoogleImageCrawler and BingImageCrawler, as specified in the program. The
crawler takes the entity label as its keyword, filters for images which are medium-sized, published
within a certain timeline if possible, and labelled for reuse with modification, and downloads
the topmost relevant image. This image is then used to represent the entity in the graph.


## Image Captioning with pre-trained model

Image captioning is the process of generating a textual description of an image. It is a challenging task that requires both computer vision and natural language processing techniques. The goal of image captioning is to automatically generate a caption that accurately describes the content of an image.

In recent years, deep learning techniques have been used to develop image captioning models that can generate captions that are both accurate and descriptive. These models typically consist of two main components: an image encoder and a language decoder.

The image encoder is a convolutional neural network (CNN) that is trained to extract features from an input image. The output of the image encoder is a fixed-length vector that represents the content of the image.

The language decoder is a recurrent neural network (RNN) that is trained to generate a sequence of words that describe the content of the image. The decoder takes the output of the image encoder as input and generates a sequence of words one at a time. At each time step, the decoder uses the output from the previous time step as input to generate the next word in the sequence.

We are using nlpconnect/vit-gpt2-image-captioning pre-trained model to generate image captioning for the images found in the article. 

Following are the steps used.

1. Generate image caption with the pre-trained model
2. Extract triples from the image caption using the OpenIE 
3. Expand MMKG with the triples
4. We are also extending the knowledge graph with the image caption provided in the article with same steps

## Visualization

The graph visualization is done with the python networkx library and matplotlib library


