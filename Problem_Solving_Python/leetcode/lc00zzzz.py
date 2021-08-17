from random import random

print([random.randint(0,100) for _ in range(100)])

# import math
# # arr = [12,18,21]
# # print(sum(arr)/3)
# # arr=[11,12,12,14,15,16,17,18,19,20]
# arr=[ 51.73541667, 36.03222222, 24.60333333, 21.2575, 24.36136364, 35.685, 27.75666667, 24.45458333, 30.70391304, 44.04875, 36.41833333, 23.48291667, 34.08708333, 27.58291667, 40.6575, 37.85375, 28.5075, 31.82652174, 30.42318182, 41.87833333, 63.28521739, 34.23083333, 39.90291667, 48.22833333, 31.58541667, 39.69416667, 36.0185, 53.47958333, 49.86916667, 53.56166667, 33.68304348]
# def pm_freq(arr):
#     avg=sum(arr)/len(arr)
#     arr=[(a-avg)/avg for a in arr]
#     no_of_classes=10
#     arr=[math.ceil(a*no_of_classes) for a in arr]
#     buckets=[0]*no_of_classes
#     minn=min(arr)
#     arr=[a+minn for a in arr]
#     for a in arr:
#         buckets[a]+=1
#     return buckets
# ans=pm_freq(arr)
# print(ans)
# print(sum(ans))


# arr=[11,12,12,14,15,16,17,18,19,20]
# arr=[ 51.73541667, 36.03222222, 24.60333333, 21.2575, 24.36136364, 35.685,
#       27.75666667, 24.45458333, 30.70391304, 44.04875, 36.41833333, 23.48291667,
#       34.08708333, 27.58291667, 40.6575, 37.85375, 28.5075, 31.82652174,
#       30.42318182, 41.87833333, 63.28521739, 34.23083333, 39.90291667,
#       48.22833333, 31.58541667, 39.69416667, 36.0185, 53.47958333, 49.86916667,
#       53.56166667, 33.68304348]

arr = [random.randint(0,1000) for _ in range(10**6)]
def pm_freq(arr):
    minn=min(arr)
    maxx=max(arr)+1
    diff=(maxx-minn)/10
    no_of_classes=10000
    buckets=[0]*no_of_classes
    for a in arr:
        for i in range(no_of_classes):
            if minn+diff*i<=a<minn+diff*(i+1):
                buckets[i]+=1
                # break
    return buckets

ans=pm_freq(arr)
print(ans)
print(sum(ans))
