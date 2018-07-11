# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-07-11 21:04

def convert(src, dst):
    with open(src) as src, open(dst, 'w') as dst:
        for line in src:
            if line.startswith('#'):
                continue
            line = line.strip()
            if len(line) == 0:
                dst.write('\n')
                continue
            cells = line.split('\t')
            word = cells[1]
            tag = cells[3]
            dst.write('{}/{} '.format(word, tag))


if __name__ == '__main__':
    convert('UD_Chinese-GSD/zh_gsd-ud-train.conllu', 'udc.train.txt')
    convert('UD_Chinese-GSD/zh_gsd-ud-test.conllu', 'udc.test.txt')
    convert('UD_Chinese-GSD/zh_gsd-ud-dev.conllu', 'udc.dev.txt')
