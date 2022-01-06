"""
=====================
@author:Cobb
@time:2021/8/21 17:27
@Email:986379041@qq.com
=====================
"""
import seldom
from tools.is_tool import do_money
from tools.do_json import get_global,get_UI
from tools.do_db import select_data
from API import productTotalSales


class TestProductTotalSales(seldom.TestCase):
    """
    产品总销量
    """

    def test_totalAmount(self):
        """
        总金额
        :return:
        """
        sql = """
            SELECT
            IFNULL(SUM(num),'0') AS num,
            IFNULL(SUM(amount),'0.00') AS amount
            FROM ads_allstaffsales_n02.dim_product_class aa
            LEFT JOIN ads_allstaffsales_n02.fact_statistics_order_list  bb ON aa.cid=bb.level_cid_one
            WHERE order_item_status IN (2,3,4,5,6) AND order_time >= '{0}' AND order_time < '{1}';
            """.format(get_global('year'), get_global('tomorrow'))
        productTotalSales.headers['mobile_login_token'] = get_global('token')
        self.post(productTotalSales.report_queryProductTotalSales_api['url'], json=productTotalSales.report_queryProductTotalSales_api['data'], headers=productTotalSales.headers)
        self.assertJSON(productTotalSales.report_queryProductTotalSales_api['success_message'])
        API_amount = do_money(self.get_value(self.response, 'amount'))
        SQL_amount = do_money(select_data(SQL=sql)[0]['amount'])
        UI_amount = get_UI('productTotalSales', 'total')
        print('SQL_amount:\t{0}\nAPI_amount:\t{1}\nUI_amount:\t{2}'.format(SQL_amount, API_amount, UI_amount))
        assert API_amount == SQL_amount == UI_amount, '产品总销量-总金额-结果校验失败'

    def test_salesRanking(self):
        """
        销售排行
        :return:
        """
        sql = """
            SELECT aa.product_class AS productClass, IFNULL(amount,0.00) AS amount, CONCAT(FORMAT(aa.amount/allamount*100,2),'%') AS saleShare
            FROM(
            SELECT  aa.product_class, IFNULL(SUM(amount),0.00) AS amount
            FROM ads_allstaffsales_n02.dim_product_class
            aa
            LEFT JOIN
            (
            SELECT * FROM ads_allstaffsales_n02.fact_statistics_product_order_list
            WHERE order_time >= '{0}' AND order_time < '{1}'
            )
            bb
            ON aa.cid=bb.level_cid_one
            GROUP BY aa.product_class
            )
            aa
            LEFT JOIN
            (
            SELECT IFNULL(SUM(amount),'0.00') AS allamount
            FROM ads_allstaffsales_n02.dim_product_class
            aa
            LEFT JOIN
            (
            SELECT * FROM ads_allstaffsales_n02.fact_statistics_product_order_list
            WHERE order_time >= '{0}' AND order_time < '{1}'
            )
            bb
            ON aa.cid=bb.level_cid_one
            )
            bb
            ON 1=1
            ORDER BY aa.amount DESC
            """.format(get_global('year'), get_global('tomorrow'))
        productTotalSales.headers['mobile_login_token'] = get_global('token')
        self.post(productTotalSales.report_queryProductTotalSalesDetails_api['url'], json=productTotalSales.report_queryProductTotalSalesDetails_api['data'], headers=productTotalSales.headers)
        self.assertJSON(productTotalSales.report_queryProductTotalSalesDetails_api['success_message'])
        SQL_result = select_data(SQL=sql)[:5]
        API_ranking = []
        SQL_ranking = []
        for i in range(0, 5):
            # 接口数据处理
            ranking_name = self.response['result'][i]['productClass']
            ranking_money = do_money(self.response['result'][i]['amount'])
            ranking_percent = self.response['result'][i]['saleShare']
            API_row = {ranking_name: [ranking_money, ranking_percent]}
            API_ranking.append(API_row)
            # 数据库数据处理
            ranking_name = SQL_result[i]['productClass']
            ranking_money = do_money(SQL_result[i]['amount'])
            ranking_percent = SQL_result[i]['saleShare']
            SQL_row = {ranking_name: [ranking_money, ranking_percent]}
            SQL_ranking.append(SQL_row)
        # UI数据获取
        UI_ranking = get_UI('productTotalSales', 'salesRanking')
        print('SQL_ranking:\t{0}\nAPI_ranking:\t{1}\nUI_ranking:\t{2}'.format(SQL_ranking, API_ranking, UI_ranking))
        assert SQL_ranking == API_ranking == UI_ranking, '产品总销量-销售排行-结果校验失败'

    def test_orderDetails(self):
        """
        订单列表
        :return:
        """
        sql = """
        SELECT
	aa.order_id orderId,
	aa.payment_price paymentPrice,
	aa.distribution_shop_name distributionShopName,
	aa.distribution_name distributionName,
	aa.shop_name shopName
        FROM ads_allstaffsales_n02.fact_statistics_order_list aa
        INNER JOIN
        (SELECT aa.order_id,MAX(aa.distribution_shop_id)distribution_shop_id,MAX(aa.order_item_id)order_item_id
        FROM ads_allstaffsales_n02.fact_statistics_order_list aa
        WHERE
        aa.order_item_status IN (2,3,4,5,6)
	AND aa.order_time>='{0}'
	AND aa.order_time<'{1}'
        GROUP BY aa.order_id
        ) bb ON aa.order_id=bb.order_id AND aa.order_item_id=bb.order_item_id AND  aa.distribution_shop_id=aa.distribution_shop_id
        ORDER BY aa.order_time DESC
        LIMIT 11
        """.format(get_global('year'), get_global('tomorrow'))
        productTotalSales.headers['mobile_login_token'] = get_global('token')
        API_result = []
        for page in range(1, 3):
            productTotalSales.report_queryOrderDetails_api['data']['page'] = page
            self.post(productTotalSales.report_queryOrderDetails_api['url'], json=productTotalSales.report_queryOrderDetails_api['data'], headers=productTotalSales.headers)
            self.assertJSON(productTotalSales.report_queryOrderDetails_api['success_message'])
            for row in self.response['result']:
                API_result.append(row)
        SQL_result = select_data(SQL=sql)
        API_orderDetails = []
        SQL_orderDetails = []
        for i in range(0, 11):
            # 接口数据处理
            orderId = API_result[i]['orderId']
            paymentPrice = do_money(API_result[i]['paymentPrice'])
            distributionShopName = API_result[i]['distributionShopName']
            distributionName = API_result[i]['distributionName']
            shopName = API_result[i]['shopName']
            API_row = {orderId: [paymentPrice, distributionShopName, distributionName, shopName]}
            API_orderDetails.append(API_row)
            # 数据库数据处理
            orderId = str(SQL_result[i]['orderId'])
            paymentPrice = do_money(SQL_result[i]['paymentPrice'])
            distributionShopName = SQL_result[i]['distributionShopName']
            distributionName = SQL_result[i]['distributionName']
            shopName = SQL_result[i]['shopName']
            SQL_row = {orderId: [paymentPrice, distributionShopName, distributionName, shopName]}
            SQL_orderDetails.append(SQL_row)
        UI_orderDetails = get_UI('productTotalSales', 'orderDetails')
        print('SQL_orderDetails:\t{0}\nAPI_orderDetails:\t{1}\nUI_orderDetails:\t{1}'.format(SQL_orderDetails, API_orderDetails, UI_orderDetails))
        assert SQL_orderDetails == API_orderDetails == UI_orderDetails, '产品总销量-订单列表-结果校验失败'

