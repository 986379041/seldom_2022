"""
============
@auther: wuwofeng
@time: 2021/11/10  14:09
@email: 18825155741@163.com
============
"""
import seldom
from seldom import file_data
from tools.do_json import save_global
from API import login_normal


class TestLogin(seldom.TestCase):
    """
    登录
    """

    @file_data(file='login_normal.json', key='login')
    # login.json里面有3个参数，其中第一个参数不用，直接把第2、3个参数赋值给username、passwd，如果不使用此参数，使用占位符_进行占位，不予使用
    def test_login(self, _, username, passwd, ui_message, api_message):
        """
        API成功登录
        :param _: 占位
        :param username: 用户名
        :param passwd: 密码
        :param
        :param ui_message: ui断言使用的字段
        :parem api_message: api断言使用的字段
        """
        # 赋值用户名给请求参数loginname
        login_normal.login_api['data']['loginname'] = username
        # 赋值密码给请求参数的loginpwd
        login_normal.login_api['data']['loginpwd'] = passwd
        # 复制返回信息给返回参数message
        login_normal.login_api['data']['response_message'] = api_message
        # 使用post方法进行请求
        self.post(login_normal.login_api['url'], json=login_normal.login_api['data'], headers=login_normal.headers)

        self.assertStatusCode(200)
        # 断言返回值和API信息里面的值
        # self.assertJSON(login.login_api['success_message'])
        # print(self.response['message'])
        # print(login.login_api['response_message'])
        self.assertEqual(self.response['message'],login_normal.login_api['data']['response_message'])

        # 保存登录的token值为全局变量，使用get_value获取值
        save_global('token', self.get_value(self.response, 'token'))

