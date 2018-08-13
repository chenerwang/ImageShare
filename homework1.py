'''
 1. 开发环境搭建
    多版本python安装管理：下载、安装、改名、添加环境变量
    pycharm：设置解释器，连接Git
 2. pycharm菜单里每个按钮的熟悉
 3. pip install xxx
    pip uninstall xxx
'''

'''
4. python基础语法练习
'''

# 单行注释
'''多行注释'''
"""多行注释"""


# 字符串
def demo_str():
    stra = 'hello,worlD'
    print(1, stra.capitalize())
    print(2, stra.endswith('ld'))
    print(3, stra.find('lo'))
    strb = '  \n\n\r hahaha\n\r\n '
    print(4, strb.lstrip())
    print(5, strb.lstrip())
    print(6, stra.replace('ell', 'aaa'))
    print('---------------我是分割线-------------')


# 运算符
def demo_operation():
    a = 5
    b = 3
    print(1, a + b, a - b, a * b, a / b, a // b, a ** b, a % b)
    print(2, a > b, a < b, a != b)
    print(3, a & b, a | b, b ^ a, ~a, a << b, a >> b)
    print('------------------我是分割线------------')


# 内置函数
def demo_builtin():
    a = -3
    b = 'hello'
    print(1, abs(a))
    print(2, type(b))
    print(3, chr(97), ord('a'))
    print(4, range(0, 100, 20))
    print(5, len(b))
    print((6, eval('a*3')))
    print('----------------------------我是分割线---------------------')


# 控制流
def demo_control():
    x = 93
    if x > 90:
        print('nice')
    elif x < 60:
        print('bad')
    else:
        print('just so so')

    animals = ['cat', 'dog', 'cow']
    for a in animals:
        print(a)
    print()

    for a in range(5):
        print(a)
    print()

    for a in range(10):
        if a < 6:
            continue
        print(a)
        if a > 7:
            break


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# 数据结构
def demo_data():
    lista = [1, 2, 3]
    print(1, lista)
    listb = ['a', 1, 'c', 1.3]
    print(2, listb)
    lista.extend(listb)
    print(3, lista)
    print(4, len(listb))
    print(5, 'a' in listb)
    lista = lista + listb
    print(6, lista)
    lista.insert(0, 'new')
    print(7, listb)
    listb.pop(1)
    print(8, listb)
    listb.reverse()
    print(9, listb)
    print(10, listb[0], listb[1])
    listb = [1, 2, 5, 8]
    listb.sort()
    print(11, listb)
    listb.sort(reverse=True)
    print(12, listb)
    print(13, listb * 2)
    print(14, [0] * 14)
    tuplea = (1, 2, 3)
    listc = [1, 2, 3]
    listc.append(4)
    print(15, listc)
    print('---------------------我是分割线-------------------')

    dicta = {4: 16, 1: 1, 2: 4, 3: 9}
    print(1, dicta)
    print(2, dicta.keys(), dicta.values())
    for key, value in dicta.items():
        print(key, value)
    dictb = {'+': add, '-': sub}
    print(3, dictb['+'](1, 2))
    print(4, dictb['-'](8, 2))
    del dicta[1]
    print(5,dicta)
    print('------------------我是分割线------------------')
    seta=set([1,2,3])
    setb=set((2,3,4))
    print(1,seta)
    print(2, seta.intersection(setb), seta&setb)
    print(3, seta.union(setb),seta|setb)
    print(4,seta - setb)
    seta.add('x')
    print(5,seta)
    print(6,len(seta))
    print(7,seta.isdisjoint(set((1,2))))
    print('-------------------我是分割线-------------------')


'''
5. 随机数、正则表达式练习
'''

if __name__ == '__main__':
    demo_str()
    demo_operation()
    demo_builtin()
    demo_control()
    demo_data()
