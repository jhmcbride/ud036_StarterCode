""" Stores the info of the movies and runs fresh_tomatoes - which generates
the webpage to display the content."""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie ("Avatar",
                      "A Marine on an Alien Planet",
                      "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")

city_of_god = media.Movie("City of God",
                          "One boys strugle in the slums of Rio",
                          "https://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg",
                          "https://www.youtube.com/watch?v=ioUE_5wpg_E")

life_is_beautiful = media.Movie("Life is Beautiful",
                               "A father and sons journey during WWII",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Vitaebella.jpg/220px-Vitaebella.jpg",
                               "https://www.youtube.com/watch?v=zqAVwCK4r2Q")

boy = media.Movie("boy",
                  "A kid growing up with no father finally meets his hero",
                  "https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/Boy2010movieposter.jpg/220px-Boy2010movieposter.jpg",
                  "https://www.youtube.com/watch?v=Qpu0p5ldDS4")

baby_driver = media.Movie("Baby Driver",
                          "A young man learns hard lessons in his life of crime",
                          "https://upload.wikimedia.org/wikipedia/en/8/8e/Baby_Driver_poster.jpg",
                          "https://www.youtube.com/watch?v=z2z857RSfhk")

"""List to store the names of the instances of the movies."""
movies = [toy_story, avatar, city_of_god, life_is_beautiful, boy, baby_driver]

"""Runs fresh_tomatoes.py, which generates a webpage to display the movie info."""
fresh_tomatoes.open_movies_page(movies)

