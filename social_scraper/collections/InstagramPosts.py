from .Collection import Collection
import json
import csv


class InstagramPosts(Collection):
    def saveAsCSV(self, path):
        with open(path, 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["post id", "date", "text", "likes", "image URL"])
            for post in self.items:
                writer.writerow([
                    post.getId(),
                    post.getDate(),
                    post.getText(),
                    post.getLikeCount(),
                    post.getImageURL()
                ]);
