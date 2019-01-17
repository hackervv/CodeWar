# --coding: utf-8 --
import math
def dig_pow(n,p):
	""" Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k  
		dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
		dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
		dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
		dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
	"""
	# pow(): math模块中 pow(x,y) 返回x的y次方
	# enumerate(): 迭代函数 for i,item in enumerate(string) i为迭代对象的索引，item为具体数据
	s = 0
	for i,c in enumerate(str(n)):
		s += pow(int(c),p+i)
	return s/n if s%n == 0 else -1

print(dig_pow(32,1))