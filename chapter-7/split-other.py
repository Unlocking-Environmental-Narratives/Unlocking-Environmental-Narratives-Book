#!/usr/bin/env python3

import os.path
import glob
from bs4 import BeautifulSoup
import nltk
import re

DODGY_NL = re.compile(r'\r\n?')

BLANK_LINE = re.compile(r'(\s*(\n|\r|\r\n)){2,}')

HERE = os.path.dirname(os.path.realpath(__file__))

INPUT_DIR = os.path.join(HERE, '..', 'html')

OUTPUT_DIR = os.path.join(HERE, '..', 'split', 'other')


def split_text(text):
    sentences = nltk.sent_tokenize(text)
    print('Sentences', len(sentences))
    splits = []
    while len(sentences) > 399:
        split = '\n'.join(sentences[:200])
        splits.append(split)
        del(sentences[:200])
    split = BLANK_LINE.sub('\n', '\n'.join(sentences))
    splits.append(split)
    return splits


def store(name, content, counter):
    filename = os.path.join(OUTPUT_DIR,
                            '%s%03i.txt' % (name, counter))
    print('Writing', filename)
    print('Size', len(content))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return



for filename in glob.iglob(INPUT_DIR + '/*djvu.html'):
    print('Reading', filename)
    with open(filename) as f:
        soup = BeautifulSoup(f, 'lxml')
    text = soup.find('pre').get_text()
    text1 = BLANK_LINE.sub('\n', text)
    contents = split_text(text1)
    output_name = os.path.splitext(os.path.basename(filename))[0]    
    for (i, content) in enumerate(contents):
        store(output_name, content, i)

    
