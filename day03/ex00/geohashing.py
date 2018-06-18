import sys
import antigravity

def 	run(argc, argv):
	try:
		if (argc != 4):
			raise Exception("Usage: python3 geohashing.py latitude longitude datedow\nExample: python3 geohashing.py 37.421542, -122.085589, \"2005-05-26-10458.68\"")
		latitude = argv[1]
		longitude = argv[2]
		datedow = argv[3]
		antigravity.geohash(float(latitude), float(longitude), bytes(datedow, 'utf-8'))
	except Exception as e:
		print (e)

if __name__ == '__main__':
    run(len(sys.argv), sys.argv)