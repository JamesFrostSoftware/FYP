import pandas as pd
import numpy as np
import math
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Movie
from app1.forms import MovieSearchForm

def home (request):
    context = {
        'movies': Movie.objects.all()
    }
    return render(request, 'app1/home.html', context)

class MovieListView(ListView):
    model = Movie
    template_name = 'app1/home.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'desc', 'releaseDate']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def getASuggestion(request):
    return render(request, 'app1/getASuggestion.html', {'title': 'getASuggestion'})
    
class MovieCompare(ListView):
    model = Movie
    template_name = 'app1/testing.html'
    context_object_name = 'movies'


class SuggestionView(TemplateView):
    template_name = 'app1/getASuggestion2.html'

    def get(self, request):
        form = MovieSearchForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            text = request.POST.get('movie_name')
            og = request.POST.get('movie_name')
            text2 = ''
            text3 = ''
            text4 = ''
            text5 = ''
            text6 = ''
            text.lower()
            def getTitleIndex(index):
                return csv_reader[csv_reader.index == index]["title"].values[0]
            def getIndexTitle(title):
                return csv_reader[csv_reader.title == title]["index"].values[0]
            def getHomePage(index):
                return csv_reader[csv_reader.index == index]["homepage"].values[0]
            def getOverview(index):
                return csv_reader[csv_reader.index == index]["overview"].values[0]
            def getDirector(index):
                return csv_reader[csv_reader.index == index]["director"].values[0]
            def getCast(index):
                return csv_reader[csv_reader.index == index]["cast"].values[0]
            def getTagline(index):
                return csv_reader[csv_reader.index == index]["tagline"].values[0]
            def getRuntime(index):
                return csv_reader[csv_reader.index == index]["runtime"].values[0]
            csv_reader = pd.read_csv(r"C:\Users\james\fypWeb\app1\movie_dataset.csv")
            att = ['keywords', 'cast', 'genres', 'director', 'release_date', 'original_language']
            for att in att:
                csv_reader[att] = csv_reader[att].fillna('')
            def combine_att(row):
                try:
                    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director'] + " " + row['release_date'] + " " + row['original_language']
                except:
                    print('Error : ', row)
            csv_reader["combine_att"] = csv_reader.apply(combine_att, axis=1)
            cv = CountVectorizer()
            count_matrix = cv.fit_transform(csv_reader["combine_att"])
            cosine_sim = cosine_similarity(count_matrix)
            try:
                movie_index = getIndexTitle(text)
                similar_movies = list(enumerate(cosine_sim[movie_index]))
                original_m = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies2 = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies3 = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies4 = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies5 = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                sorted_similar_movies6 = iter(sorted(similar_movies, key= lambda x:x[1], reverse=True))
                next(sorted_similar_movies) 
                next(sorted_similar_movies2)
                next(sorted_similar_movies2)
                next(sorted_similar_movies3)
                next(sorted_similar_movies3)
                next(sorted_similar_movies3)
                next(sorted_similar_movies4)
                next(sorted_similar_movies4)
                next(sorted_similar_movies4)
                next(sorted_similar_movies4)
                next(sorted_similar_movies5)
                next(sorted_similar_movies5)
                next(sorted_similar_movies5)
                next(sorted_similar_movies5)
                next(sorted_similar_movies5)
                next(sorted_similar_movies6)
                next(sorted_similar_movies6)
                next(sorted_similar_movies6)
                next(sorted_similar_movies6)
                next(sorted_similar_movies6)
                next(sorted_similar_movies6)
                i=0
                for movie in sorted_similar_movies:
                    print (getTitleIndex(movie[0]))
                    text = (getTitleIndex(movie[0]))
                    homepage = (getHomePage(movie[0]))
                    overview = (getOverview(movie[0]))
                    director = (getDirector(movie[0]))
                    cast = (getCast(movie[0]))
                    tagline = (getTagline(movie[0]))
                    runtime = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break 
                for movie in sorted_similar_movies2:
                    print (getTitleIndex(movie[0]))
                    text2 = (getTitleIndex(movie[0]))
                    homepage2 = (getHomePage(movie[0]))
                    overview2 = (getOverview(movie[0]))
                    director2 = (getDirector(movie[0]))
                    cast2 = (getCast(movie[0]))
                    tagline2 = (getTagline(movie[0]))
                    runtime2 = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break         
                for movie in sorted_similar_movies3:
                    print (getTitleIndex(movie[0]))
                    text3 = (getTitleIndex(movie[0]))
                    homepage3 = (getHomePage(movie[0]))
                    overview3 = (getOverview(movie[0]))
                    director3 = (getDirector(movie[0]))
                    cast3 = (getCast(movie[0]))
                    tagline3 = (getTagline(movie[0]))
                    runtime3 = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break
                for movie in sorted_similar_movies4:
                    print (getTitleIndex(movie[0]))
                    text4 = (getTitleIndex(movie[0]))
                    homepage4 = (getHomePage(movie[0]))
                    overview4 = (getOverview(movie[0]))
                    director4 = (getDirector(movie[0]))
                    cast4 = (getCast(movie[0]))
                    tagline4 = (getTagline(movie[0]))
                    runtime4 = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break  
                for movie in sorted_similar_movies5:
                    print (getTitleIndex(movie[0]))
                    text5 = (getTitleIndex(movie[0]))
                    homepage5 = (getHomePage(movie[0]))
                    overview5 = (getOverview(movie[0]))
                    director5 = (getDirector(movie[0]))
                    cast5 = (getCast(movie[0]))
                    tagline5 = (getTagline(movie[0]))
                    runtime5 = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break 
                for movie in sorted_similar_movies6:
                    print (getTitleIndex(movie[0]))
                    text6 = (getTitleIndex(movie[0]))
                    homepage6 = (getHomePage(movie[0]))
                    overview6 = (getOverview(movie[0]))
                    director6 = (getDirector(movie[0]))
                    cast6 = (getCast(movie[0]))
                    tagline6 = (getTagline(movie[0]))
                    runtime6 = (getRuntime(movie[0]))
                    i=i+1
                    if i>0:
                        break 
            except:
                og = ''
                text = 'Not on our system, please try another film'
                text2 = ''
                text3 = ''
                text4 = ''
                text5 = ''
                text6 = ''
        if (not homepage or pd.isnull(homepage)):
            homepage = '#No-website-available'
        if (not homepage2 or pd.isnull(homepage2)):
            homepage2 = '#No-website-available'
        if (not homepage3 or pd.isnull(homepage3)):
            homepage3 = '#No-website-available'
        if (not homepage4 or pd.isnull(homepage4)):
            homepage4 = '#No-website-available'
        if (not homepage5 or pd.isnull(homepage5)):
            homepage5 = '#No-website-available'
        if (not homepage6 or pd.isnull(homepage6)):
            homepage6 = '#No-website-available'
        
        argsText = {'form': form, 'og': og, 'text': text, 'text2': text2, 'text3': text3, 'text4': text4, 'text5': text5, 'text6': text6}
        argsWeb = {'homepage': homepage, 'homepage2': homepage2, 'homepage3': homepage3, 'homepage4': homepage4, 'homepage5': homepage5, 'homepage6': homepage6}
        argsDesc = {'overview': overview, 'overview2': overview2, 'overview3': overview3, 'overview4': overview4, 'overview5': overview5, 'overview6': overview6}
        argsDirector = {'director': director, 'director2': director2, 'director3': director3, 'director4': director4, 'director5': director5, 'director6': director6}
        argsCast = {'cast': cast, 'cast2': cast2, 'cast3': cast3, 'cast4': cast4, 'cast5': cast5, 'cast6': cast6}
        argsTagline = {'tagline': tagline, 'tagline2': tagline2, 'tagline3': tagline3, 'tagline4': tagline4, 'tagline5': tagline5, 'tagline6': tagline6}
        argsRuntime = {'runtime': runtime, 'runtime2': runtime2, 'runtime3': runtime3, 'runtime4': runtime4, 'runtime5': runtime5, 'runtime6': runtime6}
        args = {**argsText, **argsWeb, **argsDesc, **argsDirector, **argsCast, **argsTagline, **argsRuntime}        
        return render(request, self.template_name, args)