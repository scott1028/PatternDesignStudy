# coding:utf-8
# 以下展式 Python 物件計程特性。
# 大體上與 Ruby 相同，物件但是在父類別呼叫上更類似 JavaScript 一些。

class X(object):
	def doSomething(self):
		print 'base Class X'

class A(X):
	def __init__(self):
		print 'init A'

	def doSomething(self):
		print 'A doSomething...'
		return 100

class B(A):
	def doSomething(self):
		a=super(B,self).doSomething()		# 可以指定為B的父類別同名方法
		print a
		print 'B doSomthing...'
		super(A,self).doSomething()			# 也可指定呼叫A的父類別同名方法

b=B()
b.doSomething()
