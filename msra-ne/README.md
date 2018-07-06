# MSRA Named Entity Corpus

A set of manually annotated Chinese word-segmentation data and specifications for training and testing a Chinese word-segmentation system for research purposes. Last published: August 16, 2007.

**This is not the official version!** 

Converted from MSRA's `xml` format to PKU format. The part-of-speech tags are predicted by `PerceptronPOSTagger` of [HanLP](https://github.com/hankcs/HanLP). 

## Samples

> 我们/r 藏/v 有/v 一/m 册/q １９４５年６月/DATE 油印/v 的/u 《/w 北京/LOCATION 文物/n 保存/v 保管/n 状态/n 之/u 调查/vn 报告/n 》/w ，/v 调查/vn 范围/n 涉及/v 故宫/LOCATION 、/v 历博/LOCATION 、/j 古研所/ORGANIZATION 、/v [北大/j 清华/j 图书馆/n]/LOCATION 、/v 北图/LOCATION 、/j 日/LOCATION 伪/j 资料/n 库/n 等/u 二十几家/INTEGER ，/d 言/Vg 及/v 文物/n 二十万件/INTEGER 以上/f ，/Ng 洋洋/z 三万/INTEGER 余/m 言/Vg ，/n 是/v 珍贵/a 的/u 北京/LOCATION 史料/n 。/w
> 画幅/n 上/f 分别/d 钤/Vg 有/v 两方/INTEGER 白文/n 篆刻/n 印章/n ，/vd 印/v 文/Ng 为/v “/v 平生/n 百/INTEGER 劫/Ng 千/INTEGER 难/Ng 后/f ”/v 、/v “/v 万象/n 纵横/v 不/d 系/v 留/v ”/v ，/v 我/r 以/p 之/r 作为/v 本文/r 标题/n ，/v 对/p 其庸/PERSON 教授/n 的/u 平生/n 及其/v 诗/n 书/n 画/n 艺术/n 的/u 造诣/n ，/v 正好/z 是/v 再/d 恰当/a 不过/u 的/u 概括/vn 说明/v 。/w

## NER types

Five NE categories with total 30 subcategories have been designed in the MSRA NE tag-set (see Table 1 below). The detail definition of each subcategory could be found in the spec, Tokenization Guidelines of Chinese Text.

![ner](http://wx4.sinaimg.cn/large/6cbb8645ly1ft0d3t9786j21kw28i7wh.jpg)

## Licence

Only for **research purpose**, see [Microsoft website](https://www.microsoft.com/en-us/download/details.aspx?id=52531) for details.

