from .Platform import Platform
from social_scraper.items.Tweet import Tweet
from social_scraper.collections.Tweets import Tweets

import json
import subprocess


class Twitter(Platform):
    def search(self, searchQuery):
        arguments = ['snscrape',
                     '--json']

        if searchQuery.getMaximumItemCount() > 0:
            arguments.extend(
                ['--max-results', str(searchQuery.getMaximumItemCount())])

        arguments.extend(['twitter-search', searchQuery.getQuery()])

        process = subprocess.Popen(arguments, stdout=subprocess.PIPE)

        tweets = []

        i = 1
        while True:
            data = process.stdout.readline()
            if data == b'':
                break
            else:
                jsonData = json.loads(data.decode("UTF-8"))
                tweet = Tweet()
                tweet.setId(jsonData["id"])
                tweet.setUsername(jsonData["user"]["username"])
                tweet.setText(jsonData["content"])
                tweet.setDate(jsonData["date"])

                tweets.append(tweet)

                if searchQuery.isVerboseEnabled() == True:
                    print(f"Downloading tweet #{i} ...")
                i = i + 1

        tweetCollection = Tweets()
        tweetCollection.setItems(tweets)

        return tweetCollection
