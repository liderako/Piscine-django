import pickle
import random
from django.conf import settings
from game.api import Data

class DataStorage:

	def __init__(
				self,
				positionPlayer=list(),
				amountMovieBall=150,
				listMovieId=list(),
				dataMovieIMDB=None,
				selectedMenuItemIndex=0
			):

		self.positionPlayer = positionPlayer
		if (len(self.positionPlayer)) == 0:
			self.positionPlayer = settings.DEFAULT_START_PLAYER_POSITION
		self.amountMovieBall = amountMovieBall
		self.listMovieId = listMovieId
		self.dataMovieIMDB = dataMovieIMDB
		self.selectedMenuItemIndex = selectedMenuItemIndex
		settings.BALLS = amountMovieBall

	### gets
	def 	getPositionPlayer(self):
		return (self.positionPlayer)

	def 	getAmountMovieBall(self):
		return (self.amountMovieBall)

	def 	getListMovieName(self):
		return (self.listMovieId)

	def 	getMoviesById(self):
		d = Data()
		arr = self.getListMovieName()
		xxx = d.getMoviesById(arr)
		return (xxx)

	def 	getDataMovie(self):
		return (self.dataMovieIMDB)

	def 	get_movie(self):
		return (self.getDataMovie())

	def 	getSelectedMenuItemIndex(self):
		return (self.selectedMenuItemIndex)
	###  sets
	def 	setPositionPlayer(self, positionPlayer):
		self.positionPlayer = positionPlayer

	def 	setAmountMovieBall(self, amountMovieBall):
		self.amountMovieBall = amountMovieBall
		settings.BALLS = amountMovieBall

	def 	setListMovieId(self, listMovieId):
		self.listMovieId = listMovieId

	def 	setDataMovieIMDV(self, dataMovieIMDB):
		self.dataMovieIMDB = dataMovieIMDB

	def 	setSelectedMenuItemIndex(self, index):
		self.selectedMenuItemIndex = index


	def 	addAmountMovieBall(self):
		self.amountMovieBall = self.amountMovieBall + 1
		settings.BALLS = settings.BALLS + 1

	def 	removeAmountMovieBall(self):
		self.amountMovieBall = self.amountMovieBall - 1
		settings.BALLS = settings.BALLS - 1

	### methods
	def 	dump(self, filename="data.pickle"):
		dictData = {
			"positionPlayer"		: self.getPositionPlayer(),
			"amountMovieBall"		: self.getAmountMovieBall(),
			"listMovieId"			: self.getListMovieName(),
			"dataMovieIMDB"			: self.getDataMovie(),
			"selectedMenuItemIndex"	: self.getSelectedMenuItemIndex()
		}
		pickling_on = open(filename,"wb")
		pickle.dump(dictData, pickling_on)
		pickling_on.close()

	def 	load(self, filename="data.pickle"):
		pickle_off = open(filename,"rb")
		dictData = pickle.load(pickle_off)
		return (dictData)

	def 	load_default_settings(self):
		self.positionPlayer = settings.DEFAULT_START_PLAYER_POSITION
		self.amountMovieBall = settings.DEFAULT_AMOUNT_BALL
		self.listMovieId = list()
		self.dataMovieIMDB = self.load_IMDB()
		self.selectedMenuItemIndex = 0

	def 	get_random_movie(self):
		d = Data()
		return (d.get_random_movie())

	def 	get_movie(self, name):
		d = Data()
		d.get_movie(name)
		return (d)

	def 	printO(self):
		print(self.positionPlayer)
		print(self.amountMovieBall)
		print(self.listMovieId)
		# print(self.dataMovieIMDB)

	def 	get_strength(self):
		return (len(self.listMovieId) + 1)

	def 	load_IMDB(self):
		d = Data()
		return (d.get())

	def 	coefBattle(strengthEnemy): #, strengthPlayer):
		strengthPlayer = self.get_strength()
		c = 50 - (strengthEnemy * 10) + (strengthPlayer * 5)
		if (c <= 1):
			return (1)
		elif (c >= 90):
			return (90)
		return (c)

	def 	addListMovieId(self, listMovieId):
		self.listMovieId.append(listMovieId)
