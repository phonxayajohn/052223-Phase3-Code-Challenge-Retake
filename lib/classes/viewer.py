class Viewer:

    all = []

    def __init__(self, username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self.username = username
            Viewer.all.append(self)
        else:
            raise Exception

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 6 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception
        
    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.viewer == self]
    
    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def has_reviewed_movie(self, movie):
        return any(review.movie == movie for review in self.reviews() if review.viewer == self)
