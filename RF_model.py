import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy2
import joblib

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    text = text.lower().replace('ё', 'е')
    text = text.replace('d', '')
    text = text.replace('rt', '')
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
    text = re.sub('@[^\s]+', '', text)
    text = re.sub(r'[a-zA-Z]', '', text)
    text = re.sub(r'\b[a-zA-Zа-яА-Я1-9]\b', '', text)
    text = re.sub(r'\b(?:[аевзпхщчоумы][аиеоузпхщчмы]+)+\b', '', text)
    text = re.sub(r'[0-9]', '', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()


def delete_stop_words_with_lemmatizing(words, morph, stop_words):
    default_list = []
    for word in words:
        if word not in stop_words:
            lem_word = morph.parse(str(word))[0].normal_form
            default_list.append(lem_word)
    return list(default_list)


def conveyor(text):
    stop_words = set(stopwords.words("russian"))
    morph = pymorphy2.MorphAnalyzer()

    tfidf_vect_test = joblib.load('tfidf_vect.pkl')
    RF_tfidf_clf = joblib.load('RF_tfidf_model.sav')

    text = preprocess_text(text)
    tokens = word_tokenize(text)

    text = delete_stop_words_with_lemmatizing(tokens, morph, stop_words)
    text = ' '.join(text)

    text_to_list = []
    text_to_list.append(text)

    X_test = tfidf_vect_test.transform(text_to_list)
    RF_tfidf_result = RF_tfidf_clf.predict(X_test)

    return RF_tfidf_result


data = str(input())

try:
    print(data, conveyor(data))
except UserWarning:
    print('Oops, something wrong :)')