from .CollectionItem import CollectionItem

class InstagramPost(CollectionItem):
    def setId(self, id):
        self.id = id
    
    def getId(self):
        return self.id

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setImageURL(self, imageURL):
        self.imageURL = imageURL

    def getImageURL(self):
        return self.imageURL

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def setLikeCount(self, likeCount):
        self.likeCount = likeCount

    def getLikeCount(self):
        return self.likeCount
