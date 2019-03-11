def multiply(a,b):
	return a*b

def oddChars(s):
	assert type(s) == str

	res = ""
	for c in range(0,len(s),2):
		res += s[c]

	return res