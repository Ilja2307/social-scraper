from .Collection import Collection
import json


class Tweets(Collection):
    def saveAsCSV(self, path):
        with open(path, 'w', encoding="utf-8") as file:
            for tweet in self.items:
                id = json.dumps(tweet.getId())
                username = json.dumps(tweet.getUsername())
                date = tweet.getDate()
                text = json.dumps(tweet.getText(), ensure_ascii=False)

                file.write(f"{id},{date},{username},{text}\n")
