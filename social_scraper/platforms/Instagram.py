from .Platform import Platform
from social_scraper.collections.InstagramPosts import InstagramPosts
from social_scraper.items.InstagramPost import InstagramPost

import json
import subprocess
import re
import datetime


class Instagram(Platform):
    def search(self, searchQuery):
        arguments = ['snscrape',
                     '--json']

        if searchQuery.getStartDate() != None:
            arguments.extend(['--since', searchQuery.getStartDate()])

        if searchQuery.getMaximumItemCount() > 0:
            arguments.extend(
                ['--max-results', str(searchQuery.getMaximumItemCount())])

        arguments.extend(['instagram-hashtag', searchQuery.getQuery()])

        process = subprocess.Popen(arguments, stdout=subprocess.PIPE)

        posts = []

        i = 1
        while True:
            data = process.stdout.readline()
            if data == b'':
                break
            else:
                jsonData = json.loads(data.decode("UTF-8"))

                post = InstagramPost()
                matches = re.findall(r"\/p\/([A-Za-z0-9_-]+)\/", jsonData["cleanUrl"])
                post.setId(matches[0])
                post.setText(jsonData["content"])
                post.setLikeCount(jsonData["likes"])
                post.setDate(datetime.datetime.strptime(jsonData["date"], "%Y-%m-%dT%H:%M:%S+00:00"))
                post.setImageURL(jsonData["displayUrl"])
                posts.append(post)

                if searchQuery.isVerboseEnabled() == True:
                    print(f"Downloading tweet #{i} from {post.getDate()} ...")
                i = i + 1

        postCollection = InstagramPosts()
        postCollection.setItems(posts)

        return postCollection