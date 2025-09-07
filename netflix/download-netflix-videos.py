# pip install netflix
# https://pypi.org/project/netflix/

from netflix import Movie, TVShow

movie = Movie("81516447", fetch_instantly=False)
#print(movie.name)
movie.fetch()

#tv_show = TVShow("80192098")
#print(tv_show.name)  # 'Money Heist'