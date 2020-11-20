from .Platform import Platform
from social_scraper.items.Tweet import Tweet
from social_scraper.collections.Tweets import Tweets
from social_scraper.users.TwitterUser import TwitterUser

import json
import subprocess


class Twitter(Platform):
    def search(self, searchQuery):
        arguments = ['snscrape',
                     '--json']

        if searchQuery.getMaximumItemCount() > 0:
            arguments.extend(
                ['--max-results', str(searchQuery.getMaximumItemCount())])

        query = searchQuery.getQuery()

        if searchQuery.getStartDate() != None:
            query = f"{query} since:{searchQuery.getStartDate()}"

        if searchQuery.getEndDate() != None:
            query = f"{query} until:{searchQuery.getEndDate()}"

        arguments.extend(['twitter-search', query])

        process = subprocess.Popen(arguments, stdout=subprocess.PIPE)

        tweets = []

        i = 1
        while True:
            data = process.stdout.readline()
            if data == b'':
                break
            else:
                jsonData = json.loads(data.decode("UTF-8"))

                user = TwitterUser()
                user.setId(jsonData["user"]["id"])
                user.setUsername(jsonData["user"]["username"])
                user.setDisplayName(jsonData["user"]["displayname"])
                user.setLocation(jsonData["user"]["location"])
                user.setVerified(jsonData["user"]["verified"])
                user.setFollowerCount(jsonData["user"]["followersCount"])
                user.setFollowingCount(jsonData["user"]["friendsCount"])

                tweet = Tweet()
                tweet.setId(jsonData["id"])
                tweet.setAuthor(user)
                tweet.setText(jsonData["content"])
                tweet.setDate(jsonData["date"])
                tweet.setLikeCount(jsonData["likeCount"])
                tweet.setRetweetCount(jsonData["retweetCount"])

                tweets.append(tweet)

                if searchQuery.isVerboseEnabled() == True:
                    print(f"Downloading tweet #{i} from {tweet.getDate()} ...")
                i = i + 1

        tweetCollection = Tweets()
        tweetCollection.setItems(tweets)

        return tweetCollection
