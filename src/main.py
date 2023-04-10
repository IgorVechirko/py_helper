from decorator import printFuncNameDecorator

@printFuncNameDecorator
def numericTypes(x, y):

	print('int')

	x = int(x)
	y = int(y)

	if x < y:
		print(x)

	if y > x:
		print(y)

	print(abs(x))

	print('float')

	x = float(x)
	y = float(y)

	if x <= y:
		print(x)

	if y >= x:
		print(y)

	print(abs(x))

	print('complex')

	x = complex(x)
	y = complex(y)

	if x != y:
		print(x+y)

	if x == y:
		print(x-y)

	print(abs(x))


@printFuncNameDecorator
def boolTypes(x:bool, y:bool):

	if x or y:
		print('or')

	if x and not y:
		print('and')

	if not y:
		print('not')

	if x is y:
		print('is')

	if x is not y:
		print('is not')




numericTypes(-1.2, 2.2)
boolTypes(True, False)




class SelfException(BaseException):
	
	def __init__(self):
		pass