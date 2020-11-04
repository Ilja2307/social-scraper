from .Collection import Collection
import json
import csv


class Tweets(Collection):
    def saveAsCSV(self, path):
        with open(path, 'w', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "date", "username", "text"])
            for tweet in self.items:
                id = tweet.getId()
                username = tweet.getUsername()
                date = tweet.getDate()
                text = tweet.getText()

                writer.writerow([id, date, username, text])
