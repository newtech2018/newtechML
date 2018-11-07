# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:22:58 2018

@author: tie303295
"""

# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

# 2018.10.24

import openpyxl

# ブックを取得
book = openpyxl.load_workbook('レビュー記録票_マージ結果_20181024_1048.xlsx')
# シートを取得 
sheet = book['Sheet1']

# セルを取得 
for rows in sheet['AL5':'AL5']:
 for cell in rows:
  print(cell.value)


# csv.py 
# -*- coding: utf-8 -*-

import csv
import MeCab

m = MeCab.Tagger("-Ochasen")
node = m.parseToNode(cell.value)

print (node)


# ファイルオープン
f = open('output.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

# データをリストに保持
while node:
 csvlist = []
 csvlist.append(node.surface)
 csvlist.append(node.feature)
 writer.writerow(csvlist) # 出力
 node = node.next
 print ("aaa")


# ファイルクローズ
f.close()
print ("おわり")