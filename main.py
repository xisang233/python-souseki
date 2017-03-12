import time
time0 = time.time()
import sys
sys.setrecursionlimit(100000)  # set the maximum depth as 1500
# 以上为必要的前期处理 以下为逻辑部分

import MeCab


def filter(text):
    # 将原文中“［］《》”之间的文字(青空文库格式txt文件中的)删除
    # 传入一个字符串，输出过滤后的字符串
    flag = True
    news = ''
    for char in text:
        if char in '［《':
            flag = False
        if flag:
            news += char
        if char in '］》':
            flag = True
    return news

def sort(words):
    # 为单词计数列表排序，使用归并排序算法，传出有小到大排序后的列表
    if len(words) <= 1:
        return words
    else:
        small  = []
        big    = []
        middle = words.pop()
        for word in words:
            if word[0] > middle[0]:
                big.append(word)
            else:
                small.append(word)
        return sort(small) + [middle] + sort(big)

with open('wagahaiwa_nekodearu.txt', encoding = 'shift-JIS') as textfile:
    text = textfile.read()
    text = filter(text)
# 读取作品「我輩は猫である」并处理

m = MeCab.Tagger("")                # MeCab分词器初始化
words = m.parse(text).split('\n')   # 分词处理

dictcounter = {}

for word in words:                  # 词语计数
    if word in dictcounter:
        dictcounter[word] += 1
    else:
        dictcounter[word] = 1

words = []

for word in dictcounter:            # 将字典中的计数信息转到列表中以方便排序
    count = dictcounter[word]
    words.append((count, word))

words = sort(words)                 # 对列表排序
for word in words[:-100:-1]:        # 输出计数最高的100个词
    print(word[0], word[1])
print(time.time() - time0)          # 显示程序运行用时
