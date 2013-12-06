# coding: utf-8
# 情境：
# 有一个画板（toolbar）可以从中取到两种图形：
# 	圆型（circle）和矩形（rectangle）它们都属于原型（Prototype）,
# 	当客户需要画一个图形时便从画板中去一个图形，原型模式的关键就在于画板克隆一个图形对象，然后返回给客户。
# 	如果你的 Class 建構函式有非常複雜的建構程序，建議可以使用 Prototype Pattern。

import copy		# 用來實現 clone

class polygonAbstract(object):
	def clone(self):
		return copy.copy(self)

	def getName(self):
		raise NotImplementedError("You must override this abstract method!")

class rectangle(polygonAbstract):
	def getName(self):
		print "i'm rectangle",self

class cylinder(polygonAbstract):
	def getName(self):
		print "i'm cylinder",self

r=rectangle()		# as prototype Instance
r2=r.clone()		# duplicate from prototype instance
c=cylinder()

r.getName()
r2.getName()


