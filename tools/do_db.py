"""
=====================
@author:Cobb
@time:2021/6/26 10:01
@Email:986379041@qq.com
=====================
"""
from tools.do_json import get_global
from seldom.db_operation import MySQLDB
def db_base():
    db = MySQLDB(host="121.37.2.117",
             port="6606",
             user="root",
             password="Gree@2020",
             database="ads_allstaffsales_n02")
    return db


def select_data(table=None,where=None,sort=None,num=None,SQL=None):
    """
    select_data(table='base_send_message',where={'address':'15765560218'},sort= 'id',num=1)
    :param table:
    :param where:
    :param sort:
    :param num:
    :return:
    """
    if SQL is not None:
        data = db_base().select_data(SQL=SQL)
    else:
        data = db_base().select_data(table=table, where=where,sort=sort,num=num)
    db_base().close()
    return data
if __name__ == '__main__':
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
            """.format(get_global('year'), get_global('tomorrow'))
    # print(select_data('fact_api_mall_order_list',{'shop_name':'格力董明珠店'},num=10))
    # print(str(select_data(SQL=sql)[0]['amount'])[1:])
    print(select_data(SQL=sql)[:11])


