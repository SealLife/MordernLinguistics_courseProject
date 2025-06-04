import os

from misc import *


def tree_tag(src_file: str, out_file: str):
    cmd = f'..\\..\\TreeTagger\\bin\\tag-english {src_file} {out_file}'
    os.system(cmd)
    print(f'tree_tag: {src_file} -> {out_file} completed.')


"""
ce: 
..\material\ce_words.txt
..\output\ce_tagged.txt

se: 
..\material\se_words.txt
..\output\se_tagged.txt
"""
if __name__ == '__main__':
    tree_tag(input('src: '), input('out: '))
