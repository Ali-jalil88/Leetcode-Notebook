'''
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Example 1:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:
Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:
Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

'''
words = ["leet","code"] # [0,1]
x = "e"
def findWordsContaining(words,x):
    result=[]
    for word in range(len(words)):
        if x in words[word]:
         result.append(word)
    return result
print("Perfect solving : " , findWordsContaining(words,x))

words = ["leet","code"] # [0,1]
x = "e"
def findWordsContaining(words,x):
   result_Perfect = [word for word in range(len(words)) if x in words[word]]
   return result_Perfect
print("result_Perfect-list Comprehension : " , findWordsContaining(words,x))

words = ["leet","code"] # [0,1]
x = "e"
def findWordsContaining(words,x):
    result=[]
    for word in words:
        if x in word:
         result.append(words.index(word))
    return result
print("Normal : " , findWordsContaining(words,x))

words = ["leet","code"] # Output: [0,1]
x = "e"
def findWordsContaining(words,x):
 result = [words.index(word) for word in words if x in word]
 return result
print("Example 1 -- list Comprehension" , findWordsContaining(words,x))

words = ["abc","bcd","aaaa","cbc"] # Output:[0,2]
x = "a"
def findWordsContaining(words,x):
 result = [words.index(word) for word in words if x in word]
 return result
print("Example 2 -- list Comprehension" , findWordsContaining(words,x))

words = ["abc","bcd","aaaa","cbc"] # Output: []
x = "z"
def findWordsContaining(words,x):
 result = [words.index(word) for word in words if x in word]
 return result
print("Example 3 -- list Comprehension" , findWordsContaining(words,x))
