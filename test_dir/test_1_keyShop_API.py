"""
=====================
@author:Cobb
@time:2021/8/21 14:36
@Email:986379041@qq.com
=====================
"""
import seldom
from tools.do_json import get_global
from API import keyShop

# @seldom.skip(123)123
class TestKeyShop(seldom.TestCase):
    """
    关键店铺销量
    """

    def test_topFive(self):
        keyShop.headers['mobile_login_token'] = get_global('token')
        self.post(keyShop.topFive_api['url'], json=keyShop.topFive_api['data'], headers=keyShop.headers)
        self.assertJSON(keyShop.topFive_api['success_message'])
