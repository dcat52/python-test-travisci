class MyObject:
	def __init__(self):
		self.x = 1
		self.a = [1,2,3]

	def getShallowArray(self):
		return self.a

	def getDeepArray(self):
		return self.a[:]