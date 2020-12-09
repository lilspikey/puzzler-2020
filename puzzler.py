#!/usr/bin/env python3

import argparse


def build_edges():
    pairs = {
        'br', 'bl', 'bo', 'bt', 'by',
        'rc', 're', 'ro', 'rl',
        'ch', 'cg', 'co', 'ce',
        'hs', 'hw', 'ho', 'hg',
        'sy', 'sn', 'so', 'sw',
        'yb', 'yt', 'yo', 'yn',
        'le', 'lo', 'lt',
        'eg', 'eo',
        'gw', 'go',
        'wn', 'wo',
        'nt', 'no',
        'tl', 'to'
    }
    edges = set()
    for pair in pairs:
        rev_pair = pair[1] + pair[0]
        edges.add(pair)
        edges.add(rev_pair)
    return edges


EDGES = build_edges()
LETTERS = set(''.join(EDGES))


def words_that_match(words_file):
    found = set()
    for line in words_file:
        word = line.strip().lower()
        matches = True
        if word not in LETTERS and len(word) > 1: 
            for i in range(len(word)-1):
                pair = word[i:i+2]
                if pair not in EDGES:
                    matches = False
                    break
        if matches:
            if word not in found:
                yield word
                found.add(word)


def main(args):
    for word in words_that_match(args.words_file):
        print(word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--words-file', type=argparse.FileType('r'), default='/usr/share/dict/words')

    args = parser.parse_args()

    main(args)

