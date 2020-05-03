#!/usr/bin/python3
import io
import os
import sys
import pyperclip

# load replacements
def load():
    dict = {}
    charsPath = os.path.dirname(os.path.abspath(__file__))  # location of this file
    charsFile = os.path.join(charsPath, 'chars.ini')
    with io.open(charsFile, 'rt', encoding='utf-8-sig') as file:
        for line in file:
            l = line.rstrip('\r\n')  # strip newline
            if l and l[0] != ';':
                char = l.split('=')
                if len(char) == 2:
                    dict[char[0]] = char[1]
                    #print('token: '+char[0]+"; replacement: "+char[1])
                #else:
                    #print('invalid format: ' + l)
            #else:
                #print('ignore comment: ' + l)
    return dict

# helpers
## input
def inp():
    return input('Enter Text and press Enter (leave empty to quit): ')
## process list
def process(dict, list):
    # replace
    res = ' '.join(map(lambda c: dict[c] if c in dict else c, list))
    # output
    print(res)
    # clipboard
    pyperclip.copy(res)
    print('(copied to clipboard)')

# main
def main():
    # load replacements
    dict = load()
    ## replace mode
    if len(sys.argv) > 1:
        # process arguments
        process(dict, sys.argv[1:])
    ## interactive mode
    else:
        line = inp()
        while line != '':
            # process line
            process(dict, line.split(' '))
            # input
            line = inp()
        print('Exit')

if __name__ == "__main__":
    main()
