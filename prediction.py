# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 15:42:07 2019

@author: tie303295
"""

import sys
import fasttext as ft
import MeCab

class predict:

    def __init__(self):
        # モデル読み込み
        self.classifier = ft.load_model('learning.bin')

    def get_surfaces(self, content):
        """
        文書を分かち書き
        """
        tagger = MeCab.Tagger('')
        tagger.parse('')
        surfaces = []
        node = tagger.parseToNode(content)

        while node:
            surfaces.append(node.surface)
            node = node.next

        return surfaces


    def bunrui_class(self, content):
        """
        指摘事項を解析して分類を行う
        """
        words = " ".join(self.get_surfaces(content))
#       estimate = self.classifier.predict([words], k=2)[0][0]
#       estimate = self.classifier.predict_proba([words], k=3)[0][0]
        estimate = self.classifier.predict([words])
        print(words)
#       print(estimate)

        if estimate == "__label__1,":
            print('要件提示漏れ・確認不足', estimate[1])
        elif estimate == "__label__2,":
            print('設計漏れ・ミス', estimate[1])
        elif estimate == "__label__3,":
            print('設計改善', estimate[1])
        if estimate == "__label__4,":
            print('説明の誤り・不足', estimate[1])
        elif estimate == "__label__5,":
            print('記述/表記ミス', estimate[1])
        elif estimate == "__label__6,":
            print('標準化誤り（形式・書式・規約違反）', estimate[1])
        if estimate == "__label__7,":
            print('制御構造不良', estimate[1])
        elif estimate == "__label__8,":
            print('ｺｰﾃﾞｨﾝｸﾞ不良', estimate[1])
        elif estimate == "__label__9,":
            print('テスト設計不良（ケース漏れ・誤り））', estimate[1])
        else:
            print('どれにも分類できませんでした・・ごめんなさい。')

if __name__ == '__main__':
    pre = predict()
    pre.bunrui_class("".join(sys.argv[1:]))