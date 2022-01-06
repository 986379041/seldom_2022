"""
=====================
@author:Cobb
@time:2021/8/24 9:36
@Email:986379041@qq.com
=====================
"""
from decimal import Decimal


def do_money(Num):
    """
    按理说，只要输入一个带数字的任意格式即可
    :param Num:
    :return:
    """
    if isinstance(Num, bytes) == True:
        Num = bytes.decode(Num)
    Num = '{}'.format(Num)
    _wan = Num.find('万')
    _yi = Num.find('亿')
    if _wan == -1 and _yi == -1:
        if float(Num) >= 10000000 and float(Num) < 10000000000:
            return '{}万'.format(float(Decimal(float(Num) / 10000).quantize(Decimal("0.00"))))
        elif float(Num) >= 10000000000:
            return '{}亿'.format(float(Decimal(float(Num) / 100000000).quantize(Decimal("0.00"))))
        else:
            return '{}'.format(float(Decimal(Num).quantize(Decimal("0.00"))))
    elif _wan != -1:
        return '{}万'.format(float(Decimal(Num[:_wan]).quantize(Decimal("0.00"))))
    elif _yi != -1:
        return '{}亿'.format(float(Decimal(Num[:_yi]).quantize(Decimal("0.00"))))
    else:
        raise ValueError


