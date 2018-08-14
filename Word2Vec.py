# Libraries

import logging
import gensim
from gensim.models import word2vec
from grnsim import corpora, models, similarities
import urllib.request
import collections
import math
from nltk.stem.snowball import FrenchStemmer
import os
import random
import zipfile
import datetime as dt
from sklearn.manifold import TSNE
import numpy as np
import tensorflow as tf
from string import punctuation
logging.basicConfig(format='%(asctime)s : %(message)s', level=logging.INFO)
import nltk
nltk.download('stopwords')

# Getting documents from specified directory
pd.read_csv(r"urlDeLaBDD.csv")

import string

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

path = "adresseDossiersContenantLesCommentaires"
tokenDict = {}
text=[]
for subdir, dirs, files in os.walk(path):

    for file in files:
        print(file)
        filePath = subdir + os.path.sep + file
        shakes = open(filePath, 'r', encoding="latin")
        text.append(shakes.readlines())
        printt(len(text))
        shakes.close()