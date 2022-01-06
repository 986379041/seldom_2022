"""
=====================
@author:Cobb
@time:2021/8/21 16:04
@Email:986379041@qq.com
=====================
"""
import json,os


def base_dir():
    """
    获取根目录
    :return:
    """
    base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    return base_dir

def save_global(key, value):
    """
    保存全局变量
    :param key: 键
    :param value: 值
    :return:
    """
    with open(base_dir() + '/test_data/global.json', 'r+', encoding='utf-8') as jsonFile:
        load_dict = json.load(jsonFile)
        load_dict[key] = value
        jsonFile.seek(0)
        json.dump(load_dict, jsonFile, ensure_ascii=False)
        jsonFile.truncate()

def get_global(key):
    """
    获取全局变量
    :param key: 键
    :return:
    """
    with open(base_dir() + '/test_data/global.json', 'rb') as load_f:
        return json.load(load_f)[key]

def save_UI(module, key, value):
    """
    UI执行时保存页面数据
    :param module: 模块
    :param key: 键
    :param value: 值
    :return:
    """
    with open(base_dir() + '/test_data/UI.json', 'r+', encoding='utf-8') as jsonFile:
        load_dict = json.load(jsonFile)
        load_dict[module][key] = value
        jsonFile.seek(0)
        json.dump(load_dict, jsonFile, ensure_ascii=False)
        jsonFile.truncate()

def get_UI(module, key):
    """
    获取UI保存的数据
    :param module: 模块
    :param key: 键
    :return:
    """
    with open(base_dir() + '/test_data/UI.json', 'rb') as load_f:
        return json.load(load_f)[module][key]

if __name__ == '__main__':
    # save_global('token','123')
    save_global('test', '666')
    # print(base_dir())