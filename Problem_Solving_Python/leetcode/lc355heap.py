#########WRONG ANSWER#############
import unittest
from collections import defaultdict
from heapq import *
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []
        self.id_tracker = 4294967296 # big number
        self.followers_to_followee = defaultdict(set) # set of people a user follows
        self.tweetId_di = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        heappush(self.heap, (self.id_tracker, userId))
        self.tweetId_di[self.id_tracker] = tweetId
        self.id_tracker-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        cnt = 0
        all_news = []
        newsfeed = []
        while True:
            if cnt == 10 or not self.heap:
                break
            id_tracker, followee_id = heappop(self.heap)
            if followee_id in self.followers_to_followee[userId]:
                newsfeed.append(self.tweetId_di[id_tracker])
            all_news.append((id_tracker, followee_id))
        for news in all_news:
            heappush(self.heap, news)
        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.followers_to_followee[followerId]:
            self.followers_to_followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followers_to_followee[followerId]:
            self.followers_to_followee[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        twitter = Twitter()
        twitter.postTweet(1,2)
        twitter.postTweet(2,3)
        twitter.postTweet(1,5)
        twitter.follow(2,1)
        actual = twitter.getNewsFeed(2)
        expected = [5,2]
        # self.assertEqual(expected, actual)
        twitter.unfollow(2,1)
        actual = twitter.getNewsFeed(2)
        expected = []
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.firstBadVersion(0)
        self.assertEqual(expected, actual)