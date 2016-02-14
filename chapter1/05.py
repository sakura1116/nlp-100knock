# -*- coding: utf-8 -*-

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

N-gramとは
検索対象を単語単位ではなく文字単位で分解し、後続の N-1 文字を含めた状態で出現頻度を求める方法。Nの値が1なら「ユニグラム(uni-gram)」、2なら「バイグラム(bi-gram)」、3なら「トライグラム(tri-gram)」と呼ばれる。
"""

# 単語bi-gram
def n_glam(sentence_list: list, num: int) -> list:
    data = sentence_list

    result = []
    for x in range(len(data)):
        z = data[x:x+num]
        r = " ".join(z) if len(z) == num else None
        if r is not None:
            result.append(r)
    return result


if __name__ == '__main__':
    sentence = 'I am an NLPer'
    num = 2
    print(n_glam(sentence.split(), num))

    no_gap_word = "".join(sentence.split())
    print(n_glam([no_gap_word[x] for x in range(len(no_gap_word))], num))
