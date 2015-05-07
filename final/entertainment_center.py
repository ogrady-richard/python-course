import fresh_tomatoes
import media

# Open our best films file and read the contents
with open("bestFilms.txt") as fin:
    rawData = fin.readlines()

# Remove trailing new line characters from our data
rawData = [element.strip('\n') for element in rawData]

# Initialize a list for our movie data
movieData = []

# Split our data using the designated semicolon delimited
movieData = [element.split('; ') for element in rawData]

# Iterate through our movie data list to add important data
for element in movieData:
    element[1] = "images/"+element[1]
    element[2]= "https://www.youtube.com/watch?v="+element[2]
    element[3] = element[3].split(', ')

# Initialize a list for our movie objects from our media library
movieList = []

# Iterate through the movie list, creating individual movie objects
for element in movieData:
    movieList.append( media.Movie(element[0],element[1],element[2],element[3]
                                            ,element[4],element[5]) )

# Execute the fresh tomatoes core library function
fresh_tomatoes.open_movies_page(movieList)
