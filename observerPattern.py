#coding:utf-8
# 說明：
#	觀察者模式（有時又被稱為發布/訂閱模式）是軟體設計模式的一種。
#	在此種模式中，一個目標物件管理所有相依於它的觀察者物件，並且在它本身的狀態改變時主動發出通知。
#	這通常透過呼叫各觀察者所提供的方法來實現。此種模式通常被用來實作事件處理系統。


# 觀察者：當被觀察的物件發送事件的時候觀察者會收到訊息
class Observer(object):
	def __init__(self,name):
		self.name=name

	# 當官者被提醒的時候
	def notify(self,event,who):
		print self.name+' observer is notified with Event: '+event+' by instance named is '+who

# 目標物件：內涵所有觀察者的指標並統一管理。
class Component(object):
	# 參考 js 部分把觀察者管理模式寫入目標物件
	def addObserver(self,observer):
		self.observers.append(observer)

	def removeObserver(self,observer):
		self.observers.remove(observer)

	def trigger(self,event):
		for i in self.observers:
			i.notify(event,self.name)	# 由誰觸發

	def __init__(self,name):
		self.name=name
		self.observers=[]

# 建立觀察者
observerWindow=Observer('window')
observerPanel=Observer('panel')

# 建立一個元件然後增加他的觀察者
componentA=Component('button')

# 讓元件受到觀察者監看
componentA.addObserver(observerWindow)
componentA.addObserver(observerPanel)

# 從元件內移除觀察者監看
componentA.removeObserver(observerWindow)

# 模擬觸發事件
componentA.trigger('click')
componentA.trigger('mouseover')


