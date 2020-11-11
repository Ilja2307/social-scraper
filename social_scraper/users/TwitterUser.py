from .User import User


class TwitterUser(User):
    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def setDisplayName(self, displayName):
        self.displayName = displayName

    def getDisplayName(self):
        return self.displayName

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setVerified(self, isVerifiedUser):
        self.isVerifiedUser = isVerifiedUser

    def isVerified(self):
        return self.isVerifiedUser

    def setFollowerCount(self, followerCount):
        self.followerCount = followerCount

    def getFollowerCount(self):
        return self.followerCount

    def setFollowingCount(self, followingCount):
        self.followingCount = followingCount

    def getFollowingCount(self):
        return self.followingCount
