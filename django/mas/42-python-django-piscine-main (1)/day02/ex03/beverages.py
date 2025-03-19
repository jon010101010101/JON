class HotBeverages:
	def __init__(self):
		self.price = 0.30
		self.name = "hot beverage"
	def description(self):
		return "Just some hot water in a cup."
	def __str__(self):
		des = self.description()
		n = self.name
		p = '%.2f' % self.price
		s = "name : " + n + "\nprice : " + p + "\ndescription : " + des
		return s

class Coffee(HotBeverages):
	def __init__(self):
		super().__init__()
		self.name = "coffee"
		self.price = 0.40
	def description(self):
		return "A coffee, to stay awake."

class Tea(HotBeverages):
	def __init__(self):
		super().__init__()
		self.name = "tea"

class Chocolate(HotBeverages):
	def __init__(self):
		super().__init__()
		self.name = "chocolate"
		self.price = 0.50
	def description(self):
		return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverages):
	def __init__(self):
		super().__init__()
		self.name = "cappuccino"
		self.price = 0.45
	def description(self):
		return "Un po' di Italia nella sua tazza!"

def test():
	print(HotBeverages())
	print(Coffee())
	print(Tea())
	print(Chocolate())
	print(Cappuccino())


if __name__ == '__main__':
	test()
