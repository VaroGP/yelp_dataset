import re
import nltk

def contractions(text):
        text = re.sub(r"won't", "will not",text)
        text = re.sub(r"would't", "would not",text)
        text = re.sub(r"could't", "could not",text)
        text = re.sub(r"'d",  " would",text)
        text = re.sub(r"can't", "can not",text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"'re", " are", text)
        text = re.sub(r"'s", " is", text)
        text = re.sub(r"'ll", " will", text)
        text = re.sub(r"'t", " not", text)
        text = re.sub(r"'ve", " have", text)
        text = re.sub(r"'m", " am", text)
        return text
    
# Remove non-alpha characters
def rm_non_alfa(text):
    text = re.sub('[^A-Za-z]+',' ', text) 
    return text

def blanks(text):
    text = re.sub('  +', ' ', text)
    return text

# Lemmatization
def lemmatizer(text):
    lemmatizer = nltk.WordNetLemmatizer()
    text = [lemmatizer.lemmatize(word,pos='v') for word in text.split()]
    return text

# Stop Words
def stopwords_removal(text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    text = [word for word in text if word not in stop_words]
    text = ' '.join(text)
    return text

# Preprocessing
def preprocessing(text):
    #Normalize
    text = text.strip().lower()
    # Clean text
    text = contractions(text)
    text = rm_non_alfa(text)
    text = blanks(text)
    text = lemmatizer(text)
    text = stopwords_removal(text)
    return text
  
class TextPreprocessor():
    """
    Sklearn custom transformer to preprocess text data
    """

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X.text = X.text.map(lambda x : preprocessing(x))
        return X.text
