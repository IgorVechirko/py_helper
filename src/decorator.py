def printFuncNameDecorator(func):
	def wrapper(*args, **kwargs):
		print('')
		print('>>',func.__name__)
		result = func(*args, **kwargs)
		print('<<',func.__name__)
		return result
	
	return wrapper