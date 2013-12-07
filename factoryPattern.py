# coding:utf-8
# 工廠模式
# 通常是利用工廠類來建立其他生產類並該方法返回被生產類實例。
# 實質是「定義一個建立物件的介面，但讓實作這個介面的類來決定例項化哪個類。工廠方法讓類的例項化推遲到子類別中進行。」
# 實際應用條件在於：讓工廠把問題統合，把主要的流程控制都寫在工廠內，例如作業系統就是一個工廠，我們要開啟應用程式都是透過作業系統去呼叫( 基本上你也沒辦法寫語言開啟程式XD )

# 零件群
class winButton(object):
	def __init__(self):
		print 'winButton created!'

class macButton(object):
	def __init__(self):
		print 'macButton created!'

# 工廠
class buttonFactory(object):
	def buildWinButton(self):
		return winButton()

	def buildMacButton(self):
		return macButton()

# 建立工廠
myFactory=buttonFactory()

# 生產零件
myButton1=myFactory.buildWinButton()
myBytton2=myFactory.buildMacButton()