#!/usr/bin/env python3
#
import sys
import re

delim = ","

def convert(string):
    nodes = []
    string = re.split(r',\,*(?![^[]*\])', string)
    for i in string:
        if not "[" in i:
            nodes.append(i)
            continue
        j = i.split('[')[1].replace(']', '')
        h = i.split('[')[0]
        j = j.split(',')
        temp = []
        for k in j:
            if not "-" in k:
                nodes.append(h + k)
            else:
                start = int(k.split('-')[0])
                end = int(k.split('-')[1])
                for l in range(start, end + 1):
                    nodes.append(h + str(l))
    return nodes

if __name__  == "__main__":
    string = sys.argv[1]
    print(delim.join(convert(string)))
