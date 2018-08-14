# Populating the interactive namespace from numpy and matplotlib
# %pylab inline """doesn't allow you to change the mode for matplotlib from UI"""
import pandas as import pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

"""
to disable python warnings
import warnings
warnings.filterwarnings('ignore')
"""

import pandas
from nltk.tokenize import word_tokenize
from nltk.tokenize import MWETokenizer
from nltk.tokenize import RegexpTokenizer
import nltk.data
from nltk import FreqDist
from nltk.sentiment import sentiment_analyzer
from unidecode import unidecode
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.stem import SnowballStemmer
import math
import word2vec
import unicodedata
import csv
import numpy as np
import matplotlib.pyplot as plt

# ignorer les mots les plus courants en français
stopwords = stopwords.words('french')
stopwords = stopwords + ["les", "ils", "elles", "h", "a", "ça", "les"]