import media
import fresh_tomatoes


# Movies
# Below are the instances for the movies section,
# You can make changes in this section to add/remove/edit information of movies

# Toy Story Movie: title, duration, genres, storyline, poster, trailer
toy_story = media.Movie(
    "Toy Story",
    "1h 21min",
    ["Fantasy", "Adventure", "Animation"],
    "A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
    "https://www.youtube.com/watch?v=vwyZH85NQC4",  # NOQA
    1995
    )

# Avatar Movie: title, duration, genres, storyline, poster, trailer
avatar = media.Movie(
    "Avatar",
    "2h 42min",
    ["Action", "Adventure", "Fantasy", "Science Fiction"],
    "A marine on alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
    "http://www.youtube.com/watch?v=-9ceBgWV8io",  # NOQA
    2009
    )

# Deadpool Movie: title, duration, genres, storyline, poster, trailer
deadpool = media.Movie(
    "Deadpool",
    "1h 48min",
    ["Adventure", "Action", "Comedy"],
    "A fast-talking mercenary with a morbid sense of humor "
    "is subjected to a rogue experiment that leaves him"
    " with accelerated healing powers and a quest for revenge.",
    "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Xithigfg7dA",  # NOQA
    2016
    )

# TV Shows
# Below are the instances of TV Shows,
# You can make changes in this section to add/remove/edit information of movies

# Game of Thrones TVShow: title, duration, genres, storyline, poster, trailer
game_of_thrones = media.TvShows(
    "Game of Thrones",
    "56min",
    ["Adventure", "Drama", "Fantasy"],
    "Nine noble families fight for control"
    " over the mythical lands of Westeros, "
    "while a forgotten race returns "
    "after being dormant for thousands of years.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/Game_of_Thrones_Season_7.jpg/220px-Game_of_Thrones_Season_7.jpg",  # NOQA
    "https://youtube.com/watch?v=1Mlhnt0jMlg"  # NOQA
    )

#  Prison Break TVShow: title, duration, genres, storyline, poster, trailer
prison_break = media.TvShows(
    "Prison Break",
    "45min",
    ["Action", "Crime", "Drama"],
    "Seven years later, thanks to information provided by T-Bag, "
    "Lincoln and Sara discover that Michael is still alive in a Yemen prison",
    "https://upload.wikimedia.org/wikipedia/en/8/84/Prison_Break_%28miniseries%29.jpg",  # NOQA
    "https://www.youtube.com/watch?v=x9T-9fZn_oA"  # NOQA
    )

# House of Cards TVShow: title, duration, genres, storyline, poster, trailer
house_of_cards = media.TvShows(
    "House of Cards",
    "51min",
    ["Drama"],
    "A Congressman works with his equally conniving wife "
    "to exact revenge on the people who betrayed him.",
    "https://upload.wikimedia.org/wikipedia/en/a/aa/House_of_Cards_Season_5_Promo.jpg",  # NOQA
    "https://www.youtube.com/watch?v=UW8Zyt8SF_U"  # NOQA
    )

# Set the movies that will be passed to the media file
movies = [
    toy_story,
    avatar,
    deadpool
    ]
# Set the TV shows that will be passed to the media file
tvshows = [
    game_of_thrones,
    prison_break,
    house_of_cards
    ]

# Open the HTML file in a web browser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies, tvshows)
