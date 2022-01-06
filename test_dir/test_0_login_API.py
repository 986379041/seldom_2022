"""
=====================
@author:Cobb
@time:2021/8/21 11:30
@Email:986379041@qq.com
=====================
"""
import seldom
from seldom import file_data
from tools.do_json import save_global
from API import login


class TestLogin(seldom.TestCase):
    """
    登录
    """

    @file_data(file='login.json', key='login')
    def test_login(self, _, username, passwd):
        """
        API成功登录
        :param _: 占位
        :param username: 用户名
        :param passwd: 密码
        :return:
        """
        login.login_api['data']['loginname'] = username
        login.login_api['data']['loginpwd'] = passwd
        self.post(login.login_api['url'], json=login.login_api['data'], headers=login.headers)
        self.assertJSON(login.login_api['success_message'])
        save_global('token', self.get_value(self.response, 'token'))

