items = ["abc",20,"def",7,"ghi"]
def processItems(lst):
    sumstr = ""
    total = 0
    for item in lst:
        if (type(item) == str):
            sumstr += item 
        elif (type(item) == int):
            total += item
    return sumstr, total
print(f"processing items in list : {processItems(items)}")

def reverseString(s):
    index=len(s)-1
    rev = ""
    while index >= 0:
        rev += s[index]
        index -= 1
    return rev
print(f"reversed string : {reverseString("mumbai")}")

def skipevenposInword(s):
    result = ""
    for index in range(len(s)):
        if index % 2 != 0:
            result += s[index]
    return result
print(f"string after skipping even position characters : {skipevenposInword("rajnath")}")

def countcharacters(s):
    index = 0
    count = 0
    while index < len(s):
        if s[index] != ' ':
            count += 1
        index += 1
    return count
print(f"number of characters in string : {countcharacters("rajnath singh")}")

def reversewordsinsentence(s):
    words = s.split(" ")
    newwords = ""
    index=0
    while index < len(words):
        newwords = newwords + reverseString(words[index]) + " " 
        index += 1
    return newwords
print(f"reversed words in sentence : {reversewordsinsentence("I am going home")}")
