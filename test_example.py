import unittest
import example

class TestExample(unittest.TestCase):

	def test_mult_3_4(self):
		actual = example.multiply(3,4)
		expected = 12
		self.assertEqual(actual, expected)

	def test_mult_0_0(self):
		actual = example.multiply(0,0)
		self.assertEqual(actual, 0)

	def test_odd_chars_1(self):
		actual = example.oddChars("abcdef")
		self.assertEqual(actual, "ace")

	def test_odd_chars_blank(self):
		actual = example.oddChars("")
		self.assertEqual(actual, "")

	# def test_odd_chars_invalid_parameters(self):
	# 	# example.oddChars(None)
	# 	self.assertRaises(AssertionError, example.oddChars, None)
	# 	# self.assertRaises(AssertionError, example.oddChars, 1)
	# 	# self.assertRaises(AssertionError, example.oddChars, 3.14)
	# 	# self.assertRaises(AssertionError, example.oddChars, [])


if __name__ == '__main__':
	unittest.main()