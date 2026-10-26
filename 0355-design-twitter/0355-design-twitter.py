import collections
import heapq

class Twitter(object):

    def __init__(self):
        self.timestamp = 0
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.timestamp += 1
        self.tweets[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                idx = len(self.tweets[u]) - 1
                neg_time, tweetId = self.tweets[u][idx]
                heapq.heappush(heap, (neg_time, tweetId, u, idx))

        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId, u, idx = heapq.heappop(heap)
            feed.append(tweetId)
            if idx > 0:
                next_neg_time, next_tweetId = self.tweets[u][idx - 1]
                heapq.heappush(heap, (next_neg_time, next_tweetId, u, idx - 1))

        return feed

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)