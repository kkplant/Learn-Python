# -*- coding:utf-8 -*-
#Username:chenxiong

#datatime是Python处理日期和时间的标准库
from datetime import datetime, timedelta, timezone

#获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

#获取指定日期和时间
dt = datetime(2008,8,8,20,8)
print(dt)
print(type(dt))

#datetime转换为timestamp（时间戳）
"""
1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0
（1970年以前的时间timestamp为负数）
"""
print(dt.timestamp())

#timestamp转换为UTC标准时区时间
t = 1429417200.665
print(datetime.fromtimestamp(t))  #本地时间
print(datetime.utcfromtimestamp(t))  #UTC时间

#str转换为datetime(转换后没有时区信息)
time_str1 = '2019-11-26 10:24:32'
cday = datetime.strptime(time_str1,'%Y-%m-%d %H:%M:%S')
print(cday)

#datetime转换为str
print(now.strftime('%a, %b %d %H:%M:%S'))

#datetime加减
time1 = now + timedelta(hours=10)
print(time1,type(time1))
time2 = now - timedelta(days=1)
print(time2,type(time2))
time3 = now + timedelta(days=2, hours=12)
print(time3,type(time3))

#本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))  #创建时区UTC+8:00
time4 = now.replace(tzinfo=tz_utc_8)  #强制设置为UTC+8:00
print(time4)

#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  #拿到UTC时间，并强制设置时区为UTC+0:00
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  #UTC时间转换为北京时间
print(bj_dt)
tokyo_dt1 = utc_dt.astimezone(timezone(timedelta(hours=9)))  #UTC时间转换为东京时间
print(tokyo_dt1)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))  #北京时间转换为东京时间
print(tokyo_dt2)

