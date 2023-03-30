# Linking Entities from Images to Knowledge Graphs

In this project we propose methods to link 1000 ImageNet classes to 768 DBpedia classes. <br> 
We do this by using string matching methods and language models(word2vec, wikipedia2vec , SBERT) <br> 

authors: Alpino, Davide; Wei, Tianran <br> 

## Observe
*Sometimes the path to the .csv input files doesn't work, so
you have to put in the absolute path.

*Since GitHub only allows 1 GB of data, the models for word2vec and wikipedia2vec need to be downloaded seperately.

[Word2Vec](https://code.google.com/archive/p/word2vec/)

[Wikipedia2vec](https://wikipedia2vec.github.io/wikipedia2vec/pretrained/)



*We used an anconda virtual environment, for the wikipedia2vec this won't work, but executing the same code inside 
Google Colab works.

## Folder Documentation
--evaluation </br>
  --files </br>
  --processed_files </br>
  evaluation.ipynb </br>
## evaluation

files --> contains all top3 files <br> 
processed_files --> contains all top3 files, if there is no linkage between two classes we added
an empty value for them. (in files these empty values are missing) <br> 
evaluation.ipynb -> This notebook is used to generate the top3 and top5 files <br> 


## notebooks
In this folder we have all the notebooks we ever used, to investigate problems, created algorithms and found solutions. <br>
### evaluation
### files
### word_embeddings

Bert.ipynb -> contains the approach with SBert
Jaccard_Levenshtein.ipynb

## src\data
mapping.py -> this files contains the class for doing the exact string matching. <br> 






