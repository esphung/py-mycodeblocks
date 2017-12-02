# -*- coding: utf-8 -*-
# @Author: homeuser
# @Date:   2017-11-29 19:56:01
# @Last Modified 2017-12-02
# @Last Modified time: 2017-12-02 02:38:13
def ASCII(arg):
	key = 0
	for char in arg:
		key += ord(char)

	return key

name = 'eric'
print(name)
print(ASCII(name))