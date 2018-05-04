#!/usr/bin/env python
# _*_ coding:utf-8 _*_
class father():
    def call_children(self):
        print self
        child_method = getattr(self, 'out')  # 获取子类的out()方法
        print child_method
        child_method()  # 执行子类的out()方法


class children(father):
    def out(self):
        return 5


# child = children()
# print "childe", child
# d = children.call_children(children())
# print d
