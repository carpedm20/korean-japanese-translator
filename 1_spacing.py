#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs

with open('wiki.xml') as f:
    text = f.read()

    text = re.sub(r"<doc.*\">", '', text)
    text = re.sub(r"</doc>", '', text)

with open('wiki_sentences.txt', 'w') as f:
    sentences = re.split(r'\s*[!?.]\s*', text)
    for sentence in sentences:
        f.write(sentence+'\n')
