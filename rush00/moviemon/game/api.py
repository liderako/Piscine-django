from django.conf import settings
import requests
import json
import pickle
import random

class Data:

	def get(self):

		self.api_key = '59924f17'
		self.moviedex = []
		self.movielist = []
		
		for name in settings.MOVIES:
			response = requests.get(
				"http://www.omdbapi.com/?apikey="
				+ self.api_key
				+ "&t="
				+ name
				+ "&plot=short&r=json"
			)
			self.movielist.append(json.loads(response.text))
		
		self.dic = {
			"Moviedex": self.moviedex,
			"Movies": self.movielist
		}
		return self.dic

	def getMoviesById(self, arr):

		self.api_key = '59924f17'
		self.moviedex = []
		self.movielist = []
		
		for idnr in arr:
			response = requests.get(
				"http://www.omdbapi.com/?apikey="
				+ self.api_key
				+ "&i="
				+ idnr
				+ "&plot=short&r=json"
			)
			self.movielist.append(json.loads(response.text))
		
		self.dic = {
			"Moviedex": self.moviedex,
			"Movies": self.movielist
		}
		return self.dic

	def get_random_movie(self):
		obj = self.get()
		mv = obj['Movies']
		dex = obj['Moviedex']
		while len(dex) < len(mv):
			var = random.choice(mv)

			count = 0
			for i in dex:
				if dex[i]['Title'] == var['Title']:
					count += 1
			if count == 0:
				return var

	def get_movie(self, name):
		obj = self.get()['Movies']
		for item in obj:
			if item['Title'] == name:
				return item

	def get_movie_by_id(self, id):
		obj = self.get()['Movies']
		for item in obj:
			if item['imdbID'] == id:
				return item
