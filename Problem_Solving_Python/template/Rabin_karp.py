#https://github.com/TheAlgorithms/Python/pull/344/files
def toNum(char):
    return ord(char)-96
def rabin_karp(text, pat,base=27,prime=1013):
    pat_len = len(pat)
    text_len = len(text)
    hash_pat = 0
    hash_window = 0
    
    # Compute initial hash values for pattern and window
    for i in range(pat_len):
        hash_pat = (hash_pat + toNum(pat[i])) % prime
        hash_window = (hash_window + toNum(text[i])) % prime
        hash_pat = hash_pat * base
        hash_window = hash_window * base
    multiplier = base ** (pat_len-1)
    for i in range(text_len-pat_len+1):
        window = text[i:i+pat_len]
        if hash_pat==hash_window and window == pat:
            return True
        #last iteration should not update the hash_window
        if i!=text_len-pat_len:
            hash_window = hash_window - toNum(text[i]) * multiplier # Remove leftmost character from hash
            hash_window *= base # Shift all characters left by 1
            char = text[i+pat_len] #the char which will be added to the window
            hash_window = (hash_window + toNum(char)) % prime # Add new character to hash
    return False
