import itertools
import operator
from bisect import *
from collections import deque
from typing import List

di = {1:7,2:5,3:4}
print(max(di,key=di.get))