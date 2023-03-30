# Linking Entities from Images to Knowledge Graphs

In this project we propose methods to link 1000 ImageNet classes to 768 DBpedia classes. <br> 
We do this by using string matching methods and language models(word2vec, wikipedia2vec , SBERT) <br> 

authors: Alpino, Davide (<https://github.com/DavideAl/>) ; Wei, Tianran <br> 

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
 &nbsp;&nbsp; --files -> contains all top3 files</br>
 &nbsp;&nbsp; --processed_files -> contains all top3 files, if there is no linkage between two classes we added
an empty value for them </br>
 &nbsp;&nbsp; evaluation.ipynb  -> This notebook is used to generate the top3 and top5 files</br>
 --notebooks -> In this folder we have all the notebooks we ever used, to investigate problems, created algorithms and found solutions. <br>
&nbsp;&nbsp;--evaluation <br>
&nbsp;&nbsp;--files <br>
&nbsp;&nbsp;--word_embeddings <br>
&nbsp;&nbsp;Bert.ipynb <br>
&nbsp;&nbsp;Jaccard_Levenshtein <br>
&nbsp;&nbsp;jaro_similarity.ipynb <br>
&nbsp;&nbsp;mapping_results_bert.csv <br>
&nbsp;&nbsp;matching.ipynb <br>
&nbsp;&nbsp;Query_imageNet_class_in_wikipedia__2.ipynb <br>
&nbsp;&nbsp;Query_imageNet_class_in_wikipedia.ipynb <br>
&nbsp;&nbsp;string_matching.ipynb -> implementation of the Fuzzy String matching, can be ignored, since this is done again in the Jaccard_Levenshtein norebook<br>
&nbsp;&nbsp;transitive_baseline.csv -> our baseline <br>
&nbsp;&nbsp;transitive_mapping.ipynb -> transitive mapping wordnet,wikidata,dbpedia<br>
&nbsp;&nbsp;wikipedia_test.py -> a simple file to test something, can be ignores<br>




 --src\data <br>
  &nbsp;&nbsp; mapping.py -> this files contains the class for doing the exact string matching. <br> 



## notebooks



Bert.ipynb -> contains the approach with SBert
Jaccard_Levenshtein.ipynb









