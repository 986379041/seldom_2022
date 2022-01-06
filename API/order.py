"""
============
@auther: wuwofeng
@time: 2021/11/10  14:10
@email: 18825155741@163.com
============
"""

from tools.do_json import get_global

headers = {'Content-Type': 'application/json;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
           'mobile_login_token': None}

shop_orders_all_api = {
    'url': '/distribution-shop/orderDetails',
    'data':{
        "shopId": "2000261559",
        "orderItemStates": "1,2,3,4,5,6,9,10,13,14,15,21",
        "pageNumber": 1,
        "orderId": "",
        "receiverMobile": "",
        "receiverName": "",
        "orderMobile": ""},
    'success_message': {'message': 'OK'},
    'orderId': {
	    "orderId": "202108230176649001"},
}