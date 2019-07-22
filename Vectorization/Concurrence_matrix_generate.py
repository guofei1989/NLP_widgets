"""
根据文本分词生成共现矩阵
共现矩阵: word可以用其周围窗函数的words表示
"""

import jieba
import numpy as np
from gensim import corpora


class ConcurrenceMatrix(object):
    def __init__(self, window=1):
        self.window = window    # 窗函数大小
        self.cocurrence_mat = None    # 共现矩阵

    @staticmethod
    def word2id(documents):
        texts = [jieba.lcut(document) for document in documents]
        dictionary = corpora.Dictionary(texts)
        dictionary_ids = dictionary.token2id
        print(dictionary_ids)
        dictionary_len = len(dictionary_ids)
        texts_ids = [[dictionary_ids[word] for word in text] for text in texts]
        return dictionary_len, texts_ids

    def calculate(self, documents):
        dictionary_len, texts_ids = self.word2id(documents)
        print(dictionary_len)
        print(texts_ids)
        self.cocurrence_mat = np.zeros((dictionary_len, dictionary_len))
        for text in texts_ids:
            for i in range(len(text)):
                j_l = max(0, i - self.window)
                j_r = min(len(text), i + self.window + 1)    # 注意+1
                for j in range(j_l, j_r):
                    if i != j:
                        self.cocurrence_mat[text[i]][text[j]] += 1
        return self.cocurrence_mat








if __name__ == '__main__':
    result = ConcurrenceMatrix().calculate(['我是个好人',
                '今天天气好',
                '今天天气不好'])
    print(result)
