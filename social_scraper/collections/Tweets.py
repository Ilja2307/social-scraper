from .Collection import Collection
import json
import csv


class Tweets(Collection):
    def saveAsCSV(self, path):
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["tweet id", "date", "text", "likes", "retweets", "user id", "username",
                             "display name", "followers", "following", "user location", "is user verified"])
            for tweet in self.items:
                author = tweet.getAuthor()

                writer.writerow([tweet.getId(), tweet.getDate(), tweet.getText(), tweet.getLikeCount(), tweet.getRetweetCount(), author.getId(
                ), author.getUsername(), author.getDisplayName(), author.getFollowerCount(), author.getFollowingCount(), author.getLocation(), author.isVerified()])
