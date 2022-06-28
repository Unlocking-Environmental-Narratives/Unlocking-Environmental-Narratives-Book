#!/usr/bin/env python3

import os.path
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.realpath(__file__))

INPUT = os.path.join(HERE, '..', 'html', 'A Journey to the Western Isles of Scotland.html')

OUTPUT_DIR = os.path.join(HERE, '..', 'split', 'western')


def store(content, counter):
    filename = os.path.join(OUTPUT_DIR,
                            'a_journey_to_the_western_isles%03i.html' % counter)
    print('Writing', filename)
    print('Size', len(content))
    wrapped = '<html>\n<head></head>\n<body>\n%s\n</body>\n</html>' % content
    print('Padded', len(wrapped))
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(wrapped)
    return


def next_element(elem):
    while elem is not None:
        # Find next element, skip NavigableString objects
        elem = elem.next_sibling
        if hasattr(elem, 'name'):
            return elem


with open(INPUT) as f:
    soup = BeautifulSoup(f, 'lxml')

h2s = soup.find_all('h2')

# https://stackoverflow.com/questions/14444732/how-to-split-a-html-page-to-multiple-pages-using-python-and-beautiful-soup

contents = []

for h2 in h2s:
    content = [str(h2)]
    elem = next_element(h2)
    while elem and elem.name != 'h2':
        content.append(str(elem))
        elem = next_element(elem)
    contents.append('\n'.join(content))

for (i, content) in enumerate(contents):
    store(content, i)

    
