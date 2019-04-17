import webbrowser


class Video():
    """This class provides a way to store basic information about a video"""

    def __init__(self, title, duration, genere):
        self.title = title
        self.duration = duration
        self.genere = genere


class Movie(Video):
    """This class provides a way to store movie related information"""

    def __init__(
            self, movie_title, movie_duration,
            genere, movie_storyline, poster_image,
            trailer_youtube, release_year):
        Video.__init__(self, movie_title, movie_duration, genere)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_year

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShows(Video):
    """This class provides a way to store information specific to TvShows"""

    def __init__(
            self, tvshow_title, tvshow_duration,
            genere, tvshow_storyline, poster_image,
            trailer_youtube):
        Video.__init__(self, tvshow_title, tvshow_duration, genere)
        self.storyline = tvshow_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
