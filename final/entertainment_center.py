import fresh_tomatoes
import media

with open("bestFilms.txt") as fin:
    rawData = fin.readlines()

rawData = [element.strip('\n') for element in rawData]

movieData = []

movieData = [element.split('; ') for element in rawData]

for element in movieData:
    element[1] = "images/"+element[1]
    element[2]= "https://www.youtube.com/watch?v="+element[2]
    element[3] = element[3].split(', ')

movieList = []

for element in movieData:
    movieList.append( media.Movie(element[0],element[1],element[2],element[3],element[4],element[5]) )

fresh_tomatoes.open_movies_page(movieList)
