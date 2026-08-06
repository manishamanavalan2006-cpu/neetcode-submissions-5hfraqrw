from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        listdata = []

        # User's own tweets
        if userId in self.tweets:
            for tweet in self.tweets[userId]:
                listdata.append(tweet)

        # Tweets from followed users
        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.tweets:
                    for tweet in self.tweets[followee]:
                        listdata.append(tweet)

        listdata.sort(key=lambda x: x[0], reverse=True)

        result = []
        for tweet in listdata[:10]:
            result.append(tweet[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent self-follow
        if followerId == followeeId:
            return

        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)