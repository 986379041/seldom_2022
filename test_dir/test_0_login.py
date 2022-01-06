"""
=====================
@author:Cobb
@time:2021/8/23 8:41
@Email:986379041@qq.com
=====================
"""
import seldom
from seldom import file_data
from locators import login_page


class LoginTest(seldom.TestCase):
    """
    UI登录
    """

    @file_data(file='login.json', key='login')
    def test_login(self, _, username, passwd):
        """
        UI成功登录
        :param _: 占位
        :param username: 用户名
        :param passwd: 密码
        :return:
        """
        self.open(login_page.login_url)
        self.type(xpath=login_page.userName, text=username, clear=True)
        self.type(xpath=login_page.passWord, text=passwd, clear=True)
        self.click(xpath=login_page.login_btn)
        self.assertText('登录成功')
