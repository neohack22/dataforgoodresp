import logging
import gensim
from gensim.models import word2vec
from gensim import corpora, models, similarities
import urllib.request
import collections
import math
from nltk.stem.snowball import FrenchStemmer
import os
import random
# import zipfile
import datetime as dt
from sklearn.manifold import TSNE
import numpy as np
import tensorflow as tf
from string import punctuation
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import pandas as pd
import nltk
nltk.download('stopwords')

df=pd.read_csv(r"url_de_notre_bdd")

# df.head()

# take into account commments dispatched in index columns as well
l=[]
i=0
for elem in df['comments']:
    l.append(str(elem)+''+str(df['index].loc[i]))
    i=i+1

# opens every comment as a distinct file
for i in range(0,10,1):
    with open("Output"+str(i)+".txt", "w") as text_file:
        text_file.write(l[i])

# Get documents automatically

from os import listdir
from os.path import isfile, join
# the path to the directory where the comments txt files are located
mypath='chemin_vers_repertoires_des_commentaires_isolés/'

# list of every comment address
onlyfiles = [ mypath+'/'+f for f in listdir(mypath) if isfile(join(mypath, f))]

# put docs in a list

nb_doc=len(onlyfiles)
doc=list(range(nb_doc))
for i in range(len(doc)):

    with open(onlyfiles[i].encode('utf8')) as file:
        # The method readlines() reads until EOF using readline() and returns a list containing the lines
        doc[i] = file.readlines()

# Cleaning documents to compare

DOC=list(range(len(doc)))

for i in range(len(doc)): # iterate on every comment
    # remove formatting
    DOC[i] = ' '.join(doc[i])

from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize

stop_words = stopwords.words('french') + list(punctuation)
# we can add a manual list of stop words if needed

BO=list(range(len(doc)))

for i in range(len(doc)):
    BO[i] = DOC[i].strip().split(" ")

bo=list(range(len(doc)))
for i in range(len(doc)):
    bo[i]=[]

    for elem in BO[i] :
        if elem.strip().lower().replace('-','').replace('(',"").replace(')',"").replace("l'","").replace('"',"").replace',',"") in stop_words:
            continue
        else:
            bo[i].append(elem.strip().lower().replace('-','').replace('(',"").replace(')',"").replace("d'","").replace('"',"").replace('.',""))

        # Constructing a list of words

        ## wordSet = set(bowA).union(set(bowB)).union(set(bowC))

        for i in range(len(doc)):
            if i==0:
                wordSet = set(bo[i]) # eliminates duplicate entries of bo, being an array of relevant words in the comments
            else:
                wordSet = wordSet.union(set(bo[i]))

        wordDict=list(range(len(doc)))

        for i in range(len(doc)):
            wordDict[i] = dict.fromkeys(wordSet, 0) # creates a new dictionary from the given sequence of elements with a value provided

# words occurences analysis

for i in range(len(doc)):
    for word in bo[i]:
        wordDict[i][word]+=1

"""
import pandas as pd
pd.DataFrame(wordDict)
"""

# TF

## TF definition

def computeTF(wordDict, bow):
    tfDict = {}
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

## TF execution

tf=list(range(len(doc)))

for i in range(len(doc)):
    tf[i]= computeTF(wordDict[i], bo[i])

# IDF on all comments

## def idf

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                ifDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

    return idfDict

## apply idf to wordDict
idfs = computeIDF(wordDict)

## enhance IDF with TF
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

# apply tfidf to comments
    tfidfBow=list(range(len(doc)))

    for i in range(len(doc)):
        tfidfBow[i]= computeTFIDF(tf[i], idfs)

# Visualisation

## Dataframing
import pandas as pd
Code=pd.DataFrame(tfidfBow)

## print the most relevant words and score describing the comment
MyColumn=list(Code.columns)
a=list(range(len(Code)))
for i in range(len(Code)):
    a[i]={}

for elem in MyColumn:
    for i in range(len(Code)):
        #print(i,elem,Code[elem][i])
        a[i][elem]=Code[elem][i]

for i in range(len(doc)):
    print("########################## ",onlyfiles[i]," #################")
    maxValue = max(a[i].values())
    med=maxValue/2
    print ([(key, a[i][key]]) for key in a[i].keys() if a[i][key] >= med])
    print(maxValue)