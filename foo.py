x = 1

def bar():
	print('Im the bar function within foo.py')

class spam(object):
	def hello(self):
		print('I am the hello function inside spam class of the foo.py module')


if __name__ == "__main__":
	bar()

