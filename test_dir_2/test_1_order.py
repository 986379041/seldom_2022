"""
============
@auther: wuwofeng
@time: 2021/10/27  16:09
@email: 18825155741@163.com
============
"""
import seldom
from locators import index_page_normal

class Testorder(seldom.TestCase):

    def test_order_waitPay(self):
        self.click(xpath=index_page_normal.shop_orders_waitPay)
        self.assertUrl('https://pre6fmall.gree.com/distribution-shop-uat4/#/distribution/ordinaryOrders?status=1')
        self.back()

    def test_order_waitDeliver(self):
        self.click(xpath=index_page_normal.shop_orders_waitDeliver)
        self.assertUrl('https://pre6fmall.gree.com/distribution-shop-uat4/#/distribution/ordinaryOrders?status=2')
        # self.assertTitle('店铺订单')
        self.back()

    def test_order_waitReceiving(self):
        self.click(xpath=index_page_normal.shop_orders_waitReceiving)
        self.assertUrl('https://pre6fmall.gree.com/distribution-shop-uat4/#/distribution/ordinaryOrders?status=3')
        # self.assertTitle('店铺订单')
        self.back()

    def test_order_return(self):
        self.click(xpath=index_page_normal.shop_orders_return)
        self.assertUrl('https://pre6fmall.gree.com/distribution-shop-uat4/#/distribution/ordinaryOrders?status=4')
        # self.assertTitle('店铺订单')
        self.back()

    def test_order_all(self):
        self.click(xpath=index_page_normal.shop_orders_all)
        self.assertUrl('https://pre6fmall.gree.com/distribution-shop-uat4/#/distribution/ordinaryOrders?status=0')
        # self.assertTitle('店铺订单')
        self.back()
