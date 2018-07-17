print('hello,word')
print("hello,word")
age = 20
if age >=18:
	print('adult')
else:
	print('teenager')
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
s = 'Python-中文'  #Python 3的字符串使用Unicode，直接支持多语言。当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
classmates = ['Michael', 'Bob', 'Tracy'] #Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
print(len(classmates))
print(classmates)
print(classmates[0]) #用索引来访问list中每一个位置的元素，记得索引是从0开始的：
#当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
classmates.append('Adam') #ist是一个可变的有序表，所以，可以往list中追加元素到末尾：
print(classmates) 
classmates.insert(1, 'Jack') #也可以把元素插入到指定的位置，比如索引号为1的位置：
print(classmates)
classmates.pop() #要删除list末尾的元素，用pop()方法：
print(classmates)
classmates.pop(1) #要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
print(classmates)
classmates[1] = 'Sarah' #要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print(classmates)
L = ['Apple', 123, True] #list里面的元素的数据类型也可以不同，比如：
print(L)
s = ['python', 'java', ['asp', 'php'], 'scheme'] #list元素也可以是另一个list，比如：
print(len(s))
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
# 如果要定义一个空的tuple，可以写成()：

# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
t = (1)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
# 最后来看一个“可变的”tuple：

# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
# 别急，我们先看看定义的时候tuple包含的3个元素：
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
#所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
