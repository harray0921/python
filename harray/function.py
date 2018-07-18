'''
Python内置了很多有用的函数，我们可以直接调用。
要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
http://docs.python.org/3/library/functions.html#abs
也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
调用abs函数：
'''
import sys
import math
print(abs(100))
print(abs(-100))
print(abs(-12.34))
# 而max函数max()可以接收任意多个参数，并返回最大的那个：
print(max(2, 3, 1, -5))
'''
数据类型转换
Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
'''
print(int('123'))
print(float('12.34'))
print(str(1.23))
print(bool(''))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
'''
空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：
'''
def nop():
    pass
'''
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
pass还可以用在其他语句里，比如：
'''
age = 20
if age >= 18:
    pass
'''
缺少了pass，代码运行就会有语法错误。
参数检查
调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
'''
'''
参数检查
调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
'''
# my_abs(1, 2) 会报错
'''
当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
'''
'''
# 有问题
def my_abs2(x):
    if not isinstance(x, (int, float)):
    	pass
    if x >= 0:
        return x
    else:
        return -x
my_abs2('A')
'''
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)
'''
小结
定义函数时，需要确定函数名和参数个数；
如果有必要，可以先对参数的数据类型做检查；
函数体内部可以用return随时返回函数结果；
函数执行完毕也没有return语句时，自动return None。
函数可以同时返回多个值，但其实就是一个tuple。
'''
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
print(power(5,3))
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')    
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
print(calc(*nums))    
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(100))
'''
小结
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
'''
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(5, 1))   
print(fact_iter(600, 1))   
''' 
尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
'''
# 汉诺塔问题
# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(4, 'A', 'B', 'C')
# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(10) =', fact(10))



