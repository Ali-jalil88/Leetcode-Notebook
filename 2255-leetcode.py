words = ["a","b","c","ab","bc","abc"]
w = "abc"
words2 = ["a","a"]
s = "aa"
def countPrefixes(words,w):
        count=0
        for word in words:
            if w.startswith(word):
                count +=1
        return count
print( "countPrefixes : " , countPrefixes(words,w))

def countPrefixes(words2,s):
        count=0
        for word in words2:
            if s.startswith(word):
                count +=1
        return count
print( "countPrefixes2 : " , countPrefixes(words2,s))