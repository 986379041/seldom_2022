"""
=====================
@author:Cobb
@time:2021/8/21 17:24
@Email:986379041@qq.com
=====================
"""
from tools.do_json import get_global


headers = {'Content-Type': 'application/json;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
           'mobile_login_token': None}

report_queryProductTotalSales_api = {
    'url': '/distribution-shop/report/queryProductTotalSales',
    'data': {"startDate": get_global('year'),
             "endDate": get_global('today'),
             "productType": ""},
    'success_message': {'message': 'OK'}
}

report_queryProductTotalSalesDetails_api = {
    'url': '/distribution-shop/report/queryProductTotalSalesDetails',
    'data': {"startDate": get_global('year'),
             "endDate": get_global('today'),
             "productType": ""},
    'success_message': {'message': 'OK'}
}

report_queryOrderDetails_api = {
    'url': '/distribution-shop/report/queryOrderDetails',
    'data': {"productType": "",
             "biUnit": "",
             "startDate": get_global('year'),
             "endDate": get_global('today'),
             "page": 1},
    'success_message': {'message': 'OK'}

}
