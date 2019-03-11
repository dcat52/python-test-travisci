import unittest
from MyObject import MyObject

class TestMyObject(unittest.TestCase):

	def test_obj_creation(self):
		aObj = MyObject()
		bObj = MyObject()
		self.assertIsInstance(aObj, MyObject)
		self.assertNotEqual(aObj, bObj)
		self.assertEqual(aObj.x, 1)

	def test_shallow_copy(self):

		aObj = MyObject()
		sc = aObj.getShallowArray()
		self.assertEqual(sc,aObj.a)
		self.assertEqual(id(sc),id(aObj.a))

	def test_deep_copy(self):

		aObj = MyObject()
		dc = aObj.getDeepArray()
		self.assertEqual(dc,aObj.a)
		self.assertNotEqual(id(dc),id(aObj.a))




if __name__ == '__main__':
	unittest.main()