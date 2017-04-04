#!/usr/bin/env python3

import sys
import os
from collections import Counter
import re


def get_statistic(filename):
    "Return list of (word, count) pairs."        
    wordcount = Counter() 
    if os.path.isfile(filename):
        with open(filename) as file_:
            #TODO maybe use re.sub('\W', '')
            wordcount.update(file_.read().lower().split())
        return wordcount.items()
    else:
        print("File {} not exist".format(filename))
        

def main_func():
    filename = sys.argv[1]
    wordcount = get_statistic(filename)
    if wordcount:
        #Sort by word.
        wordcount = sorted(wordcount, key=lambda pair: pair[0])
        #Sort by count.
        wordcount = sorted(wordcount, key=lambda pair: pair[1], reverse=True)
        for word, count in wordcount:
            print("{}: {}".format(word, count))
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main_func()
    else:
        print("Usage:\n\tfilestat.py <filename>")
