# coding:utf-8

# 選代器模式
# 情境說明：
#	通常在 C++ 的 STL 容器內會很常見
#	有點類似 C# 對 ForEach 就面的實作。
# 主要用途：
#	它可以讓使用者透過特定的介面巡訪容器中的每一個元素而不用了解底層的實作( 就無腦調用 next() )。
#	簡單來說就是幫使用者寫好 API 接口。
#	目前看到使實現並使用的大多為資料陣列或是資料群。
#	通常高階語言不大需要你寫這段 Pattern，除非你要客製化！

# 在 python 已經有builtin方法實現陣列選代了, 可用 iter() 來實現

store=[1,2,3,4]
print store
iStore=iter(store)

try:
	while True:
		print iStore.next()
except StopIteration:
	print 'iteration end!'

############################################## 手動實現 #####################################################

class abstractInterator(object):
	currentIndex=None
	
	def next(self):
		raise NotImplementedError("You must override this abstract method!")

	def prev(self):
		raise NotImplementedError("You must override this abstract method!")

	def current(self):
		raise NotImplementedError("You must override this abstract method!")

	def first(self):
		raise NotImplementedError("You must override this abstract method!")

	def last(sefl):
		 raise NotImplementedError("You must override this abstract method!")

# 繼承 list 並實現選代介面
class dataStore(list,abstractInterator):
	def __init__(self,*args):
		for i in args:self.append(i)
		if len(self)>0:self.currentIndex=0

	def current(self):
		if self.currentIndex==None:return None
		else:return self[self.currentIndex]

	def next(self):
		try:
			self.currentIndex+=1
			return self[self.currentIndex-1]
		except:return None

	def prev(self):
		try:
			if self.currentIndex>0:
				self.currentIndex-=1
				return self[self.currentIndex]
			else:return None
		except:return None

	def first(self):
		try:return self[0]
		except:return None

	def last(self):
		try:return self[len(self)-1]
		except:return None
	

a=dataStore(10,20,30,50)

print a.first()
print a.last()
print a.prev()
print 
print a.next()
print a.current()
print a.prev()
print 
print a.next()
print a.next()
print a.next()
print a.next()