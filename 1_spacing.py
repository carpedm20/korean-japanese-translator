#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import MeCab
import codecs

wiki_xml = 'ja-wiki.xml'
wiki_sentences = 'ja-wiki_sentences.txt'

#if True:
if os.path.isfile(wiki_xml):
    print "%s exists..." % wiki_xml
else:
    with open(wiki_xml) as f:
        text = f.read()

        text = re.sub(r"<doc.*\">", '', text)
        text = re.sub(r"</doc>", '', text)

if os.path.isfile(wiki_sentences):
    print "%s exists..." % wiki_sentences
else:
    with codecs.open(wiki_sentences, 'w', encoding="utf-8") as f:
        sentences = re.split(ur'\s*[!?.。\n]\s*', text.decode('utf-8'))
        for sentence in sentences:
            f.write(sentence+'\n')

STOP_WORD = " 。 、 「 」 （ ） ? ？ ： ， , ． ! ！ # $ % & ' ( ) = ~ | ` { } * + ? _ > [ ] @ : ; / . ¥ ^ 【 】 ￥ ＿ ／ 『 』 ＞ ？ ＿ ＊ ＋ ｀ ｜ 〜 ＊ ＋ ＞ ？ ＃ ” ＃ ＄ ％ ＆ ’ \" ・".split()
word_classes = [u'名詞',u'動詞',u'形容詞',u'副詞',u'助詞',u'助動詞']

def n2l(node):
    ll = []
    prev = ''
    while node:
        cur = node.feature.split(",")[0]
        if cur == '助詞':
            ll[-1] = ll[-1] + node.surface
        elif cur == '名詞' and prev == '名詞':
            ll[-1] = ll[-1] + node.surface
        else:
            ll.append(node.surface)
        node = node.next
        prev = cur
    return ll

ban_pos = ['Josa','Number','Punctuation']
accept_pos = ['名詞','動詞','形容詞','副詞','助動詞']
def n2l2(node):
    ll = []
    while node:
        cur = node.feature.split(",")[0]
        if cur in accept_pos:
            ll.append(node.surface)
        node = node.next
    return ll

tagger = MeCab.Tagger("wakati")
with codecs.open('jawiki_tokens.txt', 'w', encoding="utf-8") as token_f:
    with codecs.open(wiki_sentences, encoding="utf-8") as f:
        sentences = f.readlines()
        for sentence in sentences:
            s = sentence.encode('utf-8')
            for i in STOP_WORD:
                s=s.replace(i,'')
            node = tagger.parseToNode(s)
            ll = n2l2(node)
            s = "\t".join(ll)+"\n"
            token_f.write(s.decode('utf-8'))

