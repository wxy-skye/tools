###最后一个节点为用例名称，其他节点为用例目录，-隔开
import pandas as pd
from xmindparser import xmind_to_dict

def xmind_to_excel(xmind_file, excel_file, customize_notes):
    # 解析XMind文件
    xmind_data = xmind_to_dict(xmind_file)

    # 递归遍历节点并提取数据
    def extract_data(node, parent_titles, data):
        node_title = node.get('title', '')
        current_titles = parent_titles + [node_title]
        parent_nodes = '-'.join(parent_titles)# 使用 "-" 分隔父节点信息
        parents_nodes = customize_notes + "-" + parent_nodes
        if 'topics' in node:
            for topic in node['topics']:
                extract_data(topic, current_titles, data)
        else:
            data.append((parents_nodes, node_title))

    # 提取数据
    data = []
    extract_data(xmind_data[0]['topic'], [], data)

    # 创建DataFrame并写入Excel文件
    df = pd.DataFrame(data, columns=['用例目录', '用例名称'])
    df.to_excel(excel_file, index=False)

# 示例用法
#需要转换的xmind文件路径
xmind_file = '1.xmind'
#转出excel文件路径
excel_file = 'example.xlsx'
#自定义根目录
customize_notes = "回归用例"
xmind_to_excel(xmind_file, excel_file, customize_notes)

###生成一列，各个节点用-隔开
import pandas as pd
from xmindparser import xmind_to_dict

def xmind_to_excel(xmind_file, excel_file):
    # 解析XMind文件
    xmind_data = xmind_to_dict(xmind_file)

    # 递归遍历节点并提取数据
    def extract_data(node, parent_titles, data):
        node_title = node.get('title', '')
        current_titles = parent_titles + [node_title]
        parent_nodes = '-'.join(parent_titles) # 使用 "-" 分隔父节点信息
        if 'topics' in node:
            for topic in node['topics']:
                extract_data(topic, current_titles, data)
        else:
            data.append(parent_nodes + '-' + node_title) # 将父节点和当前节点标题合并为一列

    # 提取数据
    data = []
    extract_data(xmind_data[0]['topic'], [], data)

    # 创建DataFrame并写入Excel文件
    df = pd.DataFrame(data, columns=['用例名称'])
    df.to_excel(excel_file, index=False)

###生成一列，去除根节点，其余节点用-隔开
# 示例用法
xmind_file = '1.xmind'
excel_file = 'example.xlsx'
xmind_to_excel(xmind_file, excel_file)

import pandas as pd
from xmindparser import xmind_to_dict

def xmind_to_excel(xmind_file, excel_file):
    # 解析XMind文件
    xmind_data = xmind_to_dict(xmind_file)

    # 递归遍历节点并提取数据
    def extract_data(node, parent_titles, data):
        node_title = node.get('title', '')
        current_titles = parent_titles + [node_title]
        parent_nodes = '-'.join(parent_titles) # 使用 "-" 分隔父节点信息
        if 'topics' in node:
            for topic in node['topics']:
                extract_data(topic, current_titles, data)
        else:
            data.append(parent_nodes + '-' + node_title) # 将父节点和当前节点标题合并为一列

    # 提取数据
    data = []
    root_topic = xmind_data[0]['topic']
    if 'topics' in root_topic:
        for topic in root_topic['topics']:
            extract_data(topic, [], data)

    # 创建DataFrame并写入Excel文件
    df = pd.DataFrame(data, columns=['用例名称'])
    df.to_excel(excel_file, index=False)

# 示例用法
xmind_file = '1.xmind'
excel_file = 'example.xlsx'
xmind_to_excel(xmind_file, excel_file)
