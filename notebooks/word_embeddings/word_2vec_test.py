from gensim.models import Word2Vec
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import gensim.downloader as api
import gensim

import pandas as pd
import numpy as np
import pickle


def model_meth():
    model = gensim.models.KeyedVectors.load_word2vec_format('word_embeddings/GoogleNews-vectors-negative300.bin', binary=True)
    pickle.dumps(model)

model_meth()

model = None 
zero_vec = np.zeros(300, dtype=int)
def get_mean_vector(word2vec_model, words):
    # remove out-of-vocabulary words
    #words = [word for word in words if word in word2vec_model.key_to_index]
    process_words = []
    for el in words:
        if el in model.key_to_index:
            process_words.append(model[el])
        else:
            multi = el.split(",")

            if len(multi) > 1:
                new_val = [[]]
                arr = np.ndarray(shape=(3,300))
                i = 0
                for elem in multi:
                    elem = elem.strip()
                    if elem in model.key_to_index:
                        print(model[elem].shape)
                        new_val[i].append(model[elem])
                        #arr[i] = model[elem]
                    else:
                        new_val[i].append(zero_vec)
                #averages = [np.average(el) for el in new_val]
                #mean = np.mean(arr)
                #test = np.mean([new_val[0],new_val[1]])
                print(len(new_val))
                process_words.append(np.mean(np.asarray(new_val, dtype=object), axis=0))#geht das so mit dem np.mean PROBLEM we receive one value but should receive a matrix
                #print(np.mean(np.asarray(new_val, dtype=object), axis=0).shape) #TODO: this should be only an array with shape (1,300)
                i += 1
            else:
                process_words.append(zero_vec)
    if len(process_words) >= 1:
        return np.mean(process_words, axis=0)
    else:
        return []