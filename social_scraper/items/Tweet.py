from .CollectionItem import CollectionItem


class Tweet(CollectionItem):
    def setAuthor(self, user):
        self.author = user

    def getAuthor(self):
        return self.author

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setRetweetCount(self, retweetCount):
        self.retweetCount = retweetCount

    def getRetweetCount(self):
        return self.retweetCount

    def setLikeCount(self, likeCount):
        self.likeCount = likeCount

    def getLikeCount(self):
        return self.likeCount
