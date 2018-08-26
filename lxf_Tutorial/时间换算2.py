#-*- coding:utf-8 -*-
print('秒数转换为时分秒')
time=input('请输入秒数：')
time0=int(time)
#参数初始化
time_day=0
time_hour=0
time_min=0
time_sec=0
if time0<0:
    print('秒数不能为负值，请输入正确秒数！')
else:
    #转换为分钟数
    time1=time0//60
    #转换为小时数
    time2=time1//60
    #转换为天数
    time3=time2//24
    time_sec=time0-time1*60
    time_min=time1-time2*60
    time_hour=time2-time3*24
    time_day=time3
#print('%s天%s时%s分%s秒' %(time_day_0,time_hour_0,time_min_0,time_sec_0))
print('%s天%s时%s分%s秒' %(time_day,time_hour,time_min,time_sec))
