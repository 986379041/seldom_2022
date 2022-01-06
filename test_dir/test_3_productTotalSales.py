"""
=====================
@author:Cobb
@time:2021/8/25 13:50
@Email:986379041@qq.com
=====================
"""
import seldom
from locators import productTotalSales_page,index_page
from tools.do_json import save_UI
from tools.is_tool import do_money


class TestProductTotalSales(seldom.TestCase):
    """
    UI产品总销量
    """

    def test_totalAmount(self):
        """
        总金额
        :return:
        """
        self.click(xpath=index_page.productTotalSales_btn)
        self.click(xpath=productTotalSales_page.year_btn)
        total_amount = do_money(self.get_text(xpath=productTotalSales_page.totalAmount))
        save_UI('productTotalSales', 'total', total_amount)
        self.back()


    def test_salesRanking(self):
        """
        销售排行
        :return:
        """
        self.click(xpath=index_page.productTotalSales_btn)
        self.click(xpath=productTotalSales_page.year_btn)
        list_gather = []
        for i in range(2, 7):
            ranking_name = self.get_text(xpath=productTotalSales_page.rankingName.replace('%', str(i)))
            ranking_money = do_money(self.get_text(xpath=productTotalSales_page.rankingMoney.replace('%', str(i))))
            ranking_percent = self.get_text(xpath=productTotalSales_page.rankingPercent.replace('%', str(i)))
            dict_row = {ranking_name: [ranking_money, ranking_percent]}
            list_gather.append(dict_row)
        save_UI('productTotalSales', 'salesRanking', list_gather)
        self.back()

    def test_orderDetails(self):
        """
        订单列表
        :return:
        """
        self.click(xpath=index_page.productTotalSales_btn)
        self.click(xpath=productTotalSales_page.year_btn)
        self.click(xpath=productTotalSales_page.viewOrder_btn)
        self.move_to_element(xpath=productTotalSales_page.orderId.replace('%', str(10)))
        list_gather = []
        for i in range(1, 12):
            orderId = self.get_text(xpath=productTotalSales_page.orderId.replace('%', str(i)))
            assert orderId not in str(list_gather), '订单号重复'
            orderTotalAmount = do_money(self.get_text(xpath=productTotalSales_page.orderTotalAmount.replace('%', str(i)))[1:])
            orderDistributionShop = self.get_text(xpath=productTotalSales_page.orderDistributionShop.replace('%', str(i)))
            orderDistributor = self.get_text(xpath=productTotalSales_page.orderDistributor.replace('%', str(i)))
            orderShopName = self.get_text(xpath=productTotalSales_page.orderShopName.replace('%', str(i)))
            dict_row = {orderId: [orderTotalAmount, orderDistributionShop, orderDistributor, orderShopName]}
            list_gather.append(dict_row)
        save_UI('productTotalSales', 'orderDetails', list_gather)
        self.back()
        self.back()
