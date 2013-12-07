# coding:utf-8
# 訪問者模式
# 情境說明：
# 	首先我們擁有一個由許多對象構成的對象結構，這些對象的類都擁有一個accept方法用來接受訪問者對象；訪問者是一個介面，它擁有一個visit方法，這個方法對訪問到的對象結構中不同類型的元素作出不同的反應。
#	基本上就是 一個 instance set 的 class 內必須在實作訪問者該調用自己的哪一個方法來訪問 set 中的每一個子類成員。
#	參考大部分語言的 socket Class 的實現方式。

# 可以在客製化這些類
class foot(object):
	pass

class hand(object):
	pass

class head(object):
	pass

class body(object):
	pass

class human(object):
	def __init__(self):
		self.body=body()
		
		self.foots=[
			foot(),
			foot()
		]

		self.hands=[
			hand(),
			hand()
		]

	# 實作被訪問的時候的行為
	def accept(self,aVisitor):
		aVisitor.visitHuman(self.body)
		for i in self.foots:aVisitor.visitHuman(i)
		for i in self.hands:aVisitor.visitHuman(i)

class visitor(object):
	def visitOthers(self):
		pass

	# 每個被訪的類要實現調用哪一個訪問函式
	def visitHuman(self,part):
		print 'this is a part of human',part

v=visitor()
h=human()

# 當 human 被訪問
h.accept(v)