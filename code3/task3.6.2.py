# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:26:42 2020

@author: meika
"""
#(6)关键词提取TextRank
from os import path
import jieba
import jieba.analyse

dict_dir = r"C:/Users/meika/Desktop/src/#dictCF.txt"
src_dir = r"C:/Users/meika/Desktop/src/#outputCF.txt"
d = path.dirname(__file__)

#读取文件
content = open(src_dir, 'r',encoding="utf-8").read()

#加载用户字典
jieba.analyse.set_idf_path(dict_dir);

#关键词提取TF-IDF(名词，动词)
tags = jieba.analyse.textrank(content, topK=100,withWeight=True,allowPOS=('n','v'))
for i in tags :
    print(i)