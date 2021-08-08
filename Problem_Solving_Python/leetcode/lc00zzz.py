import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def turn_on(jobs,job_id):
    return jobs|1<<job_id
jobs=8
idx =4
print(turn_on(jobs,idx))