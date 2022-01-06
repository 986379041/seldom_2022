"""
=====================
@author:Cobb
@time:2021/8/21 18:53
@Email:986379041@qq.com
=====================
"""
import datetime
from datetime import timedelta
from tools.do_json import save_global

now = datetime.datetime.now()
# 明天日期
tomorrow = (now + timedelta(days=1)).strftime("%Y-%m-%d")
save_global('tomorrow', tomorrow)
# 今日日期
today = now.strftime("%Y-%m-%d")
save_global('today', today)
# 周一日期
week = (now + timedelta(days= -now.weekday())).strftime("%Y-%m-%d")
save_global('week', week)
# 本月一号日期
month = datetime.datetime(now.year, now.month, 1).strftime("%Y-%m-%d")
save_global('month', month)
# 今年元旦
year = datetime.datetime(now.year, 1, 1).strftime("%Y-%m-%d")
save_global('year', year)

