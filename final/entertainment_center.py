import fresh_tomatoes
import media

space_jam = media.Movie("Space Jam", "images/space-jam.jpg", "https://www.youtube.com/watch?v=u7AYd8uGG6E", ["Michael Jordan", "Bugs Bunny"], "November 15, 1996")

fresh_tomatoes.open_movies_page([space_jam])
