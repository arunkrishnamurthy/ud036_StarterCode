"""
File contains data structure for data types video and movie
"""
import webbrowser


class Video():
    """
    This class provides a structure to all video media types
    """
    def __init__(self, title, duration):
        """
        This is the constructor for the class Video.
        It initializes a instance of Video type.
        Attributes are video's title and duration.
        """
        # instance variables
        self.title = title
        self.duration = duration


class Movie(Video):
    """
    This class provides a structure to all media type of type Movie
    """
    def __init__(
                self,
                title,
                duration,
                story_line,
                poster_image_url,
                trailer_youtube_url):
        """
        This is the constructor for the class Movie
        It initializes a instance of Movie type with movie's title,
        duration, story line, poster image url and trailer youtube url.
        """
        # instance variables
        Video.__init__(self, title, duration)
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

        """
        instance method, which would open the browse
        and launch a instance's trailer
        """
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)
