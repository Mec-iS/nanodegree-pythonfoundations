"""
Video and its Child-classes.
A set of classes to implement media content in an Object Oriented way
"""


class Video(object):
    """
    A general class for video content
    """
    def __init__(self, title, youtube_url, image_url):
        self.title = title
        self.url = youtube_url
        self.image_url = image_url
        self.trailer_youtube_id = None

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

    def get_content(self, tile_content):
        content = tile_content.format(
            title=self.title,
            trailer_youtube_id=self.trailer_youtube_id,
            poster_image_url=self.image_url,
            color="orange",
            type="Movie"
        )
        return content


class TvSeries(Video):
    """
    A class to describe TV series
    """
    def __init__(self, title, youtube_url, image_url, season):
        super().__init__(title, youtube_url, image_url=image_url)
        self.season = season

    def get_content(self, tile_content):
        content = tile_content.format(
            title=self.title + ' S' + self.season,
            trailer_youtube_id=self.trailer_youtube_id,
            poster_image_url=self.image_url,
            season=self.season,
            color="red",
            type="TV Series"
        )
        return content


class MusicVideo(Video):
    """
    A class to describe music videos
    """
    def __init__(self, title, youtube_url, image_url, performer):
        super().__init__(title, youtube_url, image_url)
        self.performer = performer

    def get_content(self, tile_content):
        content = tile_content.format(
            title=self.title,
            trailer_youtube_id=self.trailer_youtube_id,
            poster_image_url=self.image_url,
            performer=self.performer,
            color="blue",
            type="Music Video"
        )
        return content
