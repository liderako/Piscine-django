def read():
	f = open("numbers.txt", 'r')
	res = f.read()
	return res.split(',')

def run():
	reabBuffer = read()
	for x in reabBuffer:
		print (x)

if __name__ == '__main__':
    run()