"""Utilitites for Simple Search."""
from nltk.stem import WordNetLemmatizer


def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for token in tokens:
        lemmatized.append(lemmatizer.lemmatize(token))
    return lemmatized
