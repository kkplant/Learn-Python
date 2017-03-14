#for循环
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素都迭代出来
#句式：for x in ...,循环就是把每个元素代入变量x，然后执行缩进块的语句，直到迭代完毕
age=[1,3,5,7,11,13,17,19]
for i in age:
    print(i)

sum=0
for i in age:
    sum=sum+i
    print(sum)

#函数range(x),可以用来生成一个整数序列，从0到x-1个数
i=range(3)
for x in i:
    print(x)

#求和0~100求和
sum=0
nums=list(range(101))          #这里序列要转换成list
for x in nums:
    sum=sum+x
print(sum)

sum=0
for x in range(101):
    sum=sum+x
print(sum)

#while循环，只要条件满足，就不断循环，条件不满足时退出循环
#计算100以内的奇数之和
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

sum=0
m=1
while m<100:
    sum=sum+m
    m=m+2
print(sum)

#练习
#利用循环依次对list中的每个名字打印出Hello, xxx!：
L=['Bart','Lisa','Adam']
for name in L:
    print('Hello,',name,'!')

#break
#在循环中，break语句可以提前退出循环

