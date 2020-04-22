import re
import nltk
import string
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


wnl  = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def remove_URLs(x):
    return re.compile(r'https?:\/\/\S+').sub(" ", x) 

def remove_punctuations(x):
    return re.sub(r"[^a-zA-Z]+", r" ", x)

def remove_contractions(x):
    rem_cont = [contractions.fix(word) for word in x.split()]
    return " ".join(map(str, rem_cont))

def tokenize(x):
    return word_tokenize(x)

def lowercase(x):
    return [word.lower() for word in x]

def remove_stopwords(x):
    stop_words = set(stopwords.words('english') + ['amp']) # added 'amp' to remove ampersands
    return [word for word in x if word not in stop_words]

def lemmatize(x):
    x = nltk.tag.pos_tag(x)
    x = [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in x]
    return [wnl.lemmatize(word, tag) for word, tag in x]


def remove_smallwords(x):
    return [t for t in x if len(t) > 2]

def tok_string(x):
    return " ".join(map(str, x))


def normalizeString(s):
    s = s.lower().strip()
    s = remove_URLs(s)
    s = remove_contractions(s)
    s = remove_punctuations(s)
    s = tokenize(s)
    s = remove_stopwords(s)
    s = lemmatize(s)
    s = remove_smallwords(s)
    s = tok_string(s)
    return s