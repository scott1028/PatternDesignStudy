# coding:utf-8
# 單例模式
# 情境說明：
#	實現單例模式的思路是：一個類能返回對象一個引用(永遠是同一個)和一個獲得該實例的方法（必須是靜態方法，通常使用getInstance這個名稱）
#	簡單來說就是不允許你建立第二個 instance。使用 static class 來達成此目的
#	基本上不要使用 new mainSystem() 的方式來建立。

class mainSystem(object):
	# 可以直接透過 mainSystem 當作 static variable
	systemHandle=None

	@staticmethod
	def getInstance():
		if(mainSystem.systemHandle==None):
			mainSystem.systemHandle=mainSystem()

		print mainSystem.systemHandle

		return mainSystem.systemHandle

# 都返回同一個 instance
mySys1=mainSystem.getInstance()
mySys2=mainSystem.getInstance()
mySys3=mainSystem.getInstance()
mySys4=mainSystem.getInstance()