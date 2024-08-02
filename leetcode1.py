words = ["one.two.three","four.five","six"]
Output: ["one","two","three","four","five","six"]

def splitWordsBySeparator(word) :
    result = []
    for x in word:
        print(f" x:  {x}")
        s = x.split(".")
        print(f" S : {s}")
        for x in s:
         result.append(x)
    return result
print(splitWordsBySeparator(words))