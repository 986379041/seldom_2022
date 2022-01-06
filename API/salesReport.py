"""
=====================
@author:Cobb
@time:2021/8/25 16:26
@Email:986379041@qq.com
=====================
"""
from tools.do_json import get_global

headers = {'Content-Type': 'application/json;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
           'mobile_login_token': None}

shopReport_storeSale_api = {
    'url': '/distribution-shop/shopReport/storeSale',
    'data': {"storeId": "2000002215",
             "startTime": get_global('year'),
             "endTime": get_global('tomorrow'),
             "productClass": "",
             "category": "",
             "series": ""},
    'success_message': {'message': 'OK'}
}

shopReport_storeTopProduct_api = {
    'url': '/distribution-shop/shopReport/storeTopProduct',
    'data': {"storeId": "2000002215",
             "startTime": "2021-01-01 00:00:00",
             "endTime": "2021-08-25 16:10:57",
             "productClass": "",
             "category": "",
             "series": ""}
    ,
    'success_message': {'message': 'OK'}
}
