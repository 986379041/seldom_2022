"""
============
@auther: wuwofeng
@time: 2021/11/10  14:07
@email: 18825155741@163.com
============
"""
import seldom
from tools.do_json import get_global
from API import order

class TestLogin(seldom.TestCase):
    """
    订单
    """

    def test_order(self):
        order.headers['mobile_login_token'] = get_global('token')
        # 请求订单列表
        self.post(order.shop_orders_all_api['url'],
                  json=order.shop_orders_all_api['data'],
                  headers=order.headers)
        self.assertStatusCode(200)
        self.assertJSON(order.shop_orders_all_api['success_message'])

        # 请求订单详情
        self.post(order.shop_orders_all_api['url'],
                  json=order.shop_orders_all_api['orderId'],
                  headers=order.headers)
        self.assertStatusCode(200)
        self.assertJSON(order.shop_orders_all_api['success_message'])
        # print(order.shop_orders_all_api['orderId']['orderId'])
        # print(self.response['result'][0]['order_id'])
        # 断言返回的订单id和实际请求的订单id是否一致
        # 新增了响应头信息，为了断言返回头的内容
        print(self.headers)
        assert order.shop_orders_all_api['orderId']['orderId'] == self.response['result'][0]['order_id']

