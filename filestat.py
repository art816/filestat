#!/usr/bin/env python3

import sys
import os
from collections import Counter


def get_statistic(filename):
    "Return dict_items of (word, count) pairs or None."
    wordcount = Counter()
    if os.path.isfile(filename):
        with open(filename, encoding="utf-8-sig") as file_:
            #TODO maybe use re.sub('\W', '')
            try:
                wordcount.update(file_.read().lower().split())
                return wordcount.items()
            except UnicodeDecodeError:
                print('UnicodeDecodeError')
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise            
    else:
        print("File {} not exist".format(filename))


def main_func(filename):
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
        main_func(sys.argv[1])
    else:
        print("Usage:\n\tfilestat.py <filename>")
