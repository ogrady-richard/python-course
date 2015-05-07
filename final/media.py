class Movie:
    ## Movie object constructor
    #  @param t | The movie title
    #  @param p | The movies poster image URL
    #  @param u | The movies trailer URL
    #  @param a | An array of actors
    #  @param r | The movie release date
    def __init__(self, t='', p='', u='', a=[], rel='', rate=0):
        self.title = t
        self.poster_image_url = p
        self.trailer_youtube_url = u
        self.actors = a
        self.release = rel
        self.rating = rate
