"""
------------------------------
:@Time     : 2021/11/8 19:14
:@Author   : Cobb
:@Email    : 986379041@qq.com
:@Project  : Auto_BI_Reports
:@File     : load_file.py
:@Software : PyCharm
------------------------------
"""
from ruamel import yaml
from tools.do_json import base_dir


# yaml格式内容数据读取
def load_yaml(path=base_dir()+'/locators/Locators.yaml'):
    """
    读取yaml文件
    :param path: 文件路径
    :return: 返回文件内容
    """
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file.read(), Loader=yaml.Loader)
    return data

if __name__ == '__main__':
    print(load_yaml())