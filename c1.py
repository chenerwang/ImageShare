import random
import re


# !usr/bin/env python
# _*_ coding:utf-8 _*_


def demo_set():
    seta = set((1, 2, 3))
    setb = set((2, 3, 4))
    print(1, seta.intersection(setb))
    print(seta & setb)
    print(2, seta.union(setb))
    print(seta | setb)


def demo_random():
    # random.seed(1)
    print(1, random.random())
    print(2, random.randint(0, 200))
    print(3, random.choice(range(0, 100)))
    print(4, random.sample(range(0, 100), 4))
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(5, a)


def demo_re():
    str = 'abd123def12gh15'
    p = re.compile('[\d]+')
    p2 = re.compile('\d')
    print(1, p.findall(str))
    print(2, p2.findall(str))

    str = 'a@163.com;b@gmail.com;c@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print(3, p3.findall(str))

    str = '<html><h>title</h><body>xxxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print(4, p4.findall(str))
    p5 = re.compile('<h>([^<]+)</h>')
    print(5, p5.findall(str))

    str = 'xx2016-06-11yy'
    p6 = re.compile('\d\d\d\d-\d\d-\d\d')
    print(6, p6.findall(str))
    p7 = re.compile('\d{4}-\d{2}-\d{2}')
    print(7, p7.findall(str))


if __name__ == '__main__':
    # print('hello world')
    # demo_set()
    # demo_random()
    demo_re()
