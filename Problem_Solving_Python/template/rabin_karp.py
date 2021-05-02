# https://www.geeksforgeeks.org/python-program-for-rabin-karp-algorithm-for-pattern-searching/
def myord(char):
    return ord(char)-ord('a')+1

def search(pat, txt, prime):
    base = 10
    n = len(pat)
    m = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, n-1)% prime"

    for i in range(n-1):
        h = (h * base) % prime

    # h = pow(d,n-1)%prime # also works

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(n):
        p = (p*base + myord(pat[i]))    % prime
        t = (t*base + myord(txt[i]))    % prime

    # Slide the pattern over text one by one
    for i in range(m-n + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(n):
                if txt[i + j] != pat[j]:
                    break
            j+= 1
            # if p == t and pat[0...n-1] = txt[i, i + 1, ...i + n-1]
            if j == n:
                print("Pattern found at index " + str(i))

            # also works
            # if pat==txt[i:i+n]:
            #     print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < m-n:
            t = t-myord(txt[i])*h
            t = t * base
            t = t+myord(txt[i+n])
            t = t % prime
            # one liner
            # t = (base * (t - myord(txt[i]) * h) + myord(txt[i + n])) % prime

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + prime

# Driver program to test the above function
txt = "dabceabc"
pat = "abc"
prime = 100000000 # changed for visualization
search(pat, txt, prime)
