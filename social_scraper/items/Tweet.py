from .CollectionItem import CollectionItem


class Tweet(CollectionItem):
    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

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
