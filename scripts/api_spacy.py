from __future__ import unicode_literals
from __future__ import print_function
import sys

import plac
import bz2
import ujson
import spacy.en


def google_doing_something(w):
    if w.lower_ != 'google':
        return False
    # Is it the subject of a verb?
    elif w.dep_ != 'nsubj':
        return False
    # And not 'is'
    elif w.head.lemma_ == 'be' and w.head.dep_ != 'aux':
        return False
    # Exclude e.g. "Google says..."
    elif w.head.lemma_ in ('say', 'show'):
        return False
    else:
        return True


def main():
    # Load the model takes 10-20 seconds.
    nlp = spacy.en.English()
    comments = 'Inventor Ray Kurzweil made his name as a pioneer in technology that helped machines understand human language, both written and spoken. These days he is probably best known as a prophet of The Singularity, one of the leading voices predicting that artificial intelligence will soon surpass its human creators - resulting in either our enslavement or immortality, depending on how things shake out. Back in 2012 he was hired at Google as a director of engineering to work on natural language recognition, and today we got another hint of what he is working on. In a video from a recent Singularity conference Kurzweil says he and his team at Google are building a chatbot, and that it will be released sometime later this year.'
    comments = comments.split('. ')
    for comment_str in comments:
        comment_parse = nlp(comment_str)
        for word in comment_parse:
            if google_doing_something(word):
                # Print the clause
                print(''.join(w.string for w in word.head.subtree).strip())

if __name__ == '__main__':
    plac.call(main)
