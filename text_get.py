# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:11:24 2019

@author: tie303295
"""

import openpyxl
import csv
import MeCab

# ブックを取得
book = openpyxl.load_workbook('レビュー記録票_マージ結果_テスト.xlsx')
sheet = book['Sheet1']

# ファイルオープン
# 結果出力ファイルはここ　C:\Users\tie304164\.spyder-py3
f = open('output2.txt', 'w')
writer = csv.writer(f, lineterminator='\n')

# セルを取得 
for rows in sheet['AL5':'AL50']:
    for cell in rows:
        print(cell.value)
#       print('end')
        sample = cell.value
        tagger = MeCab.Tagger("-Owakati")
        result = tagger.parse(sample).strip()
        print(result)
        src = result

# データをリストに保持

        csvlist = []
        csvlist.append(result)
        writer.writerow(csvlist)  # 出力
#    csvlist.append(node.feature)

#    node = node.next
        

# ファイルクローズ
f.close()
print ("おわり")
