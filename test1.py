# coding:utf8
__author__ = 'minqk'

class Animal(object):
    def eat(self):
        print("吃")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    def cry(self):
        print("叫")



class A(object):
    def __init__(self):
        print(1)

class B(A):
    def __init__(self):
        print(2)

class C(B):
    def __init__(self):
        print(super(C, self).__module__)

