t = int(input())
for _ in range(t):
    word=input()
    length=len(word)
    lenMinus2=length-2
    if length<=10:
        print(word)
    else:
        print(word[0]+str(lenMinus2)+word[-1])
