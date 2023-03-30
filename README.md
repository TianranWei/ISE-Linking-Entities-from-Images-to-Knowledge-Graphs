# Linking Entities from Images to Knowledge Graphs

In this project we propose methods to link 1000 ImageNet classes to 768 DBpedia classes. <br> 
We do this by using string matching methods and language models(word2vec, wikipedia2vec , SBERT) <br> 

authors: Alpino, Davide; Wei, Tianran <br> 

## Observe
Sometimes the path to the .csv input files doesn't work, so
you have to put in the absoulte path.

## evaluation

files --> contains all top3 files <br> 
processed_files --> contains all top3 files, if there is no linkage between two classes we added
an empty value for them. (in files these empty values are missing) <br> 
evaluation.ipynb -> This notebook is used to generate the top3 and top5 files <br> 


## notebooks

## src\data
mapping.py -> this files contains the class for doing the exact string matching. <br> 






