import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from forms import MovieSearchForm

class SuggestionView(TemplateView):
    template_name = 'app1/getASuggestion2.html'

    def get(self, request):
        form = MovieSearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = MovieSearchForm()
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def findSimilarMovies():
	def getTitleIndex(index):
		return csv_reader[csv_reader.index == index]["title"].values[0]
	def getIndexTitle(title):
		return csv_reader[csv_reader.title == title]["index"].values[0]
	csv_reader = pd.read_csv("movie_dataset.csv")
	att = ['keywords', 'cast', 'genres', 'director', 'release_date']
	for att in att:
		csv_reader[att] = csv_reader[att].fillna('')
	def combine_att(row):
		try:
			return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director'] + " " + row['release_date']
		except:
			print('Error : ', row)
	csv_reader["combine_att"] = csv_reader.apply(combine_att, axis=1)
	cv = CountVectorizer()
	count_matrix = cv.fit_transform(csv_reader["combine_att"])
	cosine_sim = cosine_similarity(count_matrix)
	movie_index = getIndexTitle(movie_name)
	similar_movies = list(enumerate(cosine_sim[movie_index]))
	sorted_similar_movies = sorted(similar_movies, key= lambda x:x[1], reverse=True)
	i=0
	for movie in sorted_similar_movies:
		print (getTitleIndex(movie[0]))
		i=i+1
		if i>50:
			break 