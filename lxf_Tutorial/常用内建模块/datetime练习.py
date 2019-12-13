# -*- coding:utf-8 -*-
# Username:chenxiong

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt_strTodt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    tz_int = int(re.match(r'^(\w*)+|-(\s+):$',tz_str).group(2))
    tz_utc = timezone(timedelta(hours=tz_int))  #创建时区
    time4 = now.replace(tzinfo=tz_utc)  #强制设置时区

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')    