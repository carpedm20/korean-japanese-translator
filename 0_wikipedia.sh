#!/bin/sh
cat jawiki-latest-pages-articles.xml | python WikiExtractor.py -o extracted
find extracted -wholename '*/wiki*' -exec cat {} \; > wiki.xml
