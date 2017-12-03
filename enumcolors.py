from enum import Enum
class Color(Enum):
     red = 1
     green = 2
     blue = 3

try:
	Color.blue = "stuff"
	print(Color.blue)
except Exception as e:
	print('No blue variable exists')
finally:
	print(Color.blue)
