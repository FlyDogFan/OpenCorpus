# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-01-12 22:47
from pyhanlp import *


def pystr_to_jstring(pystr):
    from jpype import java
    java_string = java.lang.String(pystr.encode(), 'UTF8')
    return java_string


def jstring_to_pystr(jstring):
    return str(jstring).encode('utf-16', errors='surrogatepass').decode('utf-16')


def convert(src, dst):
    with open(src) as src, open(dst, 'w') as dst:
        for line in src:
            sc = jstring_to_pystr(HanLP.t2s(pystr_to_jstring(line)))
            dst.write(sc)


convert('UD_Chinese-GSD/zh_gsd-ud-train.conllu', 'chs_gsd-ud-train.conllu')
convert('UD_Chinese-GSD/zh_gsd-ud-test.conllu', 'chs_gsd-ud-test.conllu')
convert('UD_Chinese-GSD/zh_gsd-ud-dev.conllu', 'chs_gsd-ud-dev.conllu')
