"""
Video and its Child-classes.
A set of classes to implement media content in an Object Oriented
"""


class Video(object):
    """
    A general class for video content
    """
    def __init__(self, title, youtube_url, image_url):
        self.title = title
        self.url = youtube_url
        self.image_url = image_url

    def print_title(self):
        return "title: " + str(self.title)

    def print_url(self):
        return "title: " + str(self.title)

    def print_image(self):
        return "title: " + str(self.image_url)


class Movie(Video):
    """
    A class to describe movies
    """
    def __init__(self, title, youtube_url, image_url, movie_storyline):
        super().__init__(title=title, youtube_url=youtube_url, image_url=image_url)
        self.storyline = movie_storyline


class TvSeries(Video):
    """
    A class to describe TV series
    """
    def __init__(self, title, youtube_url, image_url, season):
        super().__init__(title, youtube_url, image_url=image_url)
        self.season = season


class MusicVideo(Video):
    """
    A class to describe music videos
    """
    def __init__(self, title, youtube_url, image_url, performer):
        super().__init__(title, youtube_url, image_url)
        self.performer = performer

