#-*- coding:utf-8 -*-
print('秒数转换为时分秒')
time=input('请输入秒数：')
time1=int(time)
if time1>=0 and time1<60:
    time1_sec=time1
    print("%s秒" %time1_sec)
    #print("00:00:%s" %time_sec1)
elif time1>=60 and time1<3600:
    time2=time1
    time2_min=time2//60
    time2_sec=time2-time2_min*60
    print('%s分%s秒' %(time2_min,time2_sec))
    #print("00:%s:%s" %(time2_min,time2_sec))
elif time1>=3600 and time1<86400:
    time3=time1
    time3_hour=time3//3600
    time3_min=(time3-time3_hour*3600)//60
    time3_sec=time3-time3_hour*3600-time3_min*60
    print('%s时%s分%s秒' %(time3_hour,time3_min,time3_sec))
elif time1>=86400:
    time4=time1
    time4_day=time4//86400
    time4_hour=(time4-time4_day*86400)//3600
    time4_min=(time4-time4_day*86400-time4_hour*3600)//60
    time4_sec=time4-time4_day*86400-time4_hour*3600-time4_min*60
    print('%s天%s时%s分%s秒' %(time4_day,time4_hour,time4_min,time4_sec))
else:
    print('请输入正确秒数')    
    
