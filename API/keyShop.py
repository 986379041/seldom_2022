"""
=====================
@author:Cobb
@time:2021/8/21 14:38
@Email:986379041@qq.com
=====================
"""
from tools.do_json import get_global
headers = {'Content-Type': 'application/json;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
           'mobile_login_token': None}
topFive_api = {
    'url': '/mobile/shop/topFive',
    'data': {"shopId": "2000295150",
             "startDate": get_global('today'),
             "endDate": get_global('today'),
             "shipmentType": "89",
             "page": 1},
    'success_message': {'message': 'OK'}
}
