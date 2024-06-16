import nltk

nltk.download('punkt')

import nltk.data


def split_into_sentences(paragraph):
    sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    paragraph = paragraph.replace('|', 'I')
    sentences = sentence_detector.tokenize(paragraph.replace('\n', ' '))

    return sentences

# paragraph = """"""
# sentences = split_into_sentences(paragraph)
#
# for i, sentence in enumerate(sentences):
#     print(f"Sentence {i + 1}: {sentence}")
