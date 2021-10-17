import os
import pandas as pd

class vending_machine:


	def __init__(self,name):
	
		self.name = name
		self.path = os.getcwd() + "/classes/vending_machine"
		
		
	def getName(self):
	
		return self.name
		
		
	def getDataPath(self):
	
		dataPath = self.path + "/data"
		
		return dataPath
		
		
	def getWelcomeMessage(self):
	
		path = self.getDataPath() + "/welcome_message.txt"
		welcomeMessage = open(path, 'r').read()
		
		return welcomeMessage
		
		
	def printWelcomeMessage(self):
	
		print(self.getWelcomeMessage().format(self.getName()))
		
		return None
		
		
	def getStockDataPath(self):
	
		stockDataPath = self.getDataPath() + "/stock_data.csv"
		
		return stockDataPath
		
		
	def printStockOptions(self):
	
		stockData = pd.read_csv(self.getStockDataPath())
		
		for i in range(len(stockData)):
			print("{}: {}".format(stockData["stock_id"][i], stockData["name"][i]))
		
		return None
		
	
		
		 
