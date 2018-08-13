#!usr/bin/env python
# -*- coding:utf-8 -*-

from flask_script import Manager
from c2 import app

manager = Manager(app)


@manager.option('-n', '--name', dest='name', default='hahaha')
def hello(name):
    print('hello' + name)


@manager.command
def initialize():
    'initialize database'
    print('database...')


if __name__ == '__main__':
    manager.run()
