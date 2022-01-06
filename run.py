import seldom,os
from tools import get_day
# project_path = os.path.dirname(os.path.abspath(__file__))
if __name__ == '__main__':
    # run test file
    seldom.main(path="test_cases/",
                browser="iPhone X",
                # driver_path=os.path.join(project_path,'chromedriver.exe'),
                base_url='https://fmall.gree.com',
                title="BI报表自动化测试",
                description="测试环境",
                debug=False,
                rerun=2,
                # addressee='772793409@qq.com,986379041@qq.com',
                # addressee=['18825155741@163.com','986379041@qq.com'],
                save_last_run = True
                )