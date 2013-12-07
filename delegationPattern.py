# coding:utf-8
# 情境說明：
#	使用 聚合 來替代繼承。就像開了一個 static class 來當指中介指派類。
#	其實在動態語言也可以直接用 Hash Table 實現。

# 真正工作的類
class realPrinter(object):
	def doPrint(self):
		print 'real printer is printing'

# 當作指派類(delegation)
class printer:
	@staticmethod
	def doPrint():
		p=realPrinter()
		p.doPrint()

	@staticmethod
	def doOthers():
		raise NotImplementedError("You must override this abstract method!")

printer.doPrint()
#printer.doOthers()