def function1(word):
    longestword = ''
    words = word.split()
    for item in words:
        if len(item)> len(longestword):
            longestword = item
    print (longestword)

    "making some changes"


function1(input())


