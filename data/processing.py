import re
import json
import codecs
from twkorean import TwitterKoreanProcessor

processor = TwitterKoreanProcessor()

fname = 'train.txt'
with open(fname) as f:
    with codecs.open('clean-'+fname, 'w', encoding='utf-8') as outf:
        lines = f.readlines()

        for l in lines:
            a, b = l.split(',', 1)
            b = re.sub(r'\([^)]*\)', '', b)
            for i in b.split(','):
                try:
                    i = re.findall(u'[\uAC00-\uD7A3]+', i.decode('utf8'))[0]
                except:
                    continue
                l = a+' '+processor.tokenize(i)[0].text+'\n'
                outf.write(l.encode('utf-8'))
