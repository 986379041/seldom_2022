"""
=====================
@author:Cobb
@time:2021/8/21 11:21
@Email:986379041@qq.com
=====================
"""
headers = {'Content-Type': 'application/json;charset=UTF-8',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
login_api = {
    'url': 'https://pre6fmall.gree.com/distribution-shop/login',
    'data': {
        "loginname": None,
        "loginpwd": None,
        "userFlage": 1},
    'response_message': None
}
