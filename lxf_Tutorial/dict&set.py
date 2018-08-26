#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入

#初始化dict
d={'a':1,'b':2,'c':3}
#取值
d['a']
#将键值放入dict
d['d']=4
#一个键（key）对应一个值（value），多次对一个key放入value，后面的值会把前面的值冲掉
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
'e' in d
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value,返回None的时候Python的交互式命令行不显示结果
d.get('e',0)
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('d')

#dict内部存放的顺序和key放入的顺序是没有关系的
#需要牢记的第一条就是dict的key必须是不可变对象，如字符串、整数，list是可变的，不能作为key，tuple可以


#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#创建set，需要提供一个list作为输入集合
s=set([1,2,3,])

i=[4,5,6]
s=set(i)

#重复元素在set中自动被过滤
s=set([1,1,2,3,3,4])

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(5)

#通过remove(key)方法可以删除元素
s.remove(5)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1=set([1,2,3,5])
s2=set([2,5,4])
s1&s2
s1|s2

#set和dict的唯一区别仅在于没有存储对应的value,同样不可以放入可变对象
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的


