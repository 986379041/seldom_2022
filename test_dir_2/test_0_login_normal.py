"""
============
@auther: wuwofeng
@time: 2021/11/10  14:09
@email: 18825155741@163.com
============
"""
import seldom
from seldom import file_data
from locators import login_page




class LoginTest(seldom.TestCase):
    """
    UI登录
    """

    @file_data(file='login_normal.json', key='login')
    def test_login(self, _, username, passwd, ui_message,api_message):
        """
        UI成功登录
        :param _: 占位
        :param username: 用户名
        :param passwd: 密码
        :return:
        """

        # 使用locators/login_page的url地址打开浏览器
        self.open(login_page.login_url)
        # 使用self.type()操作输入框
        self.type(text=username, clear=True, xpath=login_page.userName)
        #self.type(xpath=login_page.userName, text=username, clear=True)
        self.type(text=passwd, clear=True, xpath=login_page.passWord)
        #self.type(xpath=login_page.passWord, text=passwd, clear=True)
        # 使用self.click点击动作，点击登录
        self.click(xpath=login_page.login_btn)
        # 断言asserText()断言文本内容
        self.assertText(ui_message)



