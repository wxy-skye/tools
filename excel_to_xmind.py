import re

import xmind
import pandas as pd

# 读取Excel文件为 DataFrame
df = pd.read_excel('1.xlsx')

data = df.values.tolist()
# 创建xmind工作簿
workbook = xmind.load("my.xmind")
sheet = workbook.getPrimarySheet()

# 创建主题
topic = sheet.getRootTopic()
created = {}
# 循环添加每一行为一个主题
for d in data:
    parent = topic
    for i in range(len(d)):
        title = d[i]
        # 判断该标题是否已创建
        if title in created:
            # 已创建,则获取节点
            parent = created[title]
        else:
            # 新创建
            child = parent.addSubTopic()
            child.setTitle(title)
            created[title] = child
            parent = child


# 保存为xmind文件
xmind.save(workbook, path='test.xmind')
