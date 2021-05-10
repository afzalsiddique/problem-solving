# https://www.youtube.com/watch?v=edJ19qIL8WQ
from bisect import *
# BISECT_LEFT RETURNS FIRST OCCURRENCE OF X IF EXISTS ELSE NEXT POINTER OF X
# BISECT_RIGHT RETURNS NEXT POINTER OF X


def my_bisect_left(arr,x):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid = lo+(hi-lo)//2
        if x<=arr[mid]:
            hi=mid-1
        else:
            lo=mid+1
    # if increasing array: return lo
    # if decreasing array: return hi
    return lo

def my_bisect_right(arr,x):
    lo=0
    hi=len(arr)-1
    while lo<=hi:
        mid = lo+(hi-lo)//2
        if x>=arr[mid]:
            lo=mid+1
        else:
            hi=mid-1
    # if increasing array: return lo
    # if decreasing array: return hi
    return lo

print('CHECK IF X EXISTS IN ARRAY OR NOT USING BISECT LEFT')
def if_exists_using_left(arr, x):
    # USING BISECT_LEFT
    idx = bisect_left(arr,x)
    if idx!=len(arr) and arr[idx]==x:
        print('idx: ',idx,'val: ',arr[idx])
    else:
        print('does not exists')
arr = [1,4,5,8,9]
if_exists_using_left(arr, 4)
if_exists_using_left(arr, 3)
if_exists_using_left(arr, 10)

print('CHECK IF X EXISTS IN ARRAY OR NOT USING BISECT RIGHT')
def if_exists_using_right(arr,x):
    # USING BISECT_RIGHT
    idx = bisect_right(arr,x)
    if idx!=0 and arr[idx-1]==x:
        print('idx: ',idx-1,'val: ',arr[idx-1])
    else:
        print('does not exists')
arr = [1,4,5,8,9]
if_exists_using_right(arr, 4)
if_exists_using_right(arr, 3)
if_exists_using_right(arr, 10)

print('FIRST OCCURRENCE OF X')
def first_occurrence(arr,x):
    idx=bisect_left(arr,x)
    if idx!=len(arr) and arr[idx]==x:
        print('idx: ',idx,' val: ',arr[idx])
    else:
        print('does not exist')

arr = [1,4,4,4,4,9,9,10,11]
first_occurrence(arr,4)
first_occurrence(arr,0)
first_occurrence(arr,12)


print('LAST OCCURRENCE OF X')
def last_occurrence(arr,x):
    idx=bisect_right(arr,x)
    if idx!=0 and arr[idx-1]==x:
        print('idx: ',idx-1,' val: ',arr[idx-1])
    else:
        print('does not exist')

arr = [1,4,4,4,4,9,9,10,11]
last_occurrence(arr,4)
last_occurrence(arr,0)
last_occurrence(arr,12)

print('LARGEST NUMBER LESS THAN X')
def largest_no_less_than_x(arr, x):
    idx = bisect_left(arr,x)
    if idx!=0:
        print('idx: ',idx-1,' val: ',arr[idx-1])
    else:
        print('does not exist')
arr = [1,4,4,4,4,9,9,10,11]
largest_no_less_than_x(arr, 4)
largest_no_less_than_x(arr, 0)
largest_no_less_than_x(arr, 11)

print('SMALLEST NUMBER GREATER THAN X')
def smallest_no_greater_than_x(arr, x):
    idx = bisect_right(arr,x)
    if idx!=len(arr):
        print('idx: ',idx,' val: ',arr[idx])
    else:
        print('does not exist')
arr = [1,4,4,4,4,9,9,10,11]
smallest_no_greater_than_x(arr, 4)
smallest_no_greater_than_x(arr, 0)
smallest_no_greater_than_x(arr, 11)

