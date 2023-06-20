import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Twitter()
class Twitter:
    def __init__(self):
        self.di = {} # userdata base
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.di:
            self.di[userId] = User(userId, self)
        user = self.di[userId]
        user.post(self.time,tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.di:
            self.di[userId] = User(userId, self)
        user = self.di[userId]
        return user.get_news_feed()

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.di:
            self.di[followeeId] = User(followeeId, self)
        if followerId not in self.di:
            self.di[followerId] = User(followerId, self)
        user = self.di[followerId]
        user.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.di:
            self.di[followerId] = User(followerId, self)
        user = self.di[followerId]
        user.unfollow(followeeId)

class User:
    def __init__(self, userId,twitter):
        self.userId = userId
        self.followees = [userId] # I need to follow myself
        self.posts = deque()
        self.twitter = twitter
    def post(self, time, tweetId):
        self.twitter.time += 1
        self.posts.append((time, tweetId))
        if len(self.posts)>10:
            self.posts.popleft()
    def follow(self, followeeId):
        if followeeId not in self.followees:
            self.followees.append(followeeId)
    def unfollow(self, foloweeId):
        if foloweeId in self.followees:
            self.followees.remove(foloweeId)
    def get_posts(self):
        return self.posts
    def get_news_feed(self):
        li = []
        for folowee in self.followees:
            li.extend(self.twitter.oldToNew[folowee].get_posts())
        li.sort(reverse=True)
        res = [x for _,x in li[:10]]
        return res
    def __repr__(self):
        return "id: {} followees: {} posts: {}".format(self.userId, self.followees, self.posts)


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='Twitter':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='postTweet':
                outputs.append(obj.postTweet(input[0],input[1]))
            elif cmd=='getNewsFeed':
                outputs.append(obj.getNewsFeed(input[0]))
            elif cmd=='follow':
                outputs.append(obj.follow(input[0],input[1]))
            elif cmd=='unfollow':
                outputs.append(obj.unfollow(input[0],input[1]))
        return outputs
    def test_01(self):
        commands = ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
        inputs=[     [],       [1,5],        [1],        [1,2],    [2,6],        [1],        [1,2],      [1]]
        expected = [None,      None,         [5],        None,      None,       [6,5],       None,       [5]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["Twitter","follow","getNewsFeed"]
        inputs=[     [],       [1,5],    [1]]
        expected = [None, None, []]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["Twitter","postTweet","follow","follow","getNewsFeed"]
        inputs=[      [],      [2,5],     [1,2],    [1,2],   [ 1]]
        expected = [None,      None,      None,     None,    [5]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

