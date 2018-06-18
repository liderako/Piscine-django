from local_lib.path import Path

def 	testMain():
	path = Path("local_lib/")
	# p = path.abspath()
	# path.module = p
	print (path.module)
	# dir_name = path.dirname("test")
	# print (dir_name)
	# path.mkdir(mode=511)
	# print ()

if __name__ == '__main__':
    testMain()